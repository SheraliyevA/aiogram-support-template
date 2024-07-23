from dotenv import load_dotenv
import os
import json
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

load_dotenv()


BOT_TOKEN = os.environ.get("BOT_TOKEN") 
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
PROXY_URL = os.environ.get("PROXY_URL")  # Bot uchun proxy

IP = os.environ.get("ip")  # Xosting ip manzili
# operatorlarni Telegram ID-larini yozing
support_ids = [
    1981467845,
] 