import os
from pathlib import Path
from sys import path

# gonna hardcode some text to put in the new file wanna clean up my main script so please deal with the setup script lol also if this line is too long pls use word wrap you luddite :)


def setup():
    
    #some variables
    readMeText = 'Thanks for using my script, this file is a check to make sure you dont get extra folders (so pls dont change the file name)\nIncase you already have ran this code before. \nThe TLDR of this program is that it will sort your downloads folder, and only that folder so please dont try it else where. \n \n \nSo pretty much just run this script and it should be all good, also dont worry i cant see your "special" files or any file for that matter, \nInfact go ahead and read the source code as theres no way i can see anything lol. \n\nAnyway all loves and kisses from me and enjoy your clean downloads folder : )\n\n'
    

    if "README_ForSetupPy.txt" in str(Path.home() / "Downloads"):
        print("all good")
    elif "README_ForSetupPy.txt" not in str(Path.home() / "Downloads") :
        os.chdir(str(Path.home() / "Downloads"))
        readMe = open("README_ForSetupPy.txt", "w+")
        readMe.write(readMeText)
        readMe.close()
        try:
            os.mkdir("Images")
            os.mkdir("Videos")
            os.mkdir("ZIPS, RARS, .exe's")
            os.mkdir("Music")
            os.mkdir("Misc")
            os.mkdir("Documents")
        except FileExistsError:
            pass
