import shutil
import os
from_directory=r'C:\Users\dhruv\Downloads'
to_directory=r'C:\Users\dhruv\OneDrive\Desktop\Python Coding\Class 112 Classwork'
listOfFiles=os.listdir(from_directory)
print(listOfFiles)
for file_name in listOfFiles:
    name,extention=os.path.splitext(file_name)
    if extention=="":
        continue
    if extention in [".gif",".png",".jpeg",".jpg",".jfif"]:
        path1=from_directory+"/"+file_name
        path2=to_directory+"/"+"image_files"
        path3=to_directory+"/"+"image_files"+"/"+file_name
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            shutil.move(path1, path3)        