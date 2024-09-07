import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import keyboard

pyautogui.FAILSAFE = True

def click_cookie():
    cookielocationx, cookielocationy = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5)
    pyautogui.click(cookielocationx, cookielocationy, 500, .025)

def auto_play():
    x = 0
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

        #Allow for numbers to not cover cookie.
        time.sleep(1)

        #Go back to the cookie to colapse the store menu
        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5)
            pyautogui.click(cursorX, cursorY, 5, .025)
        except pyautogui.ImageNotFoundException:
            print("Cookie not found")

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('F:\\Code\\Python\\CookieClickerAutomation\\Photos\\AlchemyLab.png', confidence=0.8)
            pyautogui.click(cursorX, cursorY, 4, .025)
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

        try:
            cursorX, cursorY = pyautogui.locateCenterOnScreen('f:\\code\\python\\CookieClickerAutomation\\photos\\cookie.png', confidence=0.5)
            pyautogui.click(cursorX, cursorY, 1000, .025)
        except pyautogui.ImageNotFoundException:
            print("Cookie not found")
        
        print(x)

        try:
            if keyboard.is_pressed('esc'):
                break
            else:
                pass
        finally:
            pass

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

window.mainloop()