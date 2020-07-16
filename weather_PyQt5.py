import sys
import requests
from functools import partial
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def get_weather(choice):
    s_city = choice
    appid = 'a5c5f26e7e133daa411606be2347d43c'
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/find',
        params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid}
    )
    data = response.json()
    cities = [f"{d['name']} ({d['sys']['country']})" for d in data['list']]
    city_id = data['list'][0]['id']
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    info = (f"{cities[0]}\nСечас на улице " + str(data['weather'][0]['description']) +
            "\nТемпература воздуха: " + str(data['main']['temp']) + '\n')
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    date = None
    for i in data['list']:
        if i['dt_txt'][0:10] != date:
            info += '\n'
            info += (i['dt_txt'][:10])
        else:
            pass
        info += ('\n' + i['dt_txt'][10:16] + ' {0:+3.0f} '.format(i['main']['temp']) + i['weather'][0]['description'])
        date = i['dt_txt'][:10]
    if msg.text():
        msg.setText("")
    else:
        msg.setText(info)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Weather')
layout = QVBoxLayout()

btn = QPushButton('KYIV')
btn.clicked.connect(partial(get_weather, 'kyiv'))

btn1 = QPushButton('ODESSA')
btn1.clicked.connect(partial(get_weather, 'odessa'))

btn2 = QPushButton('KHARKIV')
btn2.clicked.connect(partial(get_weather, 'kharkiv'))

btn3 = QPushButton('LVIV')
btn3.clicked.connect(partial(get_weather, 'lviv'))

btn4 = QPushButton('DONETSK')
btn4.clicked.connect(partial(get_weather, 'donetsk'))

btn5 = QPushButton('ZHYTOMYR')
btn5.clicked.connect(partial(get_weather, 'zhytomyr'))

btn6 = QPushButton('RIVNE')
btn6.clicked.connect(partial(get_weather, 'rivne'))


layout.addWidget(btn)
layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)
layout.addWidget(btn4)
layout.addWidget(btn5)
layout.addWidget(btn6)

msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())