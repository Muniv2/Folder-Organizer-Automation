import os
import shutil
import time

"""
This program helps organize a folder by doing three things: it moves files older than a year to a backup folder and renames any duplicates, it gathers all empty folders into one "empty folder," and it sorts files into new subfolders based on their extensions. 
"""

def move_old_files(sourcedirpath, backupdirpath):
    #Moves files older than a year from the source directory to a backup directory, preserving their relative folder structure.

    current_time=time.time() # Get the current time 
    age_threshold=365*24*60*60 # Set age threhold for files
    for dirpath, dirnames, filenames in os.walk(sourcedirpath): #walk through directory and sub-directories and their files
        for file in filenames:
            try:
                filepath=os.path.join(dirpath, file) #get filepath for each file 
                if os.path.isfile(filepath): #check if its a file
                    fileage=current_time - (os.path.getmtime(filepath)) #get file age
                    if fileage>age_threshold: 
                        faddpath=os.path.join(backupdirpath, file) #path of file if it will be stored in backup folder
                        if os.path.exists(faddpath): #check if any such file alr exists
                            fnewname=f"{file}_{int(time.time())}" #if exists so rename it
                            os.rename(filepath, os.path.join(dirpath, fnewname)) #rename to get updated filepath of the same file but with a new name
                        shutil.move(filepath, backupdirpath)
            except Exception as e:
                    print(f"Error {e} occured in moving {filepath}")

def move_empty_folders(sourcedirpath):
    # move all empty folders in directory and sub-directories into one main folder containing all empty folders.
    empty_dir_path=os.path.join(sourcedirpath, "empty folder")
    os.makedirs(empty_dir_path, exist_ok=True) #make "empty folder" directory in backup directory to store all empty folders
    for dirpath, dirnames, filenames in os.walk(sourcedirpath):
        for dir in dirnames: #iterate over each sub-directory in this current directory
            if dir=="Main backup" or dir=="empty folder" or "valo wallpaper": #skip over "empty folder" directory
                continue
            else:
                try:
                    dpath=os.path.join(dirpath, dir) #get sub-directory path
                    if len(os.listdir(dpath))==0: #check if sub-directory is empty
                        if os.path.exists((os.path.join(empty_dir_path, dir))): 
                            newdirname=f"{dir}_{int(time.time())}"
                            os.rename(dpath, os.path.join(dirpath, newdirname))
                            shutil.move(dpath, empty_dir_path)
 #if sub-directory with the same name exist in "empty folder" directory so we rename this sub-directory and then move it in "empty folder" (two folders with the same name cant exist together in a directory)
                        else: #if sub-directory name unique so directly added to "empty folder" directory
                            shutil.move(dpath, empty_dir_path)
                except Exception as e:
                    print(f"Error {e} occured in moving {dpath}")

def organize_files(sourcedirpath):
    #organize all files based on their extension
    for dirpath, dirnames, filenames in os.walk(sourcedirpath):
        for file in filenames:
            try:
                filepath=os.path.join(dirpath, file) #main file path we are moving
                if os.path.isfile(filepath):
                    f, ext=os.path.splitext(file) #split filename and extension
                    if ext=="": #if no extension
                        f_noext_path=os.path.join(sourcedirpath, "no ext") #path to folder where files with no extension stored
                        os.makedirs(f_noext_path, exist_ok=True) #made directory inside backup folder to store files with no extension
                        fadd=os.path.join(f_noext_path, f) #path of file that is going to be stored in this directory, need to use it to check if any file with the same path (name) exists or not
                        if os.path.exists(fadd):
                            newf_noext_name=f"{f}_{int(time.time())}" #filename changed using timestamps
                            os.rename(filepath, os.path.join(dirpath, newf_noext_name)) #main filepath renamed
                        shutil.move(filepath, f_noext_path) 
                    else:
                        fname=ext[1:] #seperated extension (removed dot using slicing)
                        fpath=os.path.join(sourcedirpath, fname) #path to folder where files with this specific extension stored
                        os.makedirs(fpath, exist_ok=True) #made directory for this extension in backup folder
                        fileadd=os.path.join(fpath, f) #path of file that is going to be stored in this directory, need to use it to check if any file with the same path (name) exists or not
                        if os.path.exists(fileadd):
                            newfname=f"{f}_{int(time.time())}" #filename changed using timestamps
                            os.rename(filepath, os.path.join(dirpath, newfname)) #main filepath renamed
                        shutil.move(filepath, fpath)
            except Exception as e:
                print(f"Error {e} occured in moving {filepath}")


def main(sourcedirpath, backupdirpath):
    if not os.path.exists(sourcedirpath):
        print("Source directory path not found")
        return
    os.makedirs(backupdirpath, exist_ok=True)
    move_old_files(sourcedirpath, backupdirpath)
    move_empty_folders(sourcedirpath)
    organize_files(sourcedirpath)

# main(source_directory, backup_directory)

#enter directory to clean path in source_directory place and another backup directory path in backup_directory place
