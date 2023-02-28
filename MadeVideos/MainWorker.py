import praw
import pandas as pd
from praw.models import MoreComments
import time
import gtts
from playsound import playsound
from TextGrabber import GetGoodComments
from Talker import TextToSpeech 
from videomaker import MovieMaker

#CommentsObject = GetGoodComments(SUBREDDIT = 'AskReddit')  

LONGBIGLIST = (GetGoodComments(SUBREDDIT = 'AskReddit')) # THIS GRABS SUBREDDIT THING

counter = 0
#url("https://thumbs.gfycat.com/JaggedAstonishingGuillemot-size_restricted.gif");
for sublist in LONGBIGLIST: 
    try:
        print(sublist)
        print("SEP--------------------------------------------------------------SEP")
        counter +=1 
        Name = f"test{counter}"

        MovieMaker(sublist,Name) # add text to speech to 
    except IndexError:
        pass

#PostThing()


#tiktokRedditAccountPrivate
#v&6B%M*VRD3kKQB

#vscodegoodvscodegood
#v&6B%M*VRD3kKQB

#maintiktokreddit@outlook.com

#for i in list = sendkeys

#reddit   #redditstories     #redditstoriestts    #fyp    #fypage    #askreddit    #subwaysurfer    #questions   #redditstoriestok  #askredditstories 