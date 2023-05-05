import psycopg2
import os

con = psycopg2.connect(
    dbname='register_bot',
    user='hacker',
    password='1',
    host='localhost'
)

cur = con.cursor()
