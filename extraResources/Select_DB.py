import sqlite3
import subprocess
from selenium import webdriver
import time 
import sys
import os


selectTaula = sys.argv[1]
con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()

#--------------------------------------------------Tagafa les hores els minuts i segons ---------------------------------.
TimeInt = []
sec = cursorObj.execute(f"SELECT segundos,minutos,horas FROM {selectTaula}")

myTime = cursorObj.fetchall()
print(myTime)

for i in range(len(myTime)):
    Ftime = str(myTime[i])
    TimeStirp= Ftime.strip("(',)")
    TimeInt.append(TimeStirp)
print(TimeInt) # pritn = ["5, 0, 0", "5, 0, 0", "2, 0, 0"] ["sec", "hor", "min"]



ColDir = cursorObj.execute(f"SELECT direccion FROM {selectTaula}")
myDir = cursorObj.fetchall()

dirs = []
for i in range(len(myDir)):
    Furl = str(myDir[i])
    ArrUrl= Furl.strip("(',)")
    dirs.append(ArrUrl)
print(dirs) # print = ["C:\\Users\\CAPA\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe", "https://www.youtube.com/", "C:\\Users\\CAPA\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"]


MarizDirs = []
MarizTime = []

def Do_ArryToArry(TimeInt,dirs):
    for i in dirs:
        v = [i]
        MarizDirs.append(v) # print( [['https1'], ['https1'], ['dir1'], ['dir2'], ['http']] )
    for i in TimeInt:
        v = [i]
        MarizTime.append(v)#print( [["0, 3, 1"], ["8, 10, 2"], ["2, 3, 4"], ["7, 1, 0"], ["5, 8, 0" ]] )
Do_ArryToArry(TimeInt,dirs)

cont = len(dirs)
liDicTime = []


Dic_total_Time_Dirs = []
def MakeTotalDict():
  t = 0
  for i in MarizDirs:
    dicTime = dict(zip(i,(MarizTime[t])))
    Dic_total_Time_Dirs.append(dicTime)
    #print(dicTime)
    t+=1
MakeTotalDict()

#print(Dic_total_Time_Dirs) # [{'https1': '0, 3, 1'}, {'https1': '8, 10, 2'}, {'dir1': '2, 3, 4'}, {'dir2': '7, 1, 0'}, {'http': '5, 8, 0'}]

totalKeys = []


def get_TotalKeys(totalKeys):
  for i in Dic_total_Time_Dirs:
    keys =i.keys()
    totalKeys.append(keys)
get_TotalKeys(totalKeys)

#print(totalKeys): [dict_keys(['https1']), dict_keys(['https1']), dict_keys(['dir1']), dict_keys(['dir2']), dict_keys(['http'])]

globalTime = []

def getValues(totalKeys):
  for i in range(len(totalKeys)):
    timeArr = Dic_total_Time_Dirs[i]
    valuesTime = timeArr.values()
    globalTime.append(valuesTime)
getValues(totalKeys)


arrGetTime = []

def normalize_Values(globalTime):
  for i in range(len(globalTime)):
    arrTime =  globalTime[i] 
    #print(arrTime)
    for getTime in arrTime:
      arrGetTime.append(getTime)
normalize_Values(globalTime)

# no permet que un valor sigui null

arrMins = []
def getMins(rrGetTime,arrMins):
  
  for url in arrGetTime:
    print(url)
    try:

      mins = int(url[3:5])
      arrMins.append(mins)
      
    except:
      mins = int(url[3:4])
      arrMins.append(mins)

getMins(arrGetTime,arrMins)

arrSec = []
def getSec(arrGetTime,arrSec):
  
  for url in arrGetTime:

    try:
      sec = int(url[0:2]) # Fer-ho amb un if no com un try o Posar amb un for el (try) o el (print)
      arrSec.append(sec)
      
    except:
      sec = int(url[0:1])
      arrSec.append(sec)

getSec(arrGetTime,arrSec)

arrHor= []
def getHor(arrGetTime,arrHor):
  
  for url in arrGetTime:

    try:
      horas = int(url[6:8])
      arrHor.append(horas)
      
    except:
      horas = int(url[6:7])
      arrHor.append(horas)

getHor(arrGetTime,arrHor)


com = 'http'
def Web_o_Dir(com, arrMins, arrSec, arrHor):
  s=0
  for i in totalKeys:
    for url in i:
      if com in url:

        print(url, 'web')
        print("Sec -> ",arrSec[s])
        print("Mins -> ",arrMins[s])
        print("Hor -> ",arrHor[s])

        driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe') # obre el webdriver
        driver.get(str(url))
        
        time.sleep(arrMins[s]*60)# *60
        time.sleep(arrSec[s])
        time.sleep(arrHor[s]*3600)#*3600

        driver.close() # Tanca el webdriver

      else:
 
        print(url, 'dir')
        print("Sec -> ",arrSec[s])
        print("Mins -> ",arrMins[s])
        print("Hor -> ",arrHor[s])
        
        p = subprocess.Popen(str(url)) # Obre el .exe

        time.sleep(arrMins[s]*60)# *60
        time.sleep(arrSec[s])
        time.sleep(arrHor[s]*3600)#*3600

        subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)]) # Tanca el .exe

    s+=1  

Web_o_Dir(com, arrMins, arrSec, arrHor)




sys.stdout.flush()
