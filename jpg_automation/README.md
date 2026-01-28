# Task Automation with Python: Move .jpg Files
## Project Overview

This project automates the task of organizing image files by moving all .jpg files from a source folder to a destination folder using Python. It leverages the os and shutil modules to perform file and folder operations automatically.

## Goal

To reduce manual effort in organizing image files and automate the movement of .jpg files to a separate folder.

## Technologies Used

Programming Language: Python

Modules: os, shutil

Platform: Command Line / Terminal

## Key Concepts Used

File and folder handling

Looping through folder contents (os.listdir())

Moving files (shutil.move())

Conditional checks (if statements)

## How to Run

Create a folder named source_images in the same directory as the script.

Add .jpg files into source_images.

Open terminal/PowerShell in the project directory.

Run the script:

python move_jpg_files.py

📊 Sample Output
Moved file: image1.jpg
Moved file: image2.JPG

Total .jpg files moved: 2


A new folder jpg_files is automatically created with the moved images.

✅ Advantages

Automates repetitive file organization tasks

Easy to use and beginner-friendly

Works for multiple .jpg files at once

Real-time feedback for each moved file

## Future Enhancements

Support .png and .jpeg files

Handle duplicate file names automatically

Allow user to enter folder names at runtime

Add a GUI for easier use

👩‍💻 Author   Kokila
