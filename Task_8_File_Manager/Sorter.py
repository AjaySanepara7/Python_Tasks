import os
import argparse
import shutil
import time
from datetime import datetime

# time_seconds = os.path.getctime(r"F:\Drive E\Python\Python-Tasks\Task_8_File_Manager\ronaldo")
# real_time = time.ctime(time_seconds)
# print(real_time) 

# with os.scandir(r"F:\Drive E\Python\Python-Tasks\Task_8_File_Manager\ajay") as entry:
#     for x in entry:
#         print(x.name)
parser=argparse.ArgumentParser(description="sample argument parser")
parser.add_argument('--sort', help='--list', action='store_true')
parser.add_argument('--file', help='--list', action='store_true')
args = parser.parse_args()

def directory_ordered_by_creation_time(directory):
    def get_creation_time(entry):
        return entry.stat().st_ctime
    
    with os.scandir(directory) as entries:
        sorted_entries = sorted(entries, key=get_creation_time)
        sorted_time = [datetime.fromtimestamp(entry.stat().st_birthtime) for entry in sorted_entries]
    return sorted_time

path = r"F:\Drive E\Python\Python-Tasks\Task_8_File_Manager\ajay"

month = set()
time_stamps = directory_ordered_by_creation_time(path)
for x in time_stamps:
    month.add(x.strftime("%B"))
    print(x)
    print(x.strftime("%A"))
    print(x.strftime("%w"))
print(month)