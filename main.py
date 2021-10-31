import discord
from discord.utils import get
from discord.ext import commands, tasks
import time
from datetime import datetime, timedelta
import random


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
async def verify(ctx, kod):
    channel = (828011225292079124)
    global hasloo
    if ctx.channel.id == channel:
        if hasloo == kod:
            embed1=discord.Embed(title="Weryfikacja", color=0x00fffb,timestamp=datetime.utcnow())
            embed1.add_field(name="\u200b", value="**Zostałeś/aś zweryfikowany/a!**", inline=False)
            embed1.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/White_check_mark_in_dark_green_rounded_square.svg/1024px-White_check_mark_in_dark_green_rounded_square.svg.png")
            embed1.set_footer(text = f"{ctx.author}", icon_url = ctx.author.avatar_url)
            verifyrole = (discord.utils.get(ctx.guild.roles, name = "brak weryfikacji"))
            await ctx.author.remove_roles(verifyrole)
            await ctx.author.send(embed=embed1)
            await ctx.channel.purge(limit=3)
            await ctx.send("Zweryfikowano pomyślnie")




@client.event
async def on_member_join(member):

    global hasloo


    haslo = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    haslo2 = 5

    hasloo = "".join(random.sample(haslo,haslo2))


    channel = member.guild.get_channel(828011225292079124)
    await channel.send(f"{member.mention}**Your veryfication code:** \n`{hasloo}`")


@client.event
async def on_message(message):
    global s
    channel = (828011225292079124)
    if message.channel.id == channel and message.content != "!verify" and message.author != client.user:
        await message.delete()
        embed1=discord.Embed(title="ERROR", color=0xff0000,timestamp=datetime.utcnow())
        embed1.add_field(name="\u200b", value="**Please use !verify (your code)**", inline=False)
        embed1.set_thumbnail(url = "https://emoji.gg/assets/emoji/1326_cross.png")
        await message.author.send(embed=embed1)

    await client.process_commands(message)



client.run("ODI4NjYwMDc4NTAzNzg4NjE0.YGsz1g.aX_qlKI6DI5lKSG27euCySXEK9Q")

