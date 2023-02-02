import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "18734981")) #optional
API_HASH = getenv("API_HASH", "0e88a144af021c41897a8e826eaf96aa") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "1830525784"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5784670818:AAGE0FoC5zpQHeDgXBH6XllEnRv1yfdN1co")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAA-ErAVUuo3z9b_qotM0FBafYggqLGWPa4E5q9okNTp59DjMOGI49vGelwLwrO4j98fR9TKPRTb-6pAKl4CPGnAxYRwYKSuHayXq6JqEJ6WFTUUMYIzxoPk_s-wwXomdjFdjN3ttOas15_owsQ1JynWH-yiBp0-w_MeCJ9QUg6sNuVL2PdkHTN1hK4EfgHFeGfpBvoPngIEuRWByJ3VKrnUDJ9PZFc0VjedW-uftzHM_9pvIHQSGkv4DW1qX1SY7w2V97SJIGlguLO1zzQUXVya8g71w8TFyO1nfOMRkRt-p2bydk_7Ii2loSpYYZvdQqqeaWve6GomndQXmvGiCNqQAAAABtG5tYAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
