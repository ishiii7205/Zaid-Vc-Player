## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME","BQG3f2wAu6sOQCaiwNcBYq9O3EYJgZ1YEuzjq6Me7CTB8fESE0gKT6JgjIN145oSAbro86pQwWIsHmeTbZ98EwfXRvUL-S-ulWsvA1FdW2rTviunX-gd7y80e_r5Fvh8ZmhwLlGrEs9hFBjyDNN5DbkNIn8SfLzMTo0659N24LnpmkrhI-34Nx_FXyHbwHqoKEVoZvJPN59Ay7Tr-Ayy7x9EbQY5V2uNh9mCAK9eTWHTu2SKnE5gRkvO7JHGXYCQpB35RW-wzB3GRJlFDpI731KrEwqWSjZcIkc7e-v0VqLpTkWuITtdD_Cuoh7wEJNGOBMVssTo-nCvYVkOuiHRuKn55O1FKQAAAAFjkrjPAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5919328396:AAFRpPV0gMzUuCMWul5rxmAECMsSpEmQNmM")
BOT_NAME = getenv("BOT_NAME", "◄⏤͟͟͞🪺⃝⃪ ⃪ͥ͢ ᷟ𝐈𝛕ᷟ͢𝚣⃪ꙴ❥𝆺꯭𝅥𝗔𝗬𝗨𝗦𝗛𝗜༎ࠫ𐎓⃝🥀─‌⃛⌤𝐱𝐃𝄗⃝❣")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Devarora0987:#Dev12345@cluster0.razivtc.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "࿐🇬𝗛𝗢𝗦𝗧࿇")
OWNER_USERNAME = getenv("OWNER_USERNAME", "got_my_own_version")
ALIVE_NAME = getenv("ALIVE_NAME", "ㅤ𝄟͢🦋⃟≛⃝ 𝐌𝐑 𝄟⃝🖤𝐑𝐈𝐒𝐇𝐈💜⃟☜")
BOT_USERNAME = getenv("BOT_USERNAME", "cuteayushi_bot")
OWNER_ID = getenv("OWNER_ID", "5881100695")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "◄⏤͟͟͞🪺⃝⃪ ⃪ͥ͢ ᷟ𝐈𝛕ᷟ͢𝚣⃪ꙴ❥𝆺꯭𝅥𝗔𝗬𝗨𝗦𝗛𝗜༎ࠫ𐎓⃝🥀─‌⃛⌤𝐱𝐃𝄗⃝❣")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "the_sumpport_chat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "miss_u02")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5881100695").split()))
                                  
                                  
                             

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "110"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ishiii7205/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
