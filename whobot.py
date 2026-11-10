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
async def starting_bot():
    print("Spying...")

# Runs when somebody's voice status changes.
@bot.event
async def on_voice_state_update(member, before, after):

    # Detects join or a member leaving or whatever's happening
    if before.channel is None and after.channel is not None:
        
        # Timestamping 
        timestamp = datetime.now().strftime("%H:%M:%S %Y-%m-%d")

        # Prints to terminal (for redirection)
        print( f"[{timestamp}] " f"{member.name} joined " 
              f"{after.channel.name}")

        # Redirects to a file / logs entry
        with open("who_joined_vc.txt", "a", encoding="utf-8") as log:
            log.write(f"[{timestamp}] {member.name} joined {after.channel.name}\n")

        channel = bot.get_channel(CHANNEL_ID)

        if channel: await channel.send(f"{member.display_name} joined {after.channel.name}")
            

# Starts bot
bot.run(TOKEN)


# wip


