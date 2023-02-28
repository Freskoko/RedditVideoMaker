from re import T
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import csv
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import zipfile
import os
import random
import undetected_chromedriver as uc

#Hearthstone9


def PostThing():
    for i in range(1):
        
        print(f"POST ATTEMPT 1")
        
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        driver = uc.Chrome()
        action = webdriver.ActionChains(driver)

        #---DOWNLOADING 

        driver.get("https://www.tiktok.com/login/phone-or-email/email")

        time.sleep(3)

        username = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/div[1]/input")
        username.send_keys("askreddittoktts")

        passw = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/div[2]/div/input")
        passw.send_keys("v&6B%M*VRD3kKQB")

        time.sleep(0.2)

        login = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/button")
        login.click()

        time.sleep(5)

        upload = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/div[1]/div[1]/span")
        upload.click

        time.sleep(2)



        directory = (fr"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\POSTthese")
        #import pyautogui
        #import zipfile
        #import os

        for filename in os.listdir(directory):
            print(filename)
            # check if current path is a file

            pathNameMP4 = os.path.abspath(fr"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\POSTthese\{filename}")
            print(pathNameMP4)

            selectfile = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button")
            selectfile.click()

            time.sleep(0.5)

            pyautogui.write(pathNameMP4) 
            pyautogui.press('enter')

            time.sleep(0.2)

            caption = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div")
            caption.click()

            captionlist3 = ["#reddit","#redditstories","#redditstoriestts","#fyp","#fypage","#askreddit","#fypシ","#questions","#redditstoriestok","#askredditstories"]
            time.sleep(3)

            pyautogui.write("Follow @reddit2tts for more!  シ❓")

            #for i in range (7):
                #pyautogui.write(".")
                #pyautogui.press("enter")

            for i in captionlist3:

                pyautogui.write(i, interval=0.01)  # type with quarter-second pause in between each key
                time.sleep(3.0)
                pyautogui.press("space")  # type with quarter-second pause in between each key

                #turn off view and comments

            time.sleep(40)

            postbutton = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[7]/div[2]/button")
            postbutton.click() 

            time.sleep(3)

            uploadanother = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[2]")
            uploadanother.click()

            time.sleep(10)

        directory = (fr"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\POSTthese")
        for filename in os.listdir(directory):

            print(filename)
            os.remove(fr"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\POSTthese\{filename}")
    
    time.sleep(10)
    driver.quit()

    

if __name__ == '__main__':
    PostThing()