from code import compile_command
import gtts
from playsound import playsound
from TextGrabber import GetGoodComments
import os

import time

def TextToSpeech(Comments):

    flat_list = []
    goneOnce = 0
    for sublist in Comments:
        
        if goneOnce != 0:
            for item in sublist:
                flat_list.append(item)
        
        if goneOnce == 0:
            goneOnce += 1
            flat_list.append(sublist)


    Comments = flat_list

    print("------------LEGTNH-------------------------------------")
    print(len(Comments))

    while len(Comments) > 5:
        Comments.pop(-1)

    Comments = "? ".join(Comments)


    for j in [",","^","_","/",":",".com","https",".gif",'"']:
        Comments = Comments.replace(j," ")

    for j in ["sex","porn","fucking"," fuck","bitch"]:
        Comments = Comments.replace(j,"fun")
    
    print(len(Comments))

    print(Comments)


    tts = gtts.gTTS(Comments, lang='en', tld='co.za')
    #os.chdir(r"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\MadeVideos")
    tts.save("Comments.mp3")
    print("----------------saved!")
    time.sleep(3)
    

if __name__ == "__main__":
    
    Comments = ("one","two","three","four","five","six")
    TextToSpeech(Comments)