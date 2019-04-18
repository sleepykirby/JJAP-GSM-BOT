from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.parse
from datetime import datetime

# # 우리학교 급식 사이트 받아오기
RSS = "http://www.gsm.hs.kr/xboard/board.php"
values = {"tbnum" : "8"}
query = urllib.parse.urlencode(values)
url = RSS+ "?"+query
html = urlopen(url).read().decode("utf-8")
soup = bs(html, "html.parser")

# # 오늘의 급식표 받아오기
cal=soup.find("div", class_="calendar").find("li", class_="today").find_all("span", class_="content")
foodlist = []
for eat in cal:
    eat = eat.text.split("\n")
    eat_tmp = []
    for e in eat:
        e=e.strip().split()[0].strip("/")
        eat_tmp.append(e)
    if eat_tmp.count("*") > 0:
        del eat_tmp[eat_tmp.index("*"):]
    foodlist.append(eat_tmp)

# # 오늘의 급식표 출력
foodtime = ['아침', '점심', '저녁']
for foodt, foodli in zip(foodtime, foodlist):
    print(foodt)
    for food in foodli:
        print(food)
    print()

# # 이번 달 급식표 받아오기
cal=soup.find("div", class_="calendar").find_all("span", class_="content")
foodlist = []
for eat in cal:
    eat = eat.text.split("\n")
    eat_tmp = []
    for e in eat:
        e=e.strip().split()[0].strip("/")
        eat_tmp.append(e)
    if eat_tmp.count("*") > 0:
        del eat_tmp[eat_tmp.index("*"):]
    foodlist.append(eat_tmp)

# # 이번 달 급식표 날짜와 음식 둘 다 가져오기
table=soup.select("#xb_fm_list > div.calendar > ul > li > div")
tablelist=[]
for t in table:
    t_tmp = []
    for t_item in t:
        if t_item != "\n":
            t_split=t_item.text.strip().split("\n\n\n\n\n\n")
            if len(t_split)==1 and len(t_split[0])>0:
                t_tmp.append(t_split[0])
            elif len(t_split)>1:
                t_tmp.append(t_split)
            else:
                continue
    tablelist.append(t_tmp)

for day in range(len(tablelist)):
    if len(tablelist[day])<=1:
        continue
    for eats in range(len(tablelist[day][1])):
        tablelist[day].append(tablelist[day][1][eats].split("\n"))
    del tablelist[day][1]
    for eats in range(1,len(tablelist[day])):
        for foods in range(len(tablelist[day][eats])):
            tablelist[day][eats][foods]=tablelist[day][eats][foods].strip().split()
            if len(tablelist[day][eats][foods])>0:
                tablelist[day][eats][foods]=tablelist[day][eats][foods][0].strip("/")
        if tablelist[day][eats].count("*") > 0:
            del tablelist[day][eats][tablelist[day][eats].index("*"):]

# # DB 저장
now=datetime.now()
# dbn='foodtable-'
# dbn+=str(now.year)+'-'+str(now.month)
# dbn+='.db'

import sqlite3
conn = sqlite3.connect('./foodtable'+'-'+str(now.year)+'-'+str(now.month)+'.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS ft')
cur.execute('CREATE TABLE ft (date text, time text, foods text)')

for day in range(len(tablelist)):
    time = ['아침', '점심','저녁']
    for i in range(len(time)):
        if i>=len(tablelist[day])-1 or len(tablelist[day][i+1]) <= 0:
            cur.execute('INSERT INTO ft values(?,?,?)', (tablelist[day][0], time[i], "없음"))
        else:
            cur.execute('INSERT INTO ft values(?,?,?)', (tablelist[day][0], time[i], " ".join(tablelist[day][i+1])))

cur.execute('SELECT * FROM ft')
rlt = cur.fetchall()

for r in rlt:
    print("날짜 : %s, 시간: %s, 메뉴: %s"% r)
    
conn.commit()
conn.close()
