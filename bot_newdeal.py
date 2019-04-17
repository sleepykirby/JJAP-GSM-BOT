import asyncio
import discord
from discord.ext import commands
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import secrets

bot=commands.Bot(command_prefix="!")

BOT_TOKEN = "NTU4MTEzMzQ5NDczNDAyODgz.XKvVqQ.zpxrsvOYSzvoMShFSv49Ya92QU4"

#변수 목록



#봇 커맨드
@bot.event
async def on_read():
    print("Client Logged in")

@bot.command(pass_context=True)
async def hello(ctx):
    print(discord.User.display_name)
    return await ctx.send("Hello World!")

@bot.command(pass_context=True)
async def 급식(ctx):
    
    now=datetime.now()


@bot.command(pass_context=True)
async def test(ctx,*args):#args는 !명령어 args[0] args[1] args[2] ... 순
    if(len(args)==1):
        await ctx.send(args[0])
    elif(len(args)==3):
        await ctx.send(args[0]+" "+args[2])
    else:
        for l in args:
            await ctx.send(l)
            pass

@bot.command(pass_context=True)
async def 소라고둥(ctx,*args):
    if(len(args)>=2):
        if(args[1]=='add'):
            #추가
            a=0
        elif(args[1]=='del'):
            #삭제
            b=0
    elif(len(args)==1):
        if(args[1]=="help"|args[1]=="?"):
            await ctx.send("")

bot.run(BOT_TOKEN)