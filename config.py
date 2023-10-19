#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5994504457:AAHoE-YeAOmxI9lW0xO_I1C1YojUurz5Ip4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "19972075"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e3a96479a13413b964d26ccb9edfefd5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002024089916"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6018746976"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://happythehour:skumar(2006)@cluster0.wttyshn.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "SAHIL")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "I'm Alive.....!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6018746976").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{filename}\n\n{💝 𝗝𝗼𝗶𝗻 𝗕𝗮𝗰𝗸𝗨𝗽 : <a href=https://t.me/luluofficiall>𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒆</a> 👈\n💝 𝗠𝗼𝘃𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 : <a href=https://t.me/luluofficiall>𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒆</a> 👈}")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Don't Send Me Massage....!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6018746976)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)