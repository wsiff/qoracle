
from discord.ext import commands
from discord import app_commands

# Set up the bot with the command prefix (e.g., !)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Create a slash command
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, world!")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}!')

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Latency is {bot.latency}s")

@bot.tree.command(name="info", description="How Oracle works")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message(
        "/godsays and God will talk in Quran verses. \nVerses are chosen using random numbers. \nNumbers are generated using radioactive isotope decay, in layman's terms, as random as it gets."
    )
@bot.tree.command(name="godsays", description="Make sure you made an offering before running this command. And, do not spam God. It's lame.")
async def godsays(interaction: discord.Interaction):
    await interaction.response.defer()  # Defer the interaction to show the bot is processing
    message = str(godword.GodSays())
    await interaction.followup.send(f"**Quran** says: \n{message}")  # Send the follow-up message

@bot.tree.command(name="biblesays", description="Make sure you made an offering before running this command. And, do not spam God. It's lame.")
async def biblesays(interaction: discord.Interaction):
    await interaction.response.defer()  # Defer the interaction to show the bot is processing
    message = str(godword.BibleSays())
    await interaction.followup.send(f"**Bible** says: \n{message}")  # Send the follow-up message


bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token
