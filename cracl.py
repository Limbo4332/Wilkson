import requests
import time
import json

keys = ['number', 'scheme', 'type', 'brand', 'prepaid', 'country', 'bank']
keys_rus = ['Номер карты', 'Платежная система', 'Тип карты', 'Региональная платежная система', 'Предоплачена', 'Страна',
            'Банк']

data_country = ['numeric', 'alpha2', 'name', 'emoji', 'currency', 'latitude', 'longitude']
data_country_rus = ['Id страны', 'Буквенный id страны', 'Название страны', 'Символ страны', 'Валюта карты', 'Широта',
                    'Долгота']

bank_keys = ['name', 'url', 'phone']
bank_rus = ['Название банка', 'Ссылка на банк', 'Тех. поддержка']

cardcode = input('Введите номер карты: ')
cardcode1 = cardcode.replace(' ', '')
cardcode_use = cardcode1[0:8]

url = f'https://lookup.binlist.net/{cardcode_use}'

response = requests.get(url)
print('Подключение...')
time.sleep(0.5)

if response.status_code == 200:
    print('Успешно...')
    print()
    time.sleep(0.5)
    data = response.json()

    for i in keys:
        if i in data:
            if i == 'country' and isinstance(data['country'], dict):
                print()
                print('Информация о стране:')
                for c in data_country:
                    if c in data['country']:
                        index2 = data_country.index(c)
                        print(f'\t{data_country_rus[index2]}: {data["country"][c]}')

            elif i == 'bank' and isinstance(data['bank'], dict):
                print()
                print('Информация о банке:')
                for b in bank_keys:
                    if b in data['bank']:
                        index3 = bank_keys.index(b)
                        print(f'\t{bank_rus[index3]}: {data["bank"][b]}')

            else:
                index1 = keys.index(i)
                print(f'{keys_rus[index1]}: {data[i]}')

else:
    print('Попробуйте снова...')
