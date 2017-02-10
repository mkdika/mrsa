import config
import pymysql

conn = pymysql.connect(host=config.Development.DB_HOST,
                       user=config.Development.DB_USER,
                       password=config.Development.DB_PASSWORD,
                       db=config.Development.DATABASE)

try:
    with conn.cursor() as cursor:
        sql = 'create table sentiment ( id int primary key auto_increment, sentiment text, pred int );'
        cursor.execute(sql)

    conn.commit()
finally:
    conn.close()
