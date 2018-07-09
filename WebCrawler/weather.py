import requests
from bs4 import BeautifulSoup

req = requests.get('https://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT001009')

soup= BeautifulSoup(req.text, 'html.parser');
soup.select("div[style$=flex]")

today_am_weather = soup.select_one('#content > table.tbl_weather.tbl_today3')

#print(today_am_weather);

today_data=[]
for tr in today_am_weather.find_all('tr'):
    tds = list(tr.find_all('td'))
    
    for td in tds:
        if td.find('span'):
            point = td.find('span').text
            today_data.append(point)
            
#print(data)
high_temp=today_data.pop()
high_temp=int(high_temp.split('.')[0])
print('최고 기온 :',high_temp)

low_temp=today_data.pop(0)
low_temp=int(low_temp.split('.')[0])
print('최저 기온 :',low_temp)

if high_temp > 27:
    print("날씨가 매우 더우니 반팔,반바지를 입으세요.")
elif 23< high_temp<26:
    print("반팔에 면바지 혹은 얇은 긴팔을 입으세요.")
elif 20 < high_temp < 22:
    print('얇은 가디건을 챙겨주세요.')
elif 17 < high_temp < 19:
    print('얇은 니트, 후드티가 적당합니다.')
elif 12 < high_temp < 16:
    print('자켓,야상,가디건이 필요한 날씨입니다.')
elif 10 < high_temp < 11:
    print('트렌치코트를 입거나, 여러겹을 껴입어야하는 날씨입니다.')
elif 6 < high_temp < 9:
    print('히트텍을 입어주시고, 코트도 입어야합니다.')
else:
    print('매우 추우니 무조건 겨울 옷을 입으세요.')
