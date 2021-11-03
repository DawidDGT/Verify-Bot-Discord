import discord
from discord.utils import get
from discord.ext import commands, tasks
import time
from datetime import datetime, timedelta
import random
import os

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!", help_command = None,  intents=intents)






@client.event
async def on_ready():
    print("STATUS DZIAŁA")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name ="serwer Avexa Club"))

@client.command()
@commands.has_permissions(administrator = True)
async def sandra(ctx):

    embed=discord.Embed(title="How to pass the verification?", color=0x00fffb,timestamp=datetime.utcnow())
    embed.add_field(name="\u200b", value="**Send a message to verify yourself ```!verify (your code)```**", inline=False)
    embed.add_field(name="\u200b", value="**If you have any problems with verification, report to the moderator**", inline=False)
    await ctx.send(embed=embed)



@client.command()
async def v(ctx, kod):
    channel = (828011225292079124)
    global hasloo
    if ctx.channel.id == channel:
        if hasloo == kod:
            embed1=discord.Embed(title="Done", color=0x00fffb,timestamp=datetime.utcnow())
            embed1.add_field(name="\u200b", value="**You have been verified!**", inline=False)
            embed1.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/White_check_mark_in_dark_green_rounded_square.svg/1024px-White_check_mark_in_dark_green_rounded_square.svg.png")
            embed1.set_footer(text = f"{ctx.author}", icon_url = ctx.author.avatar_url)
            verifyrole = (discord.utils.get(ctx.guild.roles, name = "weryfikacja"))
            verifyrole2 = (discord.utils.get(ctx.guild.roles, name = "weryfikacja"))
            await ctx.author.remove_roles(verifyrole)
            await ctx.author.add_roles(verifyrole2)
            await ctx.author.send(embed=embed1)
            await ctx.send("You have been verified!")
            await ctx.channel.purge(limit=2)




@client.event
async def on_member_join(member):

    global hasloo


    haslo = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    haslo2 = 5

    hasloo = "".join(random.sample(haslo,haslo2))


    channel = member.guild.get_channel(828011225292079124)
    await channel.send(f"{member.mention}**Please type:** `!v {hasloo}`")


@client.event
async def on_message(message):
    global hasloo
    channel = (828011225292079124)
    if message.channel.id == channel and message.content and message.author != client.user:
        await message.delete()
        embed1=discord.Embed(title="ERROR", color=0xff0000,timestamp=datetime.utcnow())
        embed1.add_field(name="\u200b", value=f"**Please use !v {hasloo}**", inline=False)
        embed1.set_thumbnail(url = "https://emoji.gg/assets/emoji/1326_cross.png")
        await message.author.send(embed=embed1)

    await client.process_commands(message)

TOKEN = os.getenv("BOT_TOKEN")
client.run(TOKEN)

client.run(TOKEN)




