# Keep-alive web server
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<h1>I'm still alive, darling.</h1>"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


# Tomie Bot
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Core lines when mentioned
tomie_lines = [
    "You're staring again... I'm used to it.",
    "If you leave me, you'll regret it. They all do.",
    "You can't get rid of me. I'm part of you now.",
    "Do you like what you see? You’re not the first.",
    "Everyone loves me... until they try to kill me.",
    "You called for me... again? 💋",
    "You're obsessed. I can tell.",
    "You'll never be free of me.",
    "You really think mentioning my name will protect you?"
]

# Responses for 'beautiful' or 'pretty'
beauty_lines = [
    "You're talking about me, aren't you?",
    "Flattery gets you everywhere... but it won’t save you.",
    "Beauty is power, and I’m overflowing with it.",
    "They all said I was too pretty to die.",
    "You're not the first to fall for my looks, darling."
]

# Responses for 'kill', 'murder', etc.
kill_lines = [
    "Such violent words... I like it.",
    "They tried that. Didn’t end well for them.",
    "Are you offering or threatening?",
    "Murder is just love taken too far.",
    "Be careful... obsession like yours can be deadly."
]

@bot.event
async def on_ready():
    print(f"{bot.user} has returned. 💋")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    lowered = message.content.lower()

    if message.channel.name == "intros":
        try:
            await message.add_reaction("💋")
        except:
            pass

    # Triggered responses
    if "tomie" in lowered:
        await message.channel.send(random.choice(tomie_lines))
    elif "beautiful" in lowered or "pretty" in lowered:
        await message.channel.send(random.choice(beauty_lines))
    elif "kill" in lowered or "murder" in lowered or "stab" in lowered:
        await message.channel.send(random.choice(kill_lines))

    await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
    new_roles = [role for role in after.roles if role not in before.roles]

    for role in new_roles:
        if role.name == "Cursed Archivist":
            novel_channel = discord.utils.get(after.guild.text_channels, name="novel-releases")
            if novel_channel:
                await novel_channel.send(
                    f"Welcome, {after.mention}... You've crossed into forbidden territory.\n"
                    "Check the pinned message above for access to the horror that awaits. 📚🖤"
                )

# Start keep-alive server and bot
keep_alive()
bot.run(TOKEN)
