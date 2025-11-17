#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25271238"))
API_HASH = environ.get("API_HASH", "ce508bc31389578c7cba4dda560a2b71")
BOT_TOKEN = environ.get("BOT_TOKEN", "8461696277:AAFatcYAc7094-35ezJq4pBCdGMnQI85_9E")

OWNER = int(environ.get("OWNER", "8027087942"))
CREDIT = environ.get("CREDIT", "Sarkar") 

TOTAL_USER = os.environ.get('TOTAL_USERS', '8027087942').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8027087942').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
