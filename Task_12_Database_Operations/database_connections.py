from mysql import connector
import psycopg2

def connect_sql():
    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "ajay"
    )
    return mydb

def connect_postgres():
    conn = psycopg2.connect(
        user='postgres',
        password='ajay',
        host='localhost',
        port= '5432'
    )
    return conn