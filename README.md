# DownloadSort
This is a python script that should sort the downloads folder on Mac and windows.
There is a simple GUI in TKinter provided with the code and a build incase the user doesnt have python on their machine/device. 

# common issues:
- **Q** - 'My download folder isnt being sorted' *A* - This may be due to a name conflict: either a file inside the folder is already the same name but with a (01) after it, or there is an apostrophe within the file, which breaks the function. At this moment in time im unsure of how to fix this but there should be a fix at some point in the future. The following code is this `python dupeList = str(a).split("'")` and then subsequently this `python dupe = dupeList[1]` this is where the error is split by the apostrophe character, and then the middle point (the file location) is then indexed from the created array and put into the function `python renameDupeFile(dupe)`.

- **Q** - 'My script isnt working and the files all have different names' *A* - This is most likely due to the file being outdated, where the file needs to be redownloaded from this github. this can be down to new libraries or even just a corrupt file.

- **Q** - 'Does this work outside the download folder?' *A* - Unfortunately at the moment it does not, this is because the program finds the download folder via the path library, as to not need to hard code a location that will change from computer to computer. perhaps in the future if i come back to expanding this code there will be a feature that allows the user to input their directory that they want sorted.

