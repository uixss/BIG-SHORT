import requests
import sys
import time
import random
import os
from colorama import Fore

def clckru(url_e):
    try:
        shin_agent = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
        }
        shin_gets = requests.get('https://clck.ru/--?url=' + url_e, headers=shin_agent).text
        print('--------------------------------------------------------------')
        print(Fore.GREEN + 'Clck.ru RESULT : ' + shin_gets + Fore.WHITE)
        print('--------------------------------------------------------------')
    except Exception as e:
        print(Fore.RED + "Clck.ru Error: " + str(e) + Fore.WHITE)

def Main():
    try:
        url_e = input("URL [ You Must Use http:// ] : ")
        print(Fore.YELLOW + "\nGenerating shortened URLs for the given URL...\n" + Fore.WHITE)

        clckru(url_e)
        
    except Exception as e:
        print(Fore.RED + "Error: " + str(e) + Fore.WHITE)

Main()

def ulangi():
    ulangin = input("Do you want to run the program again? Y/N : ").lower()
    if ulangin == "y":
        os.system("python shorten.py")
    elif ulangin == "n":
        print("CODED BY SHIN_CODE")
        sys.exit()

ulangi()
