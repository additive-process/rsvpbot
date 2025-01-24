# Replace "pineappleys" with your private channel that only you and RSVPbot will have access to.

import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()
intents.members = True  # Enable member intents

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def rsvp(ctx):
    async def button_callback(interaction):
        user = interaction.user
        channel = discord.utils.get(ctx.guild.channels, name="pineappleys")
        if channel:
            try:
                icon_url = user.display_avatar.url
                await channel.send(f"RSVP from: {user.display_name} ({user.name})\nJoined: {user.joined_at}\n{icon_url}")
                await interaction.response.send_message("RSVP recorded!", ephemeral=True)
            except Exception as e:
                print(f"An error occurred: {e}")
                await interaction.response.send_message("Failed to record RSVP. Please try again.", ephemeral=True)
        else:
            await interaction.response.send_message("Could not find #pineappleys channel.", ephemeral=True)


    button = Button(label="RSVP", style=discord.ButtonStyle.primary)
    button.callback = button_callback
    view = View()
    view.add_item(button)

    await ctx.send("Greetings! I am RSVPbot. Please indicate your attendance by clicking the button below.", view=view)
    await bot.process_commands(ctx)


bot.run('YOURTOKEN') # Replace with your bot token