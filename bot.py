import asyncio
import discord
from discord.ext import commands
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup

client = discord.Client()
driver=webdriver.Chrome('D:/Drivers')
driver.implicitly_wait(3)


# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NTU4MTEzMzQ5NDczNDAyODgz.D3Xckg.1mZzNmfdoYk-W0JbXKpM3JESruc"

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
    await client.change_presence(activity=discord.Game("게임 안"),status=discord.Status.idle,afk=True)

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!커맨드'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        #await client.send_message(channel, '커맨드') #봇은 해당 채널에 '커맨드' 라고 말합니다.
        await message.channel.send('!클리어')
    elif message.content.startswith('!클리어'):
        await client.clear()
    elif message.content.startswith('!급식'):
        driver.get('http://www.gsm.hs.kr/xboard/board.php?tbnum=8')
        if(now.hour<=8):
            #아침식사
            driver.find_element_by_class_name("today ").find_element_by_class_name("food_list_box").find_element_by_class_name("slider_food_list slider_food25 cycle-slideshow").find_element
        elif(now.hour<=12):
            #점심식사
        else:
            #저녁식사

    elif message.content.startswith('!김동')
        await message.channel.send('국')
        #웹크롤링 급식
    #else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        #await message.channel.send('누물보')


client.run(token)