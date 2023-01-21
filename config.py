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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAOwS4QHsB0tGh-5QuUb_b_0wZ0p_clJsc6dhbb1y3LCc7vGR8aFlSZDlmuffGbD3U81O3vFsnVEiTBwEaaSICN2pkSZtPtCVmtF_9iTBALpXYPf5YfQog_LlE6U36rk10HNe9oQy4JGKvOEen6jkZSx7BCyQHw26T8__NalLnzHQQm9KVRD0uQDOJAxXd-j6Vuo4U0Kfz_X4D4Cg5X2DorCHYW5r8BmiL5yQEVqsxpIqDZbGnnesH1x1A8OaF8IPUGfF8VEbU2B57zpAzbbz2mp79th2HQCmq9iMVtCcraeowJs7YLlwtSWagTkUU0UMYTJpBdyksDWwdi_Ljp6edvAAAAABtG5tYAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
