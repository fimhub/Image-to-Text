# Import csv to postgresql db


import psycopg2
import pandas as pd
from psycopg2.extras import Json

conn = psycopg2.connect(
    "host=localhost dbname=img2txt_db user=postgres password=HCMCTWAG@1")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS users, condos, photos;  ")

cur.execute('''CREATE TABLE users (
    uid SERIAL PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL);''')

conn.commit()

cur.execute(
    """CREATE TABLE condos (
    uid SERIAL PRIMARY KEY NOT NULL,
    mlsnum TEXT NOT NULL,
    beds TEXT NOT NULL,
    baths TEXT NOT NULL,
    sqft TEXT NOT NULL,
    age TEXT NOT NULL,
    lot_size TEXT NOT NULL,
    garage TEXT NOT NULL,
    list_price TEXT NOT NULL,
    sold_price TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip TEXT NOT NULL,
    photo_url TEXT NOT NULL);"""
)
conn.commit()

cur.execute('''CREATE TABLE photos (
    pid SERIAL PRIMARY KEY NOT NULL,
    mlsnum INTEGER,    
    imgnum INTEGER,
    features JSONB);''')
conn.commit()


df_listings = pd.read_csv("./data/condos.zip", index_col=False, dtype={'ZIP': str})
for idx, u in df_listings.iterrows():
    # Data cleaning
    try:
        q = cur.execute(
            """INSERT INTO condos (mlsnum, beds, baths, sqft, age, lot_size, garage, list_price, sold_price, city, state, zip, photo_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (
                u.mlsnum,
                u.BEDS,
                u.BATHS,
                u.SQFT,
                u.AGE,
                u.LOTSIZE,
                u.GARAGE,
                u.LISTPRICE,
                u.SOLDPRICE,
                u.CITY,
                u.STATE,
                u.ZIP,
                u.PHOTOURL,
            ),
        )
    except:
        print("Exception", u.mlsnum)
    conn.commit()

df_condos = pd.read_csv("./data/condo_images.csv", index_col=False)
for idx, u in df_condos.iterrows():
    q = cur.execute(
        '''INSERT INTO photos (mlsnum, imgnum, features) VALUES (%s,%s,%s)''',
        (u.mlsnum, u.IMGNUM, Json(u.FEATURES))
    )
    conn.commit()

cur.close()
conn.close()
