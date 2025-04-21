from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

# MONGO_URL = os.getenv("MONGO_URL")
client = AsyncIOMotorClient("mongodb+srv://akhilsapplogiq:akhilsapplogiq@project01.ykcwdjt.mongodb.net/?retryWrites=true&w=majority&appName=project01")
db = client["schoolmanagement"]
