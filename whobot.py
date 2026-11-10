# Source code for who_joined. this bot exists because of you Bianca.

# importing stuff
import discord
import os 
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime 

# Loading .env
load_dotenv()

# Read and storing the token (in .env)
TOKEN = os.getenv("DISCORD_TOKEN")

# Redirecting it to a specific channel
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Bot perms
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True
intents.message_content = True

# Wait... here's the bot. oops
bot = commands.Bot(intents=intents, command_prefix="!")

# What the bot doin?
@bot.event
async def on_ready():
    print("Spying...")
    
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send("Spying...")

# Runs when somebody's voice status changes.
@bot.event
async def on_voice_state_update(member, before, after):

    # Timestamping 
    timestamp = datetime.now().strftime("%H:%M:%S %d.%m.%Y")

    channel = bot.get_channel(CHANNEL_ID)

    # Detects join
    if before.channel is None and after.channel is not None:

        if channel: await channel.send(f"{member.display_name} joined {after.channel.name} - {timestamp}\n")

  # Detects leave
    elif before.channel is not None and after.channel is None:

        if channel: await channel.send(f"{member.display_name} left {before.channel.name} - {timestamp}\n")

    # member switched voice chats
    
    elif before.channel != after.channel:
            
        if channel: await channel.send(f"{member.display_name} moved from {before.channel.name} to {after.channel.name} - {timestamp}\n")


# Starts bot
bot.run(TOKEN)


