# Source code for who_joined. this bot exists because of you Bianca.

# importing stuff
import discord
import os 
from dotenv import load_dotenv
from discord.ext import commands
import datetime 

# Loading .env
load_dotenv()

# Read and storing the token (in .env)
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot perms
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True
intents.message_content = True

# Wait... here's the bot. oops
bot = commands.Bot(intents=intents, command_prefix="!")

# What the bot doin?
async def starting_bot():
    print("Spying...")
bot.event(starting_bot)

# Runs when somebody's voice status changes.
async def member_status(member, before, after):

    # Detects join or a member leaving or whatever's happening
    if before.channel is None and after.channel is not None:
        
        # Timestamping 
        timestamp = datetime.now().strftime("%H:%M:%S %Y-%m-%d")

        # Prints to terminal (for redirection)
        print( f"[{timestamp}] " f"{member.name} joined " 
              f"{after.channel.name}")

        # Redirects to a file / logs entry
        with open("who_joined_vc.txt", "a", encoding="utf-8") as log:
            log.write(f"[{timestamp}] " f"{member.name} joined "
                      f"{after.channel.name}\n")
bot.event(member_status)

# Starts bot
bot.run(TOKEN)


# wip


