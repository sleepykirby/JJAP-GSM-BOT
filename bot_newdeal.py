import asyncio
import discord
from discord import File
from discord.ext import commands
from datetime import datetime, timedelta
import secrets
import sqlite3
import bot_2048



bot=commands.Bot(command_prefix="!")
bot.remove_command('help')
token_file=open('../token.txt','r')
BOT_TOKEN = token_file.read()
if(BOT_TOKEN):
    print('token read')
    #token 변경 완료

#변수 목록
요일=['월','화','수','목','금','토','일']
board=[]

#봇 커맨드
@bot.event
async def on_ready():
    print("Client Logged in")
    
    await bot.change_presence(activity=discord.Game("명령어 : !help"),status=discord.Status.online,afk=False)


@bot.command(pass_context=True)
async def 급식(ctx):#냠냠
    
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
        tws=tomorrow.strftime('%A')
        if(tws=='Sunday'):
            tw=6
        elif(tws=='Monday'):
            tw=0
        elif(tws=='Tuesday'):
            tw=1
        elif(tws=='Wednesday'):
            tw=2
        elif(tws=='Thursday'):
            tw=3
        elif(tws=='Friday'):
            tw=4
        elif(tws=='Saturday'):
            tw=5
        
        날짜=str(int(tomorrow.strftime('%d')))+"("+요일[tw]+")"
        시간='아침'
    print(날짜)
    dbn='foodtable-'
    dbn+=str(now.year)+'-'+str(now.month)
    dbn+='.db'
    conn = sqlite3.connect(dbn)
    cur = conn.cursor()
    sql="SELECT foods FROM ft WHERE date=\'%s\' AND time=\'%s\'"%(날짜,시간)#sql문 생성
    print(sql)
    cur.execute(sql)
    rlt=cur.fetchone()
    rltlist=rlt[0].split(' ')
    print(rltlist)
    급식날짜=str(now.year)+"년 "+str(now.month)+"월 "+날짜+" "+시간+" 식단표"#embed 박스 제목
    급식목록=''#embed 박스 내용 
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
async def 소라고둥(ctx,*args):#마법의 소라고둥은 모든 것을 알아요
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

@bot.command(pass_context=True)
async def 샌즈(ctx):#와!!
    f=File('./img/WA.png','WA.png')
    await ctx.send(file=f)



@bot.command(pass_context=True)
async def _2048(ctx,arg):#갓겜
    if arg=='gg':#리셋
        board=bot_2048.newBoard()
    elif arg=='w':#위
        bot_2048.pressW(board)
        e=discord.Embed(title='짭 GSM 봇 2048')
    elif arg=='a':#왼쪽
        bot_2048.pressA(board)
    elif arg=='s':#아래
        bot_2048.pressS(board)
    elif arg=='d':#오른쪽
        bot_2048.pressD(board)
    

@bot.command(pass_context=True)
async def 김동(ctx):
    await ctx.send("국")

@bot.command(pass_context=True)
async def 깃헙(ctx):
    await ctx.send('https://github.com/limeslime/JJAP-GSM-BOT/tree/add_newdeal.py')

# @bot.command(pass_context=True)
# async def 짹짹(ctx):
#     await ctx.send('https://twitter.com/k3id_moung')

@bot.command(pass_context=True)
async def help(ctx):#명령어 목록 출력
    msg=''
    msg+='- !급식\n'
    msg+='- !소라고둥\n'
    msg+='- !김동\n'
    msg+='- !샌즈\n'
    msg+='- !_2048\n'
    msg+='- !깃헙\n'
    #msg+='- !짹짹\n'
    e=discord.Embed(title='JJAP GSM BOT 명령어 목록',description=msg,colour=12777215)
    await ctx.send(embed=e)

bot.run(BOT_TOKEN)