import os

directory = (fr"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\POSTthese")
for filename in os.listdir(directory):

    print(filename)
    os.remove(fr"C:\Users\Henrik\Documents\PROGRAMMING\tiktokbot\POSTthese\{filename}")