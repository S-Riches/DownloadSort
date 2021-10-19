# DownloadSort
This is a python script that should sort the downloads folder on Mac and windows.
there is a simple GUI in TKinter provided with the code and a build incase the user doesnt have python on their machine/device. 

# common issues:
- Q - 'my folder isnt being sorted' a - this may be due to a name conflict, i.e. there may be a two files called image.png that the script is trying to place in the folder, raising this issue.
- Q - 'my script isnt working and the files all have different names' a - this is most likely due to the file being outdated, where the file needs to be redownloaded from this github. this can be down to new libraries or even just a corrupt file.
- Q - 'does this work outside the download folder?' a - unfortunately at the moment it does not, this is because the program finds the download folder via the path library, as to not need to hard code a location that will change from computer to computer.
