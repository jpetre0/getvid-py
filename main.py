import os
import re
import discord
import requests
import time
import asyncio
import string
import random
import dotenv
import psycopg2


intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)


dotenv.load_dotenv()


token = os.getenv("TOKEN")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


with open("database/schema.sql", "r") as sql_file:
    init_schema = sql_file.read()


try:
    connection = psycopg2.connect(
        host=db_host, port=db_port, database=db_name, user=db_user, password=db_password
    )

    cursor = connection.cursor()

    cursor.execute(init_schema)

    connection.commit()

    print("getvid-py database schema initialised successfully.")


except (Exception, psycopg2.Error) as error:
    print(f"error: {error}")


finally:
    if connection:
        cursor.close()
        connection.close()
        print("connection closed.")


bot.run(token)
