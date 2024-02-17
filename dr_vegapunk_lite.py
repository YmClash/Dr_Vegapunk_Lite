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
model = "gpt-4-1106-preview	"
model_Img = "dall-e-3"

# on cree les deux fonction asynchrone pour  1: generative  2: Generation d'image
async def demande_gpt(prompt) :
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role" : "assistant", "content" : "Je suis le Dr Vegapunk"},
            {"role" : "user", "content" : prompt}
        ],
        # quelque parametre pour  mieux controle  le bot
        max_tokens=500,
        temperature=0.75,
        top_p=0.75,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    message = response.choices[0].message.content.strip()
    return message

async def demande_image(prompt):
    response = openai.images.generate(
        model= model_Img,
        prompt = prompt,
        size="1024x1024",
        quality= "standard",
        n = 1,
    )
    # image_url =response['data'][0]['url']
    image_url = response.data[0].url
    return image_url


@bot.event
async def on_ready():
    print(f'We have logged in #momo-jam-cava as : {bot.user} , SUPER!!!!!!!!!!!!!!!!!  dev by Y_mC ')



#  on vas utiliser un decorateur pour cree des command
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    #addresse de la chaine discord ou
    dr_vegapunk_channel: discord.TextChannel = bot.get_channel(1099103151572926477)

    if message.content.startswith("!"):
        prompt = message.content[11:]
        response = await demande_gpt(prompt)
        await dr_vegapunk_channel.send(content=response)

    if message.content.startswith("/img"):
        prompt = message.content[11:]
        response = await demande_image(prompt)
        await dr_vegapunk_channel.send(content=response)


bot.run(discord_api_key,log_level=logging.INFO)




