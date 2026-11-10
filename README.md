# Who Joined?

**WhoJoined** is a Discord bot that logs voice channel activity.

- The bot can detect when somebody joins a voice channel.
- The bot can detect when somebody leaves a voice channel.
- The bot can detect when somebody switches between existing voice channels in a vc.
- The bot sends the recorded logs to the directed channel (pointed in .env), along with the user who changed their voice channel status,
the voice channel they left from and/or changed to, and the timestamp of when this status change happened (HH:MM:SS dd.mm.YY).

## Example Output

claudia de lioncourt joined Theatre de Vampires - 12:07:31 10.11.2026
claudia de lioncourt moved from Theatre de Vampires to Rat Box - 12:07:45 10.11.2026
claudia de lioncourt left Rat Box - 12:07:54 10.11.2026

# Why

- This is not the files of a 24/7-hosted Discord bot. I hosted this on my own PC for the server that I'm in. You copying these files will not mean
that you will get the finished product. You need to follow the instructions to make it your own (given under "Installations", and after).
- Do read the "Notes" section before you decide to push your own files.

## Requirements

Python: anything above 3.10
Token(s): Discord bot token
Imports: discord.py, python-dotenv
ID: Channel ID

# Installation

### Clone the repository:

```
git clone https://github.com/manisamesirmacunu/who-joined.git
cd who-joined
```

### Create a virtual environments:

```
python -m venv .venv
```

### Activate the virtual environment:

#### Windows

```
.\.venv\Scripts\Activate.ps1
```

#### Linux/macOS

```
source .venv/bin/activate
```

### Install dependencies: 

```
pip install -r requirements.txt
```

# Creating your own Discord bot

1. Create an application.

Go to the Discord Developer Portal (https://discord.com/developers) and click "New Application".

Add a name or a profile picture for the bot if you want.

2. Create the bot.

Go to the "Bot" section and click "Add Bot".

3. Enable Intents

Below "Privileged Gateway Intents", check "Server Members Intent" and "Message Content Intent". Don't forget to save changes.

4. Get the bot token

Go to the "Bot" section again and click "Reset Token" and copy the token shown.

5. Get the Discord link

Go to "OAuth2" and check the "Bot" scope and the "View Channels", and "Send Messages" permissions.
Copy the generated link below (the checked stuff will dissapear after refreshing, you only need the Discord link though.)

6. Get a channel ID

On your Discord Settings, enable "Developer Mode". This mode will allow you to right-click a channel you want the log messages to 
go to and copy the Channel ID.

# Creating your Environmental Variables

Create a file inside the folder called `.env`. 

Define a "DISCORD_TOKEN" and a "CHANNEL_ID" variable inside the file. Paste the token you got from the Discord Developer Portal in front of the 
discord token variable (e.g. `DISCORD_TOKEN= MTUSHDSDGSSASDG...`). Get the channel ID (the channel you want the logs to appear in) and paste that in
front of the channel id variable (e.g. `CHANNEL_ID=123456...`). 

Here's an example:

```
DISCORD_TOKEN=MTUADSADLSD...
CHANNEL_ID=
```

Don't forget the save the files after changes to make the bot run at the current modified file.

# Invite the bot

Paste the URL link from the Discord Developer page on any browser of your choice and invite the bot to your server. 
Click the green button to authenticate the bot and invite it to the server.

# Starting the bot

If everything's in place, everytime you run:

```
python whobot.py
```

in your terminal *(any that is in the right directory works, I used VS Code's terminal)*, the message

```
Spying...
```

 will appear in your desired channel and your terminal. This is a startup message to indicate that the bot is now active.

 # The files you should have by the end of this

 Under the `who-joined` folder:

```
 whobot.py
 requirements.txt
 .gitignore
 .env
 README.md
```

in no particular order.

# Notes

- This is a personal project, make sure your bot token is not exposed or posted anywhere.
- Don't upload or expose your `.env` file anywhere.
- Don't upload or expose your `.venv` folder anywhere.

# License

None