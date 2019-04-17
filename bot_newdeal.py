import asyncio
import discord
from discord.ext import commands
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import secrets

bot=commands.Bot(command_prefix="!")

BOT_TOKEN = "NTU4MTEzMzQ5NDczNDAyODgz.XKvVqQ.zpxrsvOYSzvoMShFSv49Ya92QU4"

@bot.event
async def on_read():
    print("Client Logged in")

@bot.command(pass_context=True)
async def hello(ctx):
    print(discord.User.display_name)
    return await ctx.send("Hello World!")

@bot.command(pass_context=True)
async def 급식(ctx):
    print(discord.User.display_name)
    html = urlopen("http://www.gsm.hs.kr/xboard/board.php?tbnum=8").read().decode("utf-8")
    soup = bs(html, "html.parser")
    cal = soup.select("#xb_fm_list > div.calendar > ul > li.today > div > div > div > div > span.content")
    foodlist=[]
    for eat in cal:
        eat = eat.text.split("\n")
        eat_tmp = []
        for e in eat:
            e=e.strip().split()[0].strip("/")
            eat_tmp.append(e)
        if eat_tmp.count("*") > 0:
            del eat_tmp[eat_tmp.index("*"):]
        foodlist.append(eat_tmp)
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
        elif(args[1]=='del'):
            #삭제
    elif(len(args)==1):
        if(args[1]=="help"|args[1]=="?"):
            await ctx.send("")

bot.run(BOT_TOKEN)