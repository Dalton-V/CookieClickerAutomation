import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import keyboard
import easyocr
import numpy as np

pyautogui.FAILSAFE = True  

def ascend():
    try:
        cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Prestige.png', confidence=0.6)
        pyautogui.click(cursorX, cursorY)
        pyautogui.press('enter') 
        time.sleep(7)
        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Reincarnate.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY)
            pyautogui.press('enter')
            time.sleep(7)
        except pyautogui.ImageNotFoundException:
            print("Reincarnate not found")
            return False
    except pyautogui.ImageNotFoundException:
        print("Prestige not found")
        return False

def read():
    reader = easyocr.Reader(['en'])
    pyautogui.screenshot('screenschot.png')
    text = reader.readtext('screenschot.png')
    for x in text:
        print(x)

def click_cookie():
    cookielocationx, cookielocationy = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5)

    while True:
        pyautogui.click(cookielocationx, cookielocationy, 200, .025)

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\GoldenCookie.png', confidence=0.4)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Golden Cookie not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\RedCookie.png', confidence=0.4)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Red Cookie not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\JackO.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("JackO not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\WrinklerSanta.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 6)
        except pyautogui.ImageNotFoundException:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Wrinkler2.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 6)
            except pyautogui.ImageNotFoundException:
                try:
                    cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Wrinkler3.png', confidence=0.8)
                    pyautogui.click(cursorX, cursorY, 6)
                except pyautogui.ImageNotFoundException:
                    print("Wrinkler not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Raindeer.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Raindeer not found")
        

def look_for_green():
    image = np.array(pyautogui.screenshot())
    greenPixels = np.argwhere(image == [97,235,96])

    for x in greenPixels:
        pyautogui.click(x[0], x[1])

def auto_play():
    cookieX, cookieY = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5) 
    #todo: these should be settings to select in the GUI
    buyShop = True
    buyCursor = True
    buyGrandma = True
    buyFarm = True
    buyMine = True
    buyFactory = True
    buyBank = True
    buyTemple = True
    buyWizard = True
    buyShhipment = True
    buyAlchemy = True
    buyPortal = True
    buyTimeMachine = True
    buyAntimCondenser = True
    buyPrism = True
    buyChancemaker = True
    buyFractalEngine = True
    buyJavascript = True
    buyIdleverse = True
    buyCortex = True
    buyYou = True
    attemptAscend = False
    while True:

        if attemptAscend:
            ascend()

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\GoldenCookie.png', confidence=0.4)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Golden Cookie not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\RedCookie.png', confidence=0.4)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Red Cookie not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Raindeer.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY)
        except pyautogui.ImageNotFoundException:
            print("Raindeer not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Wrinkler.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 5)
        except pyautogui.ImageNotFoundException:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Wrinkler2.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 5)
            except pyautogui.ImageNotFoundException:
                try:
                    cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Wrinkler3.png', confidence=0.8)
                    pyautogui.click(cursorX, cursorY, 5)
                except pyautogui.ImageNotFoundException:
                    print("Wrinkler not found")

        if buyShop:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Upgrade.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Store icon not found")

            pyautogui.scroll(-10000)
            time.sleep(.5)

        if buyCortex:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Cortex.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 51, .025)
            except pyautogui.ImageNotFoundException:
                print("Cortex not found")

        if buyYou:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\You.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 101, .025)
            except pyautogui.ImageNotFoundException:
                print("You not found")
        
        if buyIdleverse:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Idleverse.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Idleverse not found")     
        
        if buyJavascript:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Javascript.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Javascript not found")

        if buyFractalEngine:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\FractalEngine.png', confidence=0.6)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Fractal Engine not found")

        if buyChancemaker:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Chancemaker.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Chancemaker not found")

        if buyPrism:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Prism.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Prism not found")

        if buyAntimCondenser:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\AntimCondenser.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Antim Condenser not found")

        if buyTimeMachine:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\TimeMachine.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Time Machine not found")

        if buyPortal:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Portal.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("Portal not found")

        if buyAlchemy:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\AlchemyLab.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("AlchemyLab not found")

        pyautogui.scroll(10000)
        time.sleep(.5)

        if buyShhipment:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\shipment.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("shipment not found")

        if buyWizard:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\wizard.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("wizard not found")

        if buyTemple:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\temple.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("temple not found")

        if buyBank:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\bank.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("bank not found")

        if buyFactory:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\factory.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("factory not found")

        if buyMine:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\mine.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("mine not found")

        if buyFarm:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\farm.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("farm not found")

        if buyGrandma:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\grandma.png', confidence=0.5)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("grandma not found")

        if buyCursor:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\cookieclickerautomation\\photos\\cursor.png', confidence=0.5)
                pyautogui.click(cursorX, cursorY, 25, .025)
            except pyautogui.ImageNotFoundException:
                print("cusor not found")

        if buyShop:
            try:
                cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\Upgrade.png', confidence=0.8)
                pyautogui.click(cursorX, cursorY, 2, .025)
            except pyautogui.ImageNotFoundException:
                print("Store icon not found")

        if attemptAscend:
            ascend()        

        pyautogui.click(cookieX, cookieY, 300, .025)

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