import asyncio
import discord
from discord.ext import commands
from datetime import datetime
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

client = discord.Client()


# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NTU4MTEzMzQ5NDczNDAyODgz.XKvVqQ.zpxrsvOYSzvoMShFSv49Ya92QU4"




# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    #await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))
    await client.change_presence(activity=discord.Game("!커맨드"),status=discord.Status.idle,afk=False)

conch='none'
dap=['예','아니오']
# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!커맨드'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        #await client.send_message(channel, '커맨드') #봇은 해당 채널에 '커맨드' 라고 말합니다.
        await message.channel.send('!gsm'+'\n!급식'+'\n!김동'+'\n!소라고둥')
    elif message.content.startswith('!gsm'):
        await message.channel.send('http://www.gsm.hs.kr')
    elif message.content.startswith('!급식'):
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
        #print(foodlist)
        now=datetime.now()
        if(now.hour<=8):
            #아침식사
            msg=''
            for f in foodlist[0]:
                msg+=f
                msg+='\n'
            await message.channel.send(str(now.month)+'/'+str(now.day)+' 아침 식사 : ')
            await message.channel.send(msg)
        elif(now.hour<=12):
            #점심식사
            msg=''
            for f in foodlist[1]:
                msg+=f
                msg+='\n'
            await message.channel.send(str(now.month)+'/'+str(now.day)+' 점심 식사 : ')
            await message.channel.send(msg)
        elif(now.hour<=19):
            #저녁식사
            msg=''
            for f in foodlist[2]:
                msg+=f
                msg+='\n'
            await message.channel.send(str(now.month)+'/'+str(now.day)+' 저녁 식사 : ')
            await message.channel.send(msg)
        else:
            #다시 아침식사
            msg=''
            for f in foodlist[0]:
                msg+=f
                msg+='\n'
            await message.channel.send(str(now.month)+'/'+str(now.day)+' 아침 식사 : ')
            await message.channel.send(msg)
            
        
    elif message.content.startswith('!김동'):
        await message.channel.send('국')
    elif message.content.startswith('!동국'):
        await message.channel.send('!김동국#4726')
    elif message.content.startswith('!소라고둥'):
        await message.channel.send('소라고둥 명령어 : \n!s답변목록\n!s답변추가\n!s답변삭제\n!s질문')
    elif message.content.startswith('!s답변목록'):
        msg=''
        for d in dap:
            msg+=d
            msg+='\n'
        await message.channel.send(msg)
    elif message.content.startswith('!s답변추가'):
        conch='add'
        await message.channel.send('답변을 추가합니다 '+conch)
    elif message.content.startswith('!s답변삭제'):
        conch='del'
        await message.channel.send('답변을 삭제합니다 '+conch)
    elif message.content.startswith('!s질문'):
        conch='q'
        await message.channel.send('질문을 받습니다 '+conch)
    else: #위의 if에 해당되지 않는 경우
        if conch=='add':
            dap.append(message.content[:])
            
        elif conch=='del':
            try:
                dap.remove(message.content)
            except:
                message.channel.send('!s답변목록 을 통해 확인해 주세요')
                pass
        conch='none'
client.run(token)
