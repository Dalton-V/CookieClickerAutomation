import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import keyboard
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
    cookieX, cookieY = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5) 
    #todo: these should be settings to select in the GUI
    buyCursor = False
    buyGrandma = False
    buyFarm = False
    buyMine = False
    buyFactory = False
    buyBank = False
    buyTemple = False
    buyWizard = False
    buyShhipment = False
    buyAlchemy = False
    buyPortal = False
    buyTimeMachine = False
    buyAntimCondenser = True
    buyPrism = True
    buyChancemaker = True
    buyFractalEngine = True
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

        #Scroll down to see more buildings
        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\bank.png', confidence=0.8)
            pyautogui.moveTo(cursorX, cursorY)
            pyautogui.scroll(-500)
        except pyautogui.ImageNotFoundException:
            print("Bank not found")

        if buyFractalEngine:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\FractalEngine.png', confidence=0.6)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Fractal Engine not found")

        if buyChancemaker:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Chancemaker.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Chancemaker not found")

        if buyPrism:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Prism.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Prism not found")

        if buyAntimCondenser:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\AntimCondenser.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Antim Condenser not found")

        if buyTimeMachine:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\TimeMachine.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Time Machine not found")

        if buyPortal:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Portal.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Portal not found")

        #Scroll up
        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\bank.png', confidence=0.8)
            pyautogui.moveTo(cursorX, cursorY)
            pyautogui.scroll(500)
        except pyautogui.ImageNotFoundException:
            print("Bank not found")

        if buyAlchemy:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\AlchemyLab.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("AlchemyLab not found")

        if buyShhipment:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\shipment.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("shipment not found")

        if buyWizard:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\wizard.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("wizard not found")

        if buyTemple:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\temple.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("temple not found")

        if buyBank:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\bank.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("bank not found")

        if buyFactory:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\factory.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("factory not found")

        if buyMine:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\mine.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("mine not found")

        if buyFarm:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\farm.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("farm not found")

        if buyGrandma:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\grandma.png', confidence=0.5)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("grandma not found")

        if buyCursor:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\cursor.png', confidence=0.5)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("cusor not found")

        pyautogui.click(cookieX, cookieY, 1000, .025)

        if keyboard. is_pressed('esc'):
            exit()

window = tk.Tk()
window.geometry('500x500')

clickCookieButton = ttk.Button(master = window, text = "Click Cookie", command = click_cookie)
clickCookieButton.pack()

autoPlayButton = ttk.Button(master = window, text = "Auto Play", command = auto_play)
autoPlayButton.pack()

readButton = ttk.Button(master= window, text = "Read", command= read)
readButton.pack()

window.mainloop()