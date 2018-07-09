import requests
from bs4 import BeautifulSoup
import weather

req = requests.get('https://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT001009')

soup= BeautifulSoup(req.text, 'html.parser');
soup.select("div[style$=flex]")

today_am_weather = soup.select_one('#content > table.tbl_weather.tbl_today3')

#print(today_am_weather);

rain_data=[]
for tr in today_am_weather.find_all('tr'):
    tds = list(tr.find_all('td'))
    
    for td in tds:
        if td.find('strong'):
            point = td.find('strong').text
            rain_data.append(point)
            
#print(rain_data)

print('\n===================================\n')

pm_rain=rain_data.pop()
pm_rain=int(pm_rain.split('%')[0])
print('오전 강수확률 :', pm_rain,'%')

am_rain=rain_data.pop(0)
am_rain=int(am_rain.split('%')[0])
print('오후 강수확률 :',am_rain,'%')

if am_rain > 50:
    print("우산을 챙기세요~ 오전에 비 올 확률이 50%가 넘어요!")
elif pm_rain > 50:
    print("우산을 챙기세요~ 오후에 비 올 확률이 50%가 넘어요!")
else:
    print("비가 안 올 확률이 더 커요!")