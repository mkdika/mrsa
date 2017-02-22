# Movie Sentiment Analysis

Contoh aplikasi web untuk menganalisis sentiment sebuah movie berdasarkan komentar.

## Requirements
anaconda

pasang package berikut:
conda install nltk
conda install flask-wtf
conda install numpy

pada shell python jalankan
```
import nltk
nltk.download_shell()
```

download stopwords

## Untuk menjalankan aplikasi
jalankan `sh initdb.sh` untuk membuat database kosong.

untuk server mysql/mariadb bentuk database baru dan user sesuai dengan config.
jalankan python initdb.py untuk membuat schema pada database mysql/mariadb.

python app.py untuk menjalankan aplikasi web.

lanjutkan dengan membuka browser ke http://localhost:5000
=======
# Movie Reviews Sentiment Analysis
####Proof of Concept Project

This project consist of some section:

1. **Machine Learning Model** (model-train)
train and generate model to production.


2. **Production Web Application** (web-app)
this is webpage interface to play with sentiment analysis.

### Online Demo
[mrsa1.herokuapp.com](http://mrsa1.herokuapp.com/)
