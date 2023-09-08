# Created By @xl444
# Copyright By watan

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQErw48Abe7oaom13KdbAGTSqnj4zXAYPuYbSi0K4xf976AOtRnG3cZTeazQX2H8U3uO6jwhl7iDex4awuDa_sF1IUqH9wp_lE7Jtr0Swy_eRloO_T4d4B9Dr8oZS0frWUwKxuN_p41HZPFfps702mlgVCbSOa8fTvt5pSMofh7KN95SwKYLANJ3REnXub2xVSxrhgrLizlvbIVf7_BvfNcz_fDNRc-sEuenS1vhLntboeeggXIDjA5rYOPxXto-8zWvCY0J6Gb76gjEEccWAK1jWlkRqHvJytYbglXh_gxKpZMVaKRoH7UA9wAOYfoFhnmX5LPDf1QBFaSOszY1-wmCwvLaLwAAAAF3kiLBAA")
BOT_TOKEN = getenv("BOT_TOKEN", "6366616416:AAGqGfjJ7yDIUZLriMXSKzUi0bQgjiqZ2cg")
BOT_NAME = getenv("BOT_NAME", "bot")
BOT_USERNAME = getenv("BOT_USERNAME", "MusikVIBOT")
ASSID = int(getenv("ASSID", "5802896978"))
ASSNAME = getenv("ASSNAME", "Kasijekg")
ASSUSERNAME = getenv("ASSUSERNAME", "Kasijekg")

BOT_ID = int(getenv("BOT_ID", "6366616416"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/LG")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID", "24590596"))
API_HASH = getenv("API_HASH", "9d16b18e6b2b6e088d6876217d80ddcc")
OWNER_ID = int(getenv("OWNER_ID", "5802896978"))
UPDATE = getenv("UPDATE", "Haider_1h1")
SUPPORT = getenv("SUPPORT", "Haider_1h1")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", ". / ! + - @ # $").split())
BG_IMG = getenv("BG_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
START_PIC = getenv("START_PIC", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
IMG_1 = getenv("IMG_1", "https://graph.org/file/475127193de2444183fd4.jpg")
IMG_2 = getenv("IMG_2", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
IMG_3 = getenv("IMG_3", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
IMG_4 = getenv("IMG_4", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")