import os
import json
import string
import discord, aiohttp
from discord.ext import commands, tasks
import requests
from colorama import Fore
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
import requests
import time
from discord import Color, Embed
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import re
from pystyle import Center, Colorate, Colors
import io
import webbrowser
from bs4 import BeautifulSoup
import datetime
import status_rotator

from discord import Member
import openai
import tokennn
import afk
import automessage


colorama.init()

intents = discord.Intents.default()
intents.presences = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True

legendzz = commands.Bot(description='Saifi On Top!!!',
                           command_prefix='.',
                           self_bot=True,
                           intents=intents)
status_task = None

legendzz.remove_command('help')

legendzz.whitelisted_users = {}

legendzz.antiraid = False

red = "\033[91m"
yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
pretty = "\033[95m"
magenta = "\033[35m"
lightblue = "\033[36m"
cyan = "\033[96m"
gray = "\033[37m"
reset = "\033[0m"
pink = "\033[95m"
dark_green = "\033[92m"
yellow_bg = "\033[43m"
clear_line = "\033[K"

@legendzz.event
async def on_ready():
      print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.blue_to_purple,
            f"""| LegendzzCord V1 Maded By Saifi! | Your Id = {legendzz.user.name} |""",

                1,
            )
        )
    )


def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

#=== Configs Imports! ===
api_key = config.get('apikey')
ltc_priv_key = config.get('ltckey')
ltc_addy = config.get("LTC_ADDY")
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC_ADDY")
Upi = config.get("Upi")
Qr = config.get("Qr")
User_Id = config.get("User_Id")
SERVER_Link = config.get("SERVER_Link")
#==============

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

time_rn = get_time_rn()

@legendzz.event
async def on_message(message):
    if message.author.bot:
        return

    # Auto-response handling
    with open('auto_responses.json', 'r') as file:
        auto_responses = json.load(file)

    if message.content in auto_responses:
        await message.channel.send(auto_responses[message.content])

    await legendzz.process_commands(message)
def cls():
    os.system('cls' if os.name =='nt' else 'clear') 

@legendzz.command()
async def help(ctx):
    message = (f"# <a:LG_BlueCrown:1299986907991773244> LegendzzCord V1 \n **__Personal Bot!__** \n\n <a:LG_Thunder:1299987132433043460> **__Common Commands!__** \n <a:LG_Dot:1293827362764619819> Srv Clone - `.csrv <copy> <target>` \n <a:LG_Dot:1293827362764619819> Check Promo - `.checkpromo <promolink>` \n <a:LG_Dot:1293827362764619819> Afk - `.afk <reason>` \n <a:LG_Dot:1293827362764619819> Remove Afk - `.unafk` \n <a:LG_Dot:1293827362764619819> AutoRespond - `.addar <trigger> , <response>` \n <a:LG_Dot:1293827362764619819> Remove Respond - `.removear <triger>` \n <a:LG_Dot:1293827362764619819> AutoMsg - `.auto <time> true <chnl> <msg>` \n <a:LG_Dot:1293827362764619819> Stop AutoMsg - `.stopauto <msg id>` \n <a:LG_Dot:1293827362764619819> Status Rotator -  `.start_rotation` \n <a:LG_Dot:1293827362764619819> Stop Rotator - `.stop_rotation` \n <a:LG_Dot:1293827362764619819> Spam Msg - `.spam <amount> <msg>` \n <a:LG_Dot:1293827362764619819> Clear Msg - `.clear <amount>` \n\n <:LG_IndianRupees:1299987733195915265> **__Inr Commands!__** \n <a:LG_Dot:1293827362764619819> Upi Id - `.upi` \n <a:LG_Dot:1293827362764619819> Qr Code - `.qr` \n\n <a:LG_Ltc:1299987860228931614> **__Ltc Commands!__** \n <a:LG_Dot:1293827362764619819> Send Ltc - `.send <addy> <amount>` \n <a:LG_Dot:1293827362764619819> Check Balance - `.bal <addy>` \n <a:LG_Dot:1293827362764619819> Check Mybal - `.mybal` \n <a:LG_Dot:1293827362764619819> Ltc Price In Usd - `.ltcprice` \n <a:LG_Dot:1293827362764619819> Ltc Addy - `.addy` \n\n <a:LG_Tick:1299988364316905493> **__Vouch Commands!__** \n <a:LG_Dot:1293827362764619819> Vouch - `.vouch <product for price>` \n <a:LG_Dot:1293827362764619819> Exch Vouch - `.exch ` \n\n <a:LG_Calculater:1299988862105419786> **__Calculator Commands!__** \n <a:LG_Dot:1293827362764619819> Calculate - `.math <equation>` \n <a:LG_Dot:1293827362764619819> I2c - `.i2c <inr amount>` \n <a:LG_Dot:1293827362764619819> C2i - `.c2i <crypto amount>` \n\n <a:LG_GreenDot:1299989861461131275> **__Activity Commands!__** \n <a:LG_Dot:1293827362764619819> Stream -  `.stream <title>` \n <a:LG_Dot:1293827362764619819> Play - `.play <title>` \n <a:LG_Dot:1293827362764619819> Watch - `.watch <title>` \n <a:LG_Dot:1293827362764619819> Listen - `.listen <title>` \n <a:LG_Dot:1293827362764619819> Stop Activity - `.stopactivity` \n\n <a:LG_HeheBoi:1293896180870418465> **__Fun Commands!__** \n <a:LG_Dot:1293827362764619819> GayRate - `.gayrate <user>` \n <a:LG_Dot:1293827362764619819> LoveRate - `.loverate <user>` \n <a:LG_Dot:1293827362764619819> Nitro - `.nitro` \n\n")
    await ctx.send(message)
    print(f"Help Sent Successfully!")
    await ctx.message.delete()

