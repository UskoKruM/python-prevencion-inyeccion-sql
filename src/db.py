from decouple import config
import pymysql
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=config('MYSQL_HOST'),        
        database=config('MYSQL_DB'),
        user=config('MYSQL_USER'),
        password=config('MYSQL_PASSWORD')
    )
