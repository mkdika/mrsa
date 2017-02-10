from flask import Flask
from flask import request, render_template, abort, g, url_for, redirect

import sqlite3
import string
from nltk.corpus import stopwords

import numpy

import forms

def text_process(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in 
            stopwords.words('english')]

from moviesa import process_sentiment


app = Flask(__name__)
app.config.from_object('config.Development')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        if app.config['DB_TYPE'] == 'sqlite':
            db = g._database = sqlite3.connect(app.config['DATABASE'])
            db.row_factory = sqlite3.Row
        elif app.config['DB_TYPE'] == 'mysql':
            import pymysql
            db = g._database = pymysql.connect(host=app.config['DB_HOST'],
                                               user=app.config['DB_USER'],
                                               password=app.config['DB_PASSWORD'],
                                               db=app.config['DATABASE'],
                                               cursorclass=pymysql.cursors.DictCursor)
    return db

def query_db(query, args=(), one=False):
    if app.config['DB_TYPE'] == 'sqlite':
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        result = (rv[0] if rv else None) if one else rv
    else:
        with get_db().cursor() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchone() if one else cursor.fetchall()
    #return (rv[0] if rv else None) if one else rv
    return result

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'], endpoint='index')
def index():
    form = forms.SentimentForm()
    data = query_db("select * from sentiment order by id desc")
    if form.validate_on_submit():
        sentiment = request.form.get('sentiment', None).strip()
        if sentiment is None:
            return abort(400)
        pred = numpy.asscalar(numpy.int16(process_sentiment(sentiment)))

        db = get_db()
        cur = db.cursor()
        #cur.execute('insert into \
        #        sentiment(sentiment, pred) \
        #        values(:sentiment, :pred)', 
        #        dict(sentiment=sentiment, pred=int(pred)))
        cur.execute('insert into \
                sentiment(sentiment, pred) \
                values(%s, %s)',
                (sentiment, pred,))
        db.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form, data=data)


@app.route('/delete/<idx>', methods=['GET'], endpoint='delete_sentiment')
def delete_sentiment(idx):
    db = get_db()
    cur = db.cursor()
    #cur.execute("delete from sentiment where id=:id", dict(id=idx))
    cur.execute("delete from sentiment where id=%d", (idx,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
