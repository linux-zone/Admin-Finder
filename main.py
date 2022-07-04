#!/usr/bin/python3
# <-- Mr Shell -->
from requests import get
from threading import Thread
from re import match
import os

os.system('clear' if os.name == 'posix' else 'cls')
print('''\x1b[1;35m
    _       _           _       _____ _           _           
   / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ 
  / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|
 / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |   
/_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_|\x1b[00m

     \x1b[33m[+] Creator:  \x1b[36m [ Mr-shell              ]
     \x1b[33m[+] Github:   \x1b[36m [ Github.com/Linux-Zone ]
     \x1b[33m[+] Telegram: \x1b[36m [ T.me/Linux_Zone_Org   ]
''')

website = input('\x1b[91m>> \x1b[94mEnter Website Url (www.example.com): \x1b[00m')
if not match("^(http|https)://", website.lower()): website = "https://" + website
path = input('\x1b[91m>> \x1b[94mEnter wordlist file path (wordlist.txt): \x1b[00m')
if path.strip() == "": path = "wordlist.txt"
wordlist = open(path, "r").read().splitlines()

def check():
    for word in wordlist:
        if website[-1] == "/": url = website + word
        else: url = website + "/" + word
        try:
            request = get(url)
            if request.status_code == 200:
                print(f"\x1b[94m[\x1b[92m200\x1b[94m]\x1b[00m {url}")
            else:
                print(f"\x1b[94m[\x1b[91m{request.status_code}\x1b[94m]\x1b[00m {url}")
        except KeyboardInterrupt:
            print('\n\x1b[91mHave good time :)\x1b[00m\n')
            time.sleep(1)
            sys.exit()
        except Exception:
            print(f"\x1b[94m[\x1b[91m502\x1b[94m]\x1b[00m {url}")

print("\n\x1b[94m[*]\x1b[00m Please wait...!\n")
thread = Thread(target=check)
thread.start()
