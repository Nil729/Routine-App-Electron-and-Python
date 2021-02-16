from selenium import webdriver
from time import sleep
from tkinter import messagebox
import sys


url = sys.argv[1]
xTime = sys.argv[2]


def Open_CloseWebside(url, xTime):
    driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver.get(str(url))
    sleep(int(xTime))
    driver.close()
Open_CloseWebside(url,xTime)
