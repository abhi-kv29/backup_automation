import os
import schedule
import shutil
import datetime
import time

# Automation Script to take backup of folders

src_dir = "C:/Path/to/Copy/From"
dest_dir = "C:/Folder/to/Copy/to"


def copy_Folder_to_Directory(src_dir, dest_dir):
    today = datetime.date.today()
    dest = os.path.join(dest_dir, str(today))
    
    try:
        shutil.copytree(src_dir, dest)
        print(f"folder copied to: {dest}")
    except FileExistsError:
        print(f"folder already exists in: {dest}")
        

schedule.every().day.at("15:28").do(lambda: copy_Folder_to_Directory(src_dir, dest_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
