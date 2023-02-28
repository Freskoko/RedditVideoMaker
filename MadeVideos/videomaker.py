# Import everything needed to edit video clips 
from ctypes import resize
from moviepy.editor import *
from Talker import TextToSpeech
from TextGrabber import GetGoodComments
import random
import textwrap
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import vfx
import moviepy.editor as mpe
#from moviepy.audio.fx.volumex import volumex  
#from moviepy import AudioFileClip
#from moviepy.editor import *
import moviepy.audio.fx.all as afx
from moviepy.editor import *
import time

def MovieMaker(CommentList,Name):

    #[name][comments]

    comments = CommentList[1]
    title = CommentList[0]

    # ----------------------------------------------------

    def insert_newlines(string, every=33):
        return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

    commentsUpdated = []

    for i in comments:
        NewStr = textwrap.wrap(i, 33)
        NewStr = '\n'.join(NewStr)
        commentsUpdated.append(NewStr)

    titleDisplay = textwrap.wrap(title, 16)
    titleDisplay = '\n'.join(titleDisplay)

    title = textwrap.wrap(title, 33)
    title = '\n'.join(title)

    finaltext = "😻FOLLOW FOR MORE!😎 POST YOUR ANSWER IN THE COMMENTS!⬇️"

    finaltext = textwrap.wrap(finaltext, 33)
    finaltext = '\n'.join(finaltext)

        
    # Generate a text clip #ADD NEWLINES #ADD TRANSPARENCY
    txtClipDisplay = TextClip(f"{titleDisplay}", fontsize = 90, color = 'IndianRed3',bg_color = "MistyRose1", font = "Rockwell") 
    txtClipDisplay.margin(20)
    txt_clipTitle = TextClip(f"{title}", fontsize = 53, color = 'red',bg_color = "black", font = "Berlin-Sans-FB") 
    txt_clip0 = TextClip(f"{commentsUpdated[0]}", fontsize = 50, color = 'orange',bg_color = "black", font = "Berlin-Sans-FB") 
    txt_clip1 = TextClip(f"{commentsUpdated[1]}", fontsize = 50, color = 'green',bg_color = "black", font = "Berlin-Sans-FB") 
    txt_clip2 = TextClip(f"{commentsUpdated[2]}", fontsize = 50, color = 'HotPink4',bg_color = "black", font = "Berlin-Sans-FB") 
    txt_clip3 = TextClip(f"{commentsUpdated[3]}", fontsize = 50, color = 'VioletRed2',bg_color = "black", font = "Berlin-Sans-FB") 
    txt_clip4 = TextClip(f"{finaltext}", fontsize = 45, color = 'SteelBlue',bg_color = "black",font = "Rockwell") 
    # setting position of text in the center and duration will be 10 seconds 

    carspersecond = 19 #-----

    txtClipDisplay = txtClipDisplay.set_pos('center').set_start(0).set_end(0.3).set_opacity(1)

    #-----------

    timeToSpendTitle = (len(title)/carspersecond) 

    txt_clipTitle = txt_clipTitle.set_pos('center').set_start(0.3).set_end(timeToSpendTitle).set_opacity(0.8)
    #-----------

    if len(commentsUpdated[0]) <= 32:
        timeToSpend0 = (len(commentsUpdated[0])/carspersecond) + timeToSpendTitle +2
    if len(commentsUpdated[0]) > 32:
        timeToSpend0 = (len(commentsUpdated[0])/carspersecond) + timeToSpendTitle +2

    txt_clip0 = txt_clip0.set_pos('center').set_start(timeToSpendTitle).set_end(timeToSpend0).set_opacity(0.8)
    #-----------

    if len(commentsUpdated[1]) <= 32:
        timeToSpend1 = (len(commentsUpdated[1])/carspersecond) + timeToSpend0 +2
    if len(commentsUpdated[1]) > 32:
        timeToSpend1 = (len(commentsUpdated[1])/carspersecond) + timeToSpend0 +2

    txt_clip1 = txt_clip1.set_pos('center').set_start(timeToSpend0).set_end(timeToSpend1).set_opacity(0.8)

    #-----------

    if len(commentsUpdated[2]) <= 32:
        timeToSpend2 = (len(commentsUpdated[2])/carspersecond) + timeToSpend1 +2
    if len(commentsUpdated[2]) > 32:
        timeToSpend2 = (len(commentsUpdated[2])/carspersecond) + timeToSpend1 +2

    txt_clip2 = txt_clip2.set_pos('center').set_start(timeToSpend1).set_end(timeToSpend2).set_opacity(0.8)

    #-----------

    timeToSpend3 = (len(commentsUpdated[3])/carspersecond) + timeToSpend2 +2

    txt_clip3 = txt_clip3.set_pos('center').set_start(timeToSpend2).set_end(timeToSpend3).set_opacity(0.8)

    #-----------

    timeToSpend4 = (len(finaltext)/carspersecond) + timeToSpend3 +2

    txt_clip4 = txt_clip4.set_pos('center').set_start(timeToSpend3).set_end(timeToSpend4).set_opacity(0.8)
        
    # Overlay the text clip on the first video clip #order is important
    #add talking:

    # loading video (will have subwayus surfers content here)

    # clipping of the video  
    # getting video for 0-10 seconds, should be between random intervals in a hour long subway surfers video
    clip = VideoFileClip(r"C:\Users\Henrik\Documents\PROGRAMMING Python\tiktokbot\MadeVideos\SubwaySurfer.mp4") 

    clip = clip.resize((1080,1920))

    clipAmount = random.randint(50,200)


    clip2 = clip.subclip(clipAmount-0.35, clipAmount+timeToSpend4-0.35)
    
    clip2 = clip2.set_opacity(0.7)



    clip = clip.subclip(clipAmount, clipAmount+timeToSpend4) 
    
    #clip = clip.resize(height=812,width = 375) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
        
        
    # Reduce the audio volume (volume x 0.8) 


    #--- dog video

    timetospenddog = random.randint(5,6)

    clipDogs = VideoFileClip(r"C:\Users\Henrik\Documents\PROGRAMMING Python\tiktokbot\MadeVideos\neon.mp4").subclip(timetospenddog,timetospenddog+timeToSpend4)
    clipDogs = clipDogs.resize((1080,1920))
    clipDogs = clipDogs.set_pos('center')
    clipDogs = clipDogs.without_audio()
    clipDogs = clipDogs.set_opacity(0.20)
    #-----------
    


    #--- done

    video = CompositeVideoClip([clip,clip2,clipDogs, txtClipDisplay,txt_clip4,txt_clip3,txt_clip2,txt_clip1,txt_clip0,txt_clipTitle]) 

    #text to speech makes audio
    
    TextToSpeech(CommentList) #svaes audio as "Comments.mp3"

    time.sleep(2)

    audioclip = AudioFileClip(r"C:\Users\Henrik\Documents\PROGRAMMING Python\tiktokbot\MadeVideos\Comments.mp3") 
    
    clipAmountSong = random.randint(5,120)
    audiomusic = AudioFileClip(r"C:\Users\Henrik\Documents\PROGRAMMING Python\tiktokbot\MadeVideos\chillsong1.mp3") 
    audiomusic = audiomusic.subclip(clipAmountSong,clipAmountSong+timeToSpend4)

    #audiomusic = audiomusicWork.fx( vfx.volumex, 0.5)

    #audiomusic = audioclip.fx( afx.volumex, 0.2)

    #audiomusic = audiomusic.multiply_volume(0.3)

    #audiomusic = (audiomusic.max_volume(0.3) .audio_fadein(1.0) .audio_fadeout(1.0))

    #audiomusic = audiomusic.volumex(0.2)


    video.audio = CompositeAudioClip([audioclip,audiomusic.set_end(timeToSpend4)])
    #-----------

    # showing video 
    os.chdir(r"C:\Users\Henrik\Documents\PROGRAMMING Python\tiktokbot\MadeVideos")
    video.write_videofile(f"PartThree{Name}.mp4")

if __name__ == "__main__":
    #CommentList = ["comment1","comment2","comment3","comment4"]
    #print(GetGoodComments(SUBREDDIT = 'AskReddit'))
    MovieMaker(GetGoodComments(SUBREDDIT = 'AskReddit'))


