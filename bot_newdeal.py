import asyncio
import discord
from discord import File
from discord.ext import commands
from datetime import datetime, timedelta
import secrets
import sqlite3
import bot_2048
import foodCrawler



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
async def 급식(ctx,*args):#냠냠
    if(len(args)==0):
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
    elif(args[0]=='DB'):
        foodCrawler.run()

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
async def help(ctx,*args):#명령어 목록 출력
    if(len(args)==0):
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
    elif(len(args)==1):
        if(args[0]=='급식'):
            제목='!급식'
            내용='!급식 DB : 매달 한 번씩 한 달 분량 급식 다운로드'
        elif(args[0]=='김동'):
            제목='!김동'
            내용='국'
        elif(args[0]=='샌즈'):
            제목='!샌즈'
            내용='와 샌즈! 파피루스! 언더테일!'
        elif(args[0]=='소라고둥'):
            제목='!소라고둥'
            내용='질문-답변 서비스, 현재 개발중'
        elif(args[0]=='깃헙'):
            제목='!깃헙'
            내용='짭 GSM 봇 개발 Github 주소 제공'
        elif(args[0]=='_2048'):
            제목='!_2048'
            내용='재밌고 신나는 2048 게임을 디코 봇으로!, 현재 개발중'
        e=discord.Embed(title=제목,description=내용)
        await ctx.send(embed=e)



bot.run(BOT_TOKEN)