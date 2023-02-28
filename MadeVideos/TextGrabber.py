import praw
import pandas as pd
from praw.models import MoreComments

def GetGoodComments(SUBREDDIT):

    BIGLIST_RESPONSES = []

    reddit = praw.Reddit(
        #YOUR KEYS HERE        
        client_id=
        client_secret=
        user_agent=
        username = 
        password = 
        )

    # get hottest posts from a subreddit subreddits

    #hot_posts = reddit.subreddit(f'{SUBREDDIT}').hot(limit=10)
    hot_posts = reddit.subreddit(f'{SUBREDDIT}').top(time_filter="week",limit=2)
    #hot_posts = reddit.subreddit(f'{SUBREDDIT}').top(time_filter="month",limit=20)
    #print(hot_posts[1])

    postNames = []

    for post in hot_posts:
        postNames.append(post.name)
    
    
   # postNames = postNames[-5:] #GET LAST 20 INSTEAD WE NEED MORE VARIATION

    print(reddit.user.me())
    print(len(postNames))

    for postName in postNames:

        listPerPost = []
        superlistPerPost = []

        postName = postName[3:] #remove thee charchters from start of id its weird idk works tho
        print(postName)

        submission = reddit.submission(id=f"{postName}")
        submission.comments.replace_more(limit=0) # remove more comments issue

        bestcomments = []
        
        for topcomments in submission.comments:
            if len(topcomments.body) > 30: #too short comments is bad
                if len(topcomments.body) < 90: #too big is bad too!
                    bestcomments.append(topcomments.body)

        #--- here happens magic
        print(submission.title)
        #listPerPost.append(submission.title)
        for comments in bestcomments[:8]:
            
            print(f"\n\n {comments}")
            listPerPost.append(comments)

        superlistPerPost = [submission.title,listPerPost]
        BIGLIST_RESPONSES.append(superlistPerPost)
    
    return(BIGLIST_RESPONSES)
    
if __name__ == "__main__":
    LONGBIGLIST = (GetGoodComments(SUBREDDIT = 'AskReddit'))
    print("OK HERE IS ALL THE LONGBIGLIST STUFF *************************************")

    for sublist in LONGBIGLIST:
        print(sublist)
        print("SEP--------------------------------------------------------------SEP")