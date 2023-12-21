import os
import schedule
import shutil
import datetime
import time


src_dir = "C:/Users/DELL/Pictures/Screenshots"
dest_dir = "C:/Users/DELL/backup_files"


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