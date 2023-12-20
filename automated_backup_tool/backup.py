import schedule
import shutil
import os
import datetime
import time

source_dir = 'D:\study\SEM 7\OFF CAMPUS IT IZZZ\python projects\python_automation_projects\\automated_backup_tool\pictures'
destination_dir = 'C:/Users/YASH/Desktop/Backups'

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to {dest_dir}");
    except FileExistsError:
        print(f'Folder already exists in {dest}')

copy_folder_to_directory(source_dir, destination_dir)

schedule.every().day.at("20:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
