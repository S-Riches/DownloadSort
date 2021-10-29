import os
from types import TracebackType
import setup
import sys
from pathlib import Path
import shutil



# this code sorts your download folder and if it has been run before then it will place the new files in pre-existing folders
def main():
    setup.setup()    
    path = str(Path.home() / "Downloads")

    try:
        imagesort(path)
        videoSort(path)
        compFolders(path)
        music(path)
        documents(path)
        miscFiles(path)
        # have a bool to check if its sorted? i.e. loop to keep going after rename occurs

    except shutil.Error as a:
        print(a)
        # break error into string, seperate at ' and save the second item in that list (the destination)
        dupeList = str(a).split("'")
        dupe = dupeList[1]
        
        #debug
        print(dupe)
        renameDupeFile(dupe)
        return "Error < {dupe} > found!, adding (01) to tag now".format(dupe = a)



def imagesort(path):
    #makes a list of all files, the goes through each one
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/Images")
    for i in files:
        #if the file ends with any of these tags then move them to the corresponding folder needed.
        if i.lower().endswith((".png", ".gif", ".jpg", ".jpeg", ".bmp", ".heic",".jfif")):
            shutil.move(i, path)
            print(i)
        

#video sort is a copy of image sort but is for videos, and a bit slower :(
def videoSort(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/Videos")
    for i in files:
        if i.lower().endswith((".mp4", ".mov", ".webm", ".mkv", ".avi", ".flv")):
            shutil.move(i, path)
            #print(i)

# move compressed folders into one folder + executables
def compFolders(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/ZIPS, RARS, .exe's")
    for i in files:
        if i.lower().endswith((".zip", ".rar", ".7z", ".exe", ".gz", ".jar")):
            shutil.move(i, path)
            #print(i)

# move audio files to music folder
def music(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/Music")
    for i in files:
        if i.lower().endswith((".mp3", ".mid", ".wav", ".ogg")):
            shutil.move(i, path)
            #print(i)

# move documents to documents folder
def documents(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/Documents")
    for i in files:
        #checks if the for loop has gone over the read me, if true skip to next list item
        if i == "README_ForSetupPy.txt":
            pass
        elif i.lower().endswith((".txt", ".pdf", ".docx", ".pptx", ".csv", ".xlsx", ".log", ".doc", ".md", ".html", ".yml", ".conf")):
            shutil.move(i, path)
            #print(i)

# move remaining files to misc folder
def miscFiles(path):
    files = os.listdir(path)
    path = str(Path.home()/ "Downloads/Misc")
    for i in files:
        if i == "README_ForSetupPy.txt":
            pass
        else:
            if os.path.isdir(i) == False:
                shutil.move(i, path)
                #print(i)

# this function should rename a file that has been found in two different locations
def renameDupeFile(file):
    # check that the file isnt setup or directory
    try:
        if os.path.isdir(file) == False:
            if file != "README_ForSetupPy.txt":
                # splits the name into the root and extension
                name, ext = os.path.splitext(file)
                # formats the string to add (01) to stop the naming issue
                newFileName = "{Name}_{id}{ext}".format(Name = name, id = '(01)', ext = ext)
                # debug
                print(newFileName)
                # os.rename is used to rename the file.
                os.rename(file, newFileName)
        else:
            pass
    except FileNotFoundError:
        # apostrophe in file name error, shouldnt be too common, however it needs to be shown to user. possible todo?
        print("file not found, could have apostrophe in file name")
        return("file has apostrophes, please rename")
        

