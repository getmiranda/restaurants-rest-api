import csv
import sqlite3

import psycopg2
from decouple import config


conn = psycopg2.connect(
    dbname=config('NAME'), 
    user=config('USER_DB'),
    password=config('PASSWORD'),
    host=config('HOST'),
    port=config('PORT')
)
cur = conn.cursor()

query = '''
    SELECT id
    FROM restaurants_api_restaurant;
'''
cur.execute(query)

restaurant_ids = list(map(lambda item: item[0], cur.fetchall()))

with open('restaurantes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] not in restaurant_ids:
            query = '''
                INSERT INTO restaurants_api_restaurant
                (id, rating, name, site, email, phone, street, city, state, lat, lng)
                VALUES(%(id)s, %(rating)s, %(name)s, %(site)s, %(email)s, %(phone)s, %(street)s, %(city)s, %(state)s, %(lat)s, %(lng)s);
            '''
            cur.execute(query, dict(row))

conn.commit()
cur.close()
conn.close()
