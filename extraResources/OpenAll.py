import sqlite3
import subprocess
from selenium import webdriver
import time 
import sys
import os
import webbrowser


selectTaula = sys.argv[1]
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()

#--------------------------------------------------Tagafa les hores els minuts i segons ---------------------------------.

ColDir = cursorObj.execute(f"SELECT direccion FROM {selectTaula}")
myDir = cursorObj.fetchall()

dirs = []
for i in range(len(myDir)):
    Furl = str(myDir[i])
    ArrUrl= Furl.strip("(',)")
    dirs.append(ArrUrl)
print(dirs) # print = ["C:\\Users\\CAPA\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe", "https://www.youtube.com/", "C:\\Users\\CAPA\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"]


com = 'http'
def Web_o_Dir(com):
    for url in dirs:
      if com in url:

        print(url, 'web')
        webbrowser.open_new(url)
        #driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe') # obre el webdriver
        #driver.get(str(url))
        
      else:
 
        print(url, 'dir')

        p = subprocess.Popen(str(url)) # Obre el .exe
        


Web_o_Dir(com)




sys.stdout.flush()
