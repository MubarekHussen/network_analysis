from fastapi import FastAPI
import psycopg2
import pandas as pd

app = FastAPI()


def connect_to_db():
    conn = psycopg2.connect(
        dbname='slack_data',
        user='postgres',
        password='Muba@sql14',
        host='localhost',
        port='5432'
    )
    return conn


@app.get("/sentiment")
async def fetch_sentiment_data():
    conn = connect_to_db()
    query = "SELECT * FROM sentiment_by_day;"
    df_sentiment = pd.read_sql(query, conn)
    conn.close()
    return df_sentiment.to_dict(orient='records')


@app.get("/message_count")
async def fetch_message_count():
    conn = connect_to_db()
    query = "SELECT * FROM message_count;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')


@app.get("/topics")
async def fetch_message_count():
    conn = connect_to_db()
    query = "SELECT * FROM topics;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')


@app.get("/reaction_count")
async def fetch_message_count():
    conn = connect_to_db()
    query = "SELECT * FROM user_reaction_counts;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')
