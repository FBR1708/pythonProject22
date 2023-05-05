import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv('.env')
API_TOKEN=os.getenv("TOKEN")


bot=Bot(API_TOKEN)


storage=MemoryStorage()

dp=Dispatcher(bot, storage=storage)