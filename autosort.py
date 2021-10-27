import os
import setup
from pathlib import Path
import shutil

dupeList = []


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


    except shutil.Error as a:
        print(a)
        dupeList.append(a)
        print('list', *dupeList)
        return dupeList
        #TODO need to finish the dupe system

    




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
def renameDupeFile(path):

    # OH basically need to rewrite this to only check for files that are in the list not the directory, otherwise this does every non directory file
    files = os.listdir(path)
    path = str(Path.home()/ "Downloads")
    for i in files:
        if os.path.isdir(i) == False:
            # need a check that the file is a dupe.
            if i != "README_ForSetupPy.txt":
                #rename
                #print(i)
                name, ext = os.path.splitext(i)
                print(name,ext)
                newFileName = "{Name}_{id}{ext}".format(Name = name, id = '(01)', ext = ext)
                print(newFileName)
                pass
            else:
                pass
        else:
            pass

