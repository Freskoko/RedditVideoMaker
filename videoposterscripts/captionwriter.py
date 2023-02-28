import pyautogui
import time

#for i in list = sendkeys

captionlist = ["#reddit","#reddittiktok","#redditts","#redditstories","#redditreading","#fyp","#fypage","#askreddit","#subwaysurfers","#reddit_tiktok","#redditstoriestok","#askredditstory"]
captionlist2 = ["#reddit", "#redditmemes", "#redditstories", "#redditposts","#askredditstory","#askreddit","#redditts"]
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