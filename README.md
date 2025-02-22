# Usage
You can freely use, modify, and distribute this code. However, you must include the original copyright notice and this license in any copies or substantial portions of the software. The software is provided "as is," without any warranties or guarantees, and the author, Munir Tariq Malik (Muniv2), is not responsible for any issues that may arise.

# File Organizer Project

This program helps organize a folder by doing three things: it moves files older than a year to a backup folder and renames any duplicates, it gathers all empty folders into one "empty folder," and it sorts files into new subfolders based on their extensions. 

## How It Works

This **File Organizer** script automates the organization of files and folders in a source directory. It performs three main tasks:

1. **Move Old Files:** It moves files that are older than one year from the source directory to a backup folder. If a file with the same name already exists in the backup folder, it renames the file by appending a timestamp.

2. **Move Empty Folders:** It identifies and moves all empty folders from the source directory into a new folder called "empty folder."

3. **Organize Files by Extension:** It organizes all files in the source directory by their extensions, creating a subfolder for each extension. Files without an extension are moved into a folder named "no ext."

The program uses the **os** module for directory traversal, the **shutil** module to move files, and the **time** module to handle timestamps when renaming files.

