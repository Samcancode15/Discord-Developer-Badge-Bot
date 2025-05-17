# Importing required libraries
import os
import sys

# Import Discord or install if not found
try:
    import discord
    from discord.ext import commands
except ModuleNotFoundError:
    os.system("pip install discord.py")
    import discord
    from discord.ext import commands

# Function to get the token from system arguments
def get_token() -> str | None:
    if (len(sys.argv) < 2):
        raise Exception("No Discord token provided")
    return sys.argv[1]

# Defining the bot
bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

# Function that runs when the bot starts
@bot.event
async def on_ready():
    tree = await bot.tree.sync()
    print(f"Logged in as {bot.user}\n{len(tree)} slash command(s) succesfuly loaded")

# Normal command
@bot.command()
async def badge(ctx: commands.Context):
    message = "You just ran a normal command, please instead run the slash command i.e. `/badge` to become elligible for the Discord developer badge."
    try:
        await ctx.reply(message)
    except discord.errors.NotFound:
        await ctx.send(f"{ctx.author.mention}, {message}")
    except discord.errors.Forbidden:
        raise Exception("The bot does not have required permissions to send messages in the server")
    except Exception as e:
        raise e
    
# Slash command
@bot.tree.command(name="badge", description="Run this command to get the badge")
async def badge_slash_command(interaction: discord.Interaction):
    message = f"Slash command has been ran succesfuly, go to https://discord.com/developers/active-developer to claim your developer badge."
    try:
        await interaction.response.send_message(message)
    except discord.errors.Forbidden:
        raise Exception("The bot does not have required permissions to send messages in the server")
    except Exception as e:
        raise e

# Main entry point for the file
if __name__ == "__main__":
    try:
        token = get_token()
        if token:
            bot.run(token)
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(0)
