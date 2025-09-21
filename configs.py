from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "20652787"))
    API_HASH = getenv("API_HASH", "5dea928561e4d2eb77a371edf8b2eb2a")
    BOT_TOKEN = getenv("BOT_TOKEN", "6720259127:AAHF11Er4MAGNma2aDpkbwlF2YgAroZw2Sw")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "DP_BOTZ")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1002008853384"))
    ADMIN = list(map(int, getenv("ADMIN", "1242556540").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Aloneboy:Aloneboytg@cluster0.nmeelsr.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001789244683"))
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://te.legra.ph/file/ba16b6f4c78879c5d5527.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Auto_Accept_Dpbot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://te.legra.ph/file/ba16b6f4c78879c5d5527.jpg").split()

    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()
