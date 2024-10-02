import os
import argparse
import shutil
from shutil import SameFileError


parser = argparse.ArgumentParser(description = 'argument parser')
parser.add_argument('--list', help='--list', action='store_true')
parser.add_argument('--file', help='--file', action='store_true')
parser.add_argument('--folder', help='--file', action='store_true')
parser.add_argument('--move', action='store_true', help='--move')
parser.add_argument('--copy', action='store_true', help='--move')
parser.add_argument('--file_path', type=str, help='--file_path file/path')
parser.add_argument('--folder_path', type=str, help='--folder_path folder/path')
parser.add_argument("--destination", type=str, help="--destination destination/path")
parser.add_argument("--delete", type=str, help="--delete file/path")

directory = os.getcwd()
files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
folders = [file for file in os.listdir(directory) if not os.path.isfile(os.path.join(directory, file))]
files_and_folders = os.listdir(directory)

args = parser.parse_args()
args_dict = vars(args)
args_values = list(args_dict.values())
bool_args_values = 0
for x in range(1,len(args_values)):
    if args_values[x] == True:
        bool_args_values = 1

if args.list and args.file:
    for file in files:
        print(file)

if args.list and args.folder:
    for folder in folders:
        print(folder)

if args.list and bool_args_values == 0:
    for doc in files_and_folders:
        print(doc)

if args.move:
    if not(args.file_path and args.destination) and not (args.folder_path and args.destination):
        print("Error: both file or folder path and destination are required")
    if args.file_path and args.destination:
        if not os.path.exists(args.file_path):
            print(f"Error: The file{args.file_path} does not exist")
        elif not os.path.isfile(args.file_path):
            print(f"Error: The file{args.file_path} is not a valid file")
        elif not os.path.isdir(args.destination):
            print(f"Error: The destination {args.destination} is not a valid directory")
        else:
            shutil.move(args.file_path, args.destination)
    if args.folder_path and args.destination:
        if not os.path.exists(args.folder_path):
            print(f"Error: The folder{args.folder_path} does not exist")
        elif not os.path.isdir(args.folder_path):
            print(f"Error: The folder{args.folder_path} is not a valid folder")
        elif not os.path.isdir(args.destination):
            print(f"Error: The destination {args.destination} is not a valid directory")
        else:
            shutil.move(args.folder_path, args.destination)

if args.copy:
    if not(args.file_path and args.destination) and not (args.folder_path and args.destination):
        print("Error: both file or folder path and destination are required")
    if args.file_path and args.destination:
        if not os.path.exists(args.file_path):
            print(f"Error: The file{args.file_path} does not exist")
        elif not os.path.isfile(args.file_path):
            print(f"Error: The file{args.file_path} is not a valid file")
        else:
            try:
                shutil.copy(args.file_path, args.destination)
            except SameFileError:
                print("You are trying to copy the same file")
    if args.folder_path and args.destination:
        try:
            shutil.copytree(args.folder_path, args.destination)
        except FileExistsError:
            print(f"Error: The destination folder {args.destination} already exists")
        except NotADirectoryError:
            print(f"Error: The destination {args.destination} is not a directory")
        except FileNotFoundError:
            print(f"Error: The source folder {args.folder_path} not found")

if args.delete:
    try:
        os.remove(args.delete)
        print(f"File deleted successfully")
    except FileNotFoundError:
        print(f"Error: File {args.delete} not found")
    except PermissionError:
        print(f"The {args.delete} is a folder. You cannot delete a folder")