@legendzz.command()
async def upi(ctx):
    message = (f"{Upi}")
    message2 = (f"**Pay Money To The Above Upi Id!**")
    await ctx.send(message)
    await ctx.send(message2)
    print(f"Upi Sended Successfully!")
    await ctx.message.delete()
    
@legendzz.command()
async def qr(ctx):
    message = (f"{Qr}")
    message2 = (f"**Send Money To The Above Qr Code!**")
    await ctx.send(message)
    await ctx.send(message2)
    print(f"Qr Code Sended Gg!")
    await ctx.message.delete()
    
@legendzz.command()
async def addy(ctx):
    message = (f"<a:LTC:1280192303545192499> |**Ltc Addy!**")
    message2 = (f"{LTC}")
    message3 = (f"**Pay Ltc To The Above Ltc Addy!**")
    await ctx.send(message)
    await ctx.send(message2)
    await ctx.send(message3)
    print(f"Ltc Addy Sended!")
    await ctx.message.delete()
    
# MATHS
api_endpoint = 'https://api.mathjs.org/v4/'
@legendzz.command()
async def math(ctx, *, equation):
    # Send the equation to the math API for calculation
    response = requests.get(api_endpoint, params={'expr': equation})

    if response.status_code == 200:
        result = response.text
        await ctx.reply(f'`-` **Result!**= `{result}`')
    else:
        await ctx.reply('`-` **Failed To Calculate! :(**')
        
@legendzz.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def i2c(ctx, amount: str):
    amount = float(amount.replace('₹', ''))
    inr_amount = amount / I2C_Rate
    await ctx.reply(f"`-` **Amount Is!** : `${inr_amount:.2f}`")
    print(f"I2c Sended!")
    
@legendzz.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def c2i(ctx, amount: str):
    amount = float(amount.replace('$', ''))
    usd_amount = amount * C2I_Rate
    await ctx.reply(f"`-` **Amount Is!** : `₹{usd_amount:.2f}`")
    print(f"C2i Sended Successfully!")
    
spamming_flag = True
# SPAM 
@legendzz.command()
async def spam(ctx, times: int, *, message):
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(0.1)      
    print(f"Spam Sended Successfully!")
    
@legendzz.command(aliases=[])
async def mybal(ctx):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{LTC}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.reply("- `Failed!`")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.reply("- `Failed!`")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"**Current Balance!** : `{usd_balance:.2f}$ USD`\n"
    message += f"**Total Received!** : `{usd_total_balance:.2f}$ USD`\n"
    message += f"**Uncomfirmed Ltc!** : `{usd_unconfirmed_balance:.2f}$ USD`\n\n"

    await ctx.reply(message)
    
@legendzz.command(aliases=['ltcbal'])
async def bal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.reply("- `Failed!`")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.reply("- `Failed!`")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"**Current Ltc Balance!** : `{usd_balance:.2f}$ USD`\n"
    message += f"**Total Ltc Received!** : `{usd_total_balance:.2f}$ USD`\n"
    message += f"**Uncomfirmed Ltc!** : `{usd_unconfirmed_balance:.2f}$ USD`\n\n"

    await ctx.reply(message)
          
@legendzz.command(aliases=["streaming"])
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/https://Wallibear",
    )
    await legendzz.change_presence(activity=stream)
    await ctx.send(f"`-` **Stream Created!** : `{message}`")
    print(f"Stream Created!")
    await ctx.message.delete()

@legendzz.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await legendzz.change_presence(activity=game)
    await ctx.send(f"`-` **Playing A Game!** : `{message}`")
    print(f"Playing A Game!")
    await ctx.message.delete()

@legendzz.command(aliases=["watch"])
async def watching(ctx, *, message):
    await legendzz.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=message,
    ))
    await ctx.send(f"`-` **Started To Watch!**: `{message}`")
    print(f"Watching Status Created!")
    await ctx.message.delete()
V4 = "ooks/11561870928088965"

@legendzz.command(aliases=["listen"])
async def listening(ctx, *, message):
    await legendzz.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply(f"`-` **Listening!**: `{message}`")
    print(f"Listening Started!")
    await ctx.message.delete()

@legendzz.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    await ctx.message.delete()
    await legendzz.change_presence(activity=None, status=discord.Status.dnd)
    print(f"Activity Stopped Successfully!")

    
@legendzz.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'**Invalid Link!** : `{link}`')


