from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "20652787"))
    API_HASH = getenv("API_HASH", "5dea928561e4d2eb77a371edf8b2eb2a")
    BOT_TOKEN = getenv("BOT_TOKEN", "6720259127:AAFm3tGJl03N0ByWDOvevGiM_z4lpddeNr4")
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
    SURPRICE = os.environ.get("SURPRICE", "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4 https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4 https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4 https://telegra.ph/file/293cc10710e57530404f8.mp4 https://telegra.ph/file/506898de518534ff68ba0.mp4 https://telegra.ph/file/dae0156e5f48573f016da.mp4 https://telegra.ph/file/3e2871e714f435d173b9e.mp4 https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4 https://telegra.ph/file/876edfcec678b64eac480.mp4 https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4 https://telegra.ph/file/b4834b434888de522fa49.mp4").split()

    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()
