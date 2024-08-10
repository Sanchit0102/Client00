from pyrogram import Client
from os import environ,sys,mkdir,path
import logging
import requests
from flask import Flask
from threading import Thread
import pytz
import time
from apscheduler.schedulers.background import BackgroundScheduler
from sys import executable
from aiohttp import ClientSession
from dotenv import load_dotenv
import shutil
load_dotenv("config.env")
import os 
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# Mandatory Variable
try:
    SHORTAPI = environ['SHORTAPI']
    SHORTURL = environ['SHORTURL']
    VERIFY_TUTORIAL = environ['VERIFY_TUTORIAL']  
    BOT_USERNAME = environ['BOT_USERNAME']
    VERIFY = environ['VERIFY']
    API_ID = int(environ['API_ID'])
    API_HASH = environ['API_HASH']
    BOT_TOKEN = environ['BOT_TOKEN']
    OWNER_ID = int(environ['OWNER_ID'])
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)
F_SUB = environ['F_SUB']
F_SUB_CHANNEL_ID = environ.get('F_SUB_CHANNEL_ID')
F_SUB_CHANNEL_INVITE_LINK = environ.get('F_SUB_CHANNEL_INVITE_LINK')
SUDO_USERS = environ.get("SUDO_USERS",str(OWNER_ID)).split()
SUDO_USERS = [int(_x) for _x in SUDO_USERS]
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
AUTH_CHATS = environ.get('AUTH_CHATS',None ).split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
LOG_GROUP = environ.get("LOG_GROUP", None)
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)
BUG = environ.get("BUG", None)
if BUG:
    BUG = int(BUG)
genius_api = environ.get("genius_api",None)
if genius_api:
    genius_api = genius_api
  
class Mbot(Client):
    def  __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir= "", #"./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30
        )
    async def start(self):
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists('/tmp/thumbnails/'):
            mkdir('/tmp/thumbnails/')
        LOGGER.info(f"Bot Started As {BOT_INFO.username}\n")
    
    async def stop(self,*args):
        await super().stop()
        LOGGER.info("Bot Stopped, Bye.")

RENDER_EXTERNAL_URL = environ.get("RENDER_EXTERNAL_URL", "http://localhost:5000")

def ping_self():
    url = f"{RENDER_EXTERNAL_URL}/alive"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("Ping successful!")
        else:
            logging.error(f"Ping failed with status code {response.status_code}")
    except Exception as e:
        logging.error(f"Ping failed with exception: {e}")

def start_scheduler():
    scheduler = BackgroundScheduler(timezone=pytz.utc)
    scheduler.add_job(ping_self, 'interval', minutes=3)
    scheduler.start()

app = Flask(__name__)

@app.route('/alive')
def alive():
    return "I am alive!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run_flask).start()
start_scheduler()
