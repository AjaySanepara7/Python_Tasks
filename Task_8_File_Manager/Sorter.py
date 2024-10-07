import os
import argparse
import shutil
import stat 
from datetime import datetime
from math import ceil


parser=argparse.ArgumentParser(description="sample argument parser")
parser.add_argument('--sort', help='--sort', action='store_true')
parser.add_argument('--file', type=str, help='--list')
parser.add_argument('--folder', type=str, help='--list')
args = parser.parse_args()

def directory_ordered_by_creation_time(directory):
    def get_creation_time(entry):
        return entry.stat().st_ctime
    
    with os.scandir(directory) as entries:
        sorted_entries = sorted(entries, key=get_creation_time)
        sorted_time = [(datetime.fromtimestamp(entry.stat().st_birthtime),entry.path) for entry in sorted_entries]
    return sorted_time
# time_stamp = directory_ordered_by_creation_time(r"F:\Drive E\Python\Python-Tasks\Task_8_File_Manager\ajay")

# for x,y in time_stamp:
#     print(x,y)
months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
path = args.file
path_folder = args.folder
parent_dir = r"E:"
def week_of_month(dt):

    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom/7.0))


if args.sort and args.file:
    time_stamps = directory_ordered_by_creation_time(path)
    for date_obj,dir_entry_path in time_stamps:
        if os.path.isfile(dir_entry_path):
            month_name = date_obj.strftime("%B")
            week_number = week_of_month(date_obj)

            month_folder = rf"{parent_dir}\{month_name}"
            file_month = rf"{month_folder}\Files_{month_name}"
            week_folder = rf"{file_month}\Week {week_number}"

            if not os.path.exists(month_folder):
                os.makedirs(month_folder)

            if not os.path.exists(file_month):
                os.makedirs(file_month)

            if not os.path.exists(week_folder):
                os.makedirs(week_folder)

            shutil.move(dir_entry_path, week_folder)

            print(f"Created or found folder and moved the files: {week_folder}")

if args.sort and args.folder:
    time_stamps = directory_ordered_by_creation_time(path_folder)
    for date_obj,dir_entry_path in time_stamps:
        if os.path.isdir(dir_entry_path):
            month_name = date_obj.strftime("%B")
            week_number = week_of_month(date_obj)

            month_folder = rf"{parent_dir}\{month_name}"
            folder_month = rf"{month_folder}\Folder_{month_name}"
            week_folder = rf"{folder_month}\Week_{week_number}"

            if not os.path.exists(month_folder):
                os.makedirs(month_folder)
                os.chmod(month_folder, 0o444)
                # os.chmod(folder_month, stat.S_IREAD)  

            if not os.path.exists(folder_month):
                os.makedirs(folder_month)
                os.chmod(folder_month, 0o444)
                # os.chmod(folder_month, stat.S_IREAD)

            if not os.path.exists(week_folder):
                os.makedirs(week_folder)
                os.chmod(week_folder, 0o444)
                # os.chmod(folder_month, stat.S_IREAD)

            # if folder_month == dir_entry_path:
            for x in months_list:
                if x in os.path.basename(dir_entry_path):
                    shutil.move(dir_entry_path, week_folder)
            # else:
            # shutil.move(dir_entry_path,week_folder)

            print(f"Created or found folder and moved the folders: {week_folder}")