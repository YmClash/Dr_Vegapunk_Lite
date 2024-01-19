import discord
import openai
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

#API KEYS
discord_api_key = os.getenv('DR_VEGAPUNK_DISCORD_API_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')

