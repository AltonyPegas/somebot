from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os
from bs4 import BeautifulSoup
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
