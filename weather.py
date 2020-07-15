import requests

choose_dict = {
    '1': 'kyiv, UA',
    '2': 'odessa, UA',
    '3': 'kharkiv, UA',
    '4': 'lviv, UA',
    '5': 'donetsk, UA',
    '6': 'zhytomyr, UA',
    '7': 'rivne, UA'
}
choose_list = ('''
    1. Киев
    2. Одесса
    3. Харьков
    4. Львов
    5. Донецк
    6. Житомир
    7. Ровно
''')
print(choose_list, '\n')
user_input = input('Выбери город из списка: ')
s_city = choose_dict[user_input]
city_id = 0
appid = 'a5c5f26e7e133daa411606be2347d43c'
try:
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/find',
        params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid}
    )
    data = response.json()
    cities = [f"{d['name']} ({d['sys']['country']})" for d in data['list']]
    print("city: ", cities[0])
    city_id = data['list'][0]['id']
    #print('city_id=', city_id)
except Exception as e:
    print("Exception (find): ", e)
    pass

print()

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Сечас на улице", data['weather'][0]['description'])
    print("Температура воздуха:", data['main']['temp'])
except Exception as e:
    print("Exception (weather):", e)
    pass

print('\nЖелаешь посмотреть прогноз погоды на ближайшие несколько дней?')
next_step = input('''
    1. Да
    2. Нет
''')

if next_step == '1':
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        date = None
        for i in data['list']:
            if i['dt_txt'][0:10] != date:
                print()
                print(i['dt_txt'][:10])
            else: pass
            print(i['dt_txt'][10:15], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
            date = i['dt_txt'][:10]
    except Exception as e:
        print("Exception (forecast):", e)
        pass
else: print("До встречи!")


#a5c5f26e7e133daa411606be2347d43c
#response = requests.get('http://api.openweathermap.org/data/2.5/find?q=Zhytomyr,UA&type=like&APPID=a5c5f26e7e133daa411606be2347d43c')