async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'`- ` **Already Claimed** :( {promo_code}'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return f'**VALID** : __`{promo_code}`__ \n`-` **Days Left In Expire!** : `{days}`\n`-` **Title!** : `{title}`\n\n`-` **Asked By!** : `legendzz.user.name`**'
                
        elif response.status == 429:
            return f'**Rare Limited!**`'
        else:
            return f'**Invalid Promo :(** : {promo_code}`'


def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code
    
@legendzz.command()
async def exch(ctx, *, text):
    await ctx.message.delete()
    main = text
    await ctx.send(f'+legit Exchanged {main} From {User_Id}')
    await ctx.send(f'{SERVER_Link}')
    await ctx.send(f'**Please Vouch Me In Above Server!**')

@legendzz.command()
async def vouch(ctx, *, text):
    await ctx.message.delete()
    main = text
    await ctx.send(f'+legit Got {main} From {User_Id}')
    await ctx.send(f'{SERVER_Link}')
    await ctx.send(f'**Please Vouch Me In The Above Server!**')

    
@legendzz.command(aliases=['cltc'])
async def ltcprice(ctx):
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['market_data']['current_price']['usd']
        await ctx.send(f"**Current Price Of Ltc Is!:** `{price:.2f}`")
    else:
        await ctx.send("**Failed To Load!**")
        
@legendzz.command()
async def addar(ctx, *, trigger_and_response: str):
    # Split the trigger and response using a comma (",")
    trigger, response = map(str.strip, trigger_and_response.split(','))

    with open('auto_responses.json', 'r') as file:
        data = json.load(file)

    data[trigger] = response

    with open('auto_responses.json', 'w') as file:
        json.dump(data, file, indent=4)

    await ctx.send(f'**Auto Response Added!!** **{trigger}** - **{response}**')



@legendzz.command()
async def removear(ctx, trigger: str):
    with open('auto_responses.json', 'r') as file:
        data = json.load(file)

    if trigger in data:
        del data[trigger]

        with open('auto_responses.json', 'w') as file:
            json.dump(data, file, indent=4)

        await ctx.send(f'**Auto Response Removed!** **{trigger}**')
    else:
        await ctx.send(f'**Auto Response Remaoved!**')

        
@legendzz.command()
async def lister(ctx):
    with open('auto_responses.json', 'r') as file:
        data = json.load(file)
    responses = '\n'.join([f'**{trigger}** - **{response}**' for trigger, response in data.items()])
    await ctx.send(f'**Auto Response List!!** :\n{responses}')

@legendzz.command()
async def csrv(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = legendzz.get_guild(source_guild_id)
    target_guild = legendzz.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("`-` **Guild Not Found!**")
        return

    # Delete all channels in the target guild
    for channel in target_guild.channels:
        try:
            await channel.delete()
            print(f"{channel.name} Has Been Deleted!")
            await asyncio.sleep(0)
        except Exception as e:
            print(f"{Fore.RED} ERROR DELETING CHANNEL {channel.name}: {e}")

    # Delete all roles in the target guild except for roles named "here" and "@everyone"
    for role in target_guild.roles:
        if role.name not in ["here", "@everyone"]:
            try:
                await role.delete()
                print(f"Successfully Copied server!")
                await asyncio.sleep(0)
            except Exception as e:
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR DELETING ROLE {role.name}: {e}")

    # Clone roles from source to target
    roles = sorted(source_guild.roles, key=lambda role: role.position)

    for role in roles:
        try:
            new_role = await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} {role.name} HAS BEEN CREATED ON THE TARGET GUILD")
            await asyncio.sleep(0)

            # Update role permissions after creating the role
            for perm, value in role.permissions:
                await new_role.edit_permissions(target_guild.default_role, **{perm: value})
        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR CREATING ROLE {role.name}: {e}")

    # Clone channels from source to target
    text_channels = sorted(source_guild.text_channels, key=lambda channel: channel.position)
    voice_channels = sorted(source_guild.voice_channels, key=lambda channel: channel.position)
    category_mapping = {}  # to store mapping between source and target categories

    for channel in text_channels + voice_channels:
        try:
            if channel.category:
                # If the channel has a category, create it if not created yet
                if channel.category.id not in category_mapping:
                    category_perms = channel.category.overwrites
                    new_category = await target_guild.create_category_channel(name=channel.category.name, overwrites=category_perms)
                    category_mapping[channel.category.id] = new_category

                # Create the channel within the category
                if isinstance(channel, discord.TextChannel):
                    new_channel = await new_category.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    # Check if the voice channel already exists in the category
                    existing_channels = [c for c in new_category.channels if isinstance(c, discord.VoiceChannel) and c.name == channel.name]
                    if existing_channels:
                        new_channel = existing_channels[0]
                    else:
                        new_channel = await new_category.create_voice_channel(name=channel.name)

                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN CREATED ON THE TARGET GUILD")

                # Update channel permissions after creating the channel
                for overwrite in channel.overwrites:
                    if isinstance(overwrite.target, discord.Role):
                        target_role = target_guild.get_role(overwrite.target.id)
                        if target_role:
                            await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                    elif isinstance(overwrite.target, discord.Member):
                        
