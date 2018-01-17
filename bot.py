# Tutbot by Da532

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def HalifaxProblem(ctx):
    await bot.say(":information_source: __**1. Q: Why isn't Halifax injecting?**__ `A: If Halifax isn't injecting, Please download: https://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x86.exe https://download.microsoft.com/download/0/6/4/064F84EA-D1DB-4EAA-9A5C-CC2F0FF6A638/vc_redist.x86.exe and https://go.microsoft.com/fwlink/?LinkId=746571 then restart your computer`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           __**2. Q: Why it's saying it's already injected?**__ `A: It is because: 1. It's running in your background. Go to Task Manager and End Task Halifax.`")
    print ("user has information")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

bot.run("NDAzMDY4OTEwODQ2MzQ1MjE3.DUFDLQ.JtSL98QmQvZiTYE32ieT0ZSM5pc")
