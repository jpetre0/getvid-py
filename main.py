import os
import re
import discord
import requests
import time
import asyncio
import string
import random
import dotenv


dotenv.load_dotenv()


token = os.getenv("TOKEN")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
