import discord
import openai
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

# API KEYS
discord_api_key = os.getenv('DR_VEGAPUNK_DISCORD_API_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initilisation des modules
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
model = "gpt-4"

# on cree les deux fonction pour  1: generative  2: Generation d'image
async def demande_gpt(prompt) :
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role" : "system", "content" : "Je suis le Dr Vegapunk"},
            {"role" : "user", "content" : prompt}
        ],
        max_tokens=500,
        temperature=0.75,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    message = response.choices[0].message.content.strip()
    return message


