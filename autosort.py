import os
import setup
from pathlib import Path
import shutil
import ctypes, sys

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
    except shutil.Error:
        
        pass
        

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
            print(i)

# move compressed folders into one folder + executables
def compFolders(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/ZIPS, RARS, .exe's")
    for i in files:
        if i.lower().endswith((".zip", ".rar", ".7z", ".exe", ".gz", ".jar", ".dmg")):
            shutil.move(i, path)
            print(i)

# move audio files to music folder
def music(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/Music")
    for i in files:
        if i.lower().endswith((".mp3", ".mid", ".wav", ".ogg")):
            shutil.move(i, path)
            print(i)

# move documents to documents folder
def documents(path):
    files = os.listdir(path)
    path = str(Path.home() / "Downloads/Documents")
    for i in files:
        #checks if the for loop has gone over the read me, if true skip to next list item
        if i == "README_ForSetupPy.txt":
            pass
        elif i.lower().endswith((".txt", ".pdf", ".docx", ".pptx", ".csv", ".xlsx", ".log", ".doc", ".md", ".html", ".yml", ".conf", ".odt")):
            shutil.move(i, path)
            print(i)

# move remaining files to misc folder
def miscFiles(path):
    try:
        files = os.listdir(path)
        path = str(Path.home()/ "Downloads/Misc")
        for i in files:
            if i == "README_ForSetupPy.txt":
                pass
            elif i.lower().endswith(".DS_Store"):
                pass
            else:
                if os.path.isdir(i) == False:
                    shutil.move(i, path)
                    print(i)
    except shutil.Error:
        pass

main()

