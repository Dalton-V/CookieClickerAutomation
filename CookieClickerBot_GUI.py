import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import keyboard
import threading
import easyocr
import numpy as np

pyautogui.FAILSAFE = True  

def read():
    reader = easyocr.Reader(['en'])
    pyautogui.screenshot('screenschot.png')
    text = reader.readtext('screenschot.png')
    for x in text:
        print(x)

def click_cookie():
    cookielocationx, cookielocationy = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5)

    while True:
        pyautogui.click(cookielocationx, cookielocationy, 300, .025)
        
        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\GoldenCookie.png', confidence=0.4)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Golden Cookie not found")

        time.sleep(.5)

def look_for_green():
    image = np.array(pyautogui.screenshot())
    greenPixels = np.argwhere(image == [97,235,96])

    for x in greenPixels:
        pyautogui.click(x[0], x[1])

def auto_play():
    x = 0
    cookieX, cookieY = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5) 

    while True:
        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\GoldenCookie.png', confidence=0.4)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Golden Cookie not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\StoreEdge.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Store icon not found")

        #Go back to the cookie to colapse the store menu
        pyautogui.click(cookieX, cookieY, 5, .025)

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Portal.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 4, .025)
        except pyautogui.ImageNotFoundException:
            print("Portal not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\AlchemyLab.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("AlchemyLab not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Shipment.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Shipment not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Wizard.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Wizard not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Temple.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Temple not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Bank.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Bank not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Factory.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Factory not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Mine.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Mine not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Farm.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Farm not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Grandma.png', confidence=0.5)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Grandma not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Cursor.png', confidence=0.5)
            pyautogui.click(cursorX, cursorY, 2, .025)
        except pyautogui.ImageNotFoundException:
            print("Cusor not found")

        pyautogui.click(cookieX, cookieY, 1000, .025)
        print(x)

        if keyboard. is_pressed('esc'):
            exit()

        if x == 20:
            print('sleep')
            time.sleep(5)
            x = 0
        
        x = x+1

window = tk.Tk()
window.geometry('500x500')

clickCookieButton = ttk.Button(master = window, text = "Click Cookie", command = click_cookie)
clickCookieButton.pack()

autoPlayButton = ttk.Button(master = window, text = "Auto Play", command = auto_play)
autoPlayButton.pack()

readButton = ttk.Button(master= window, text = "Read", command= look_for_green)
readButton.pack()

window.mainloop()