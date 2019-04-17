from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
html = urlopen("http://www.gsm.hs.kr/xboard/board.php?tbnum=8").read().decode("utf-8")
soup = bs(html, "html.parser")
cal = soup.select("#xb_fm_list > div.calendar > ul > li.today > div > div > div > div > span.content")
foodlist=[]
for eat in cal:
    eat = eat.text.split("\n")
    eat_tmp = []
    for e in eat:
        e=e.strip().split()[0]
        eat_tmp.append(e)
    del eat_tmp[eat_tmp.index("*"):]
    foodlist.append(eat_tmp)
    for f in foodlist:
        for ff in f:
            print(ff)
#print(foodlist[0])
