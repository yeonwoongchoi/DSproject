##openweather에서 실시간 온도 값 받아서 보여주기
##https://m.blog.naver.com/wideeyed/221335980042참조
prov_list = [
    {'name':'Seoul','city_id':'1835847'},
    {'name':'Busan','city_id':'1838524'},
    {'name':'Daegu','city_id':'1835329'},
    {'name':'Incheon','city_id':'1843564'},
]
def converte_kelvin_to_celsius(k):
    return (k-273.15)
import requests
from time import sleep
url = 'http://api.openweathermap.org/data/2.5/weather'

weather_info_list = []
for i in range(len(prov_list)):
    city_id = prov_list[i]['city_id']
    city_name = prov_list[i]['name']
    print(city_name)
    params = dict(
    id = city_id,
    APPID = '3d982f4de1b989d164dec06f824f2348',)
    sleep(1)
    resp = requests.get(url=url, params = params)
    data = resp.json()
    if(data['cod'] == 429):
        break
    
    data_main = data['main']
    info = [city_id, city_name, converte_kelvin_to_celsius(data_main['temp_min']), converte_kelvin_to_celsius(data_main['temp']), converte_kelvin_to_celsius(data_main['temp_max']), data_main['pressure'], data_main['humidity']]
    weather_info_list.append(info)


import pandas as pd
df = pd.DataFrame(weather_info_list, columns = ['city-id', 'city_name', 'temp_min', 'temp', 'temp_max', 'pressure', 'humidity'])
print(df)
