import discord
import os # default module
from dotenv import load_dotenv
import godword

load_dotenv() # load all the variables from the env file
bot = discord.Bot()
bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "ping", description = "Check ping")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}s")

@bot.slash_command(name = "info", description = "How Oracle works")
async def info(ctx):
    await ctx.respond(f"/godsays and God will talk in Quran verses. \nVerses are chosen using random numbers. \nNumbers are generated using radioactive isotope decay, in laymans term, as random as it gets.")

@bot.slash_command(name = "godsays", description = "Make sure you made an offering before running this command. And, do not spam God. It's lame.")
async def godsays(ctx):
    await ctx.defer()
    message = str(godword.GodSays())
    await ctx.respond(f"God says: \n {message}")

bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token