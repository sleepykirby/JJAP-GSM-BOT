import asyncio
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import secrets
import sqlite3


bot=commands.Bot(command_prefix="!")

BOT_TOKEN = "NTU4MTEzMzQ5NDczNDAyODgz.XKvVqQ.zpxrsvOYSzvoMShFSv49Ya92QU4"

#변수 목록
요일=['월','화','수','목','금','토','일']

#봇 커맨드
@bot.event
async def on_ready():
    print("Client Logged in")
    await bot.change_presence(activity=discord.Game("!help"),status=discord.Status.idle,afk=False)


@bot.command(pass_context=True)
async def 급식(ctx):
    
    now=datetime.now()
    tomorrow=now+timedelta(days=1)
    날짜=str(now.day)+"("+요일[now.weekday()]+")"
    if((now.hour*60+now.minute)<480):#아침
        시간='아침'
    elif((now.hour*60+now.minute)<810):#점심
        시간='점심'
    elif((now.hour*60+now.minute)<1110):#저녁
        시간='저녁'
    else:
        날짜=str(tomorrow.day)+"("+요일[tomorrow.weekday]+")"
        시간='아침'
    print(날짜)
    conn = sqlite3.connect('foodtable.db')
    cur = conn.cursor()
    sql="SELECT foods FROM ft WHERE date=\'%s\' AND time=\'%s\'"%(날짜,시간)
    print(sql)
    cur.execute(sql)
    rlt=cur.fetchone()
    rltlist=rlt[0].split(' ')
    print(rltlist)
    # msg=''
    # for r in rlt:
    #     msg+=r
    #     msg+='\n'
    # await ctx.send(msg)
    급식날짜=str(now.year)+"년 "+str(now.month)+"월 "+날짜+" 식단표"
    급식목록=''
    for r in rltlist:
        급식목록+='- '+r+'\n'
    e=discord.Embed(title=급식날짜,description=급식목록,colour=12777215)
    await ctx.send(embed=e)
    conn.close()

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

# @bot.command(pass_context=True)
# async def WA(ctx):
#     file
#     await ctx.send(file=)

bot.run(BOT_TOKEN)