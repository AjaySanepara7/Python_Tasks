import argparse
import subprocess


parser = argparse.ArgumentParser(description = 'argument parser')
parser.add_argument('--list', help='--list', action='store_true')
parser.add_argument('--sort--file', help='--sort', type=str)
parser.add_argument('--sort--folder', help='--sort', type=str)
parser.add_argument('--compress', help='--list', action='store_true')
parser.add_argument('--decompress', help='--list', action='store_true')
parser.add_argument('--file',  help='--file', action='store_true')
parser.add_argument('--folder', help='--file', action='store_true')
parser.add_argument('--move', action='store_true', help='--move')
parser.add_argument('--copy', action='store_true', help='--move')
parser.add_argument('--file_path', type=str, help='--file_path file/path')
parser.add_argument('--folder_path', type=str, help='--folder_path folder/path')
parser.add_argument("--destination", type=str, help="--destination destination/path")
parser.add_argument("--delete", type=str, help="--delete file/path")


args = parser.parse_args()
args_dict = vars(args)
args_values = list(args_dict.values())
bool_args_values = 0

for x in range(1,len(args_values)):
    if args_values[x] == True:
        bool_args_values = 1
if args.list and bool_args_values == 0:
    subprocess.call(f" python File_Manager.py --list", shell=True)
if args.list and args.file:
    subprocess.call(f" python File_Manager.py --list --file", shell=True)
if args.list and args.folder:
    subprocess.call(f" python File_Manager.py --list --folder", shell=True)
if args.move:
    if not(args.file_path and args.destination) and not (args.folder_path and args.destination):
        print("Error: both file or folder path and destination are required")
    if args.file_path and args.destination:
        subprocess.call(rf' python File_Manager.py --move --file_path "{args.file_path}" --destination "{args.destination}"', shell=True)
    if args.folder_path and args.destination:
        subprocess.call(rf' python File_Manager.py --move --folder_path "{args.folder_path}" --destination "{args.destination}"', shell=True)
if args.copy:
    if not(args.file_path and args.destination) and not (args.folder_path and args.destination):
        print("Error: both file or folder path and destination are required")
    if args.file_path and args.destination:
        subprocess.call(rf' python File_Manager.py --copy --file_path "{args.file_path}" --destination "{args.destination}"', shell=True)
    if args.folder_path and args.destination:
        subprocess.call(rf' python File_Manager.py --copy --folder_path "{args.folder_path}" --destination "{args.destination}"', shell=True)
if args.delete:
    subprocess.call(f" python File_Manager.py --delete", shell=True)

if args.sort__file:
    subprocess.call(f' python Sorter.py --sort --file "{args.sort__file}"', shell=True)
if args.sort__folder:
    subprocess.call(f' python Sorter.py --sort --folder "{args.sort__folder}"', shell=True)

if args.compress and args.file_path:
    subprocess.call(f' python Compress_Your_Stuff.py --compress --file_path "{args.file_path}"', shell=True)
if args.decompress and args.file_path:
    subprocess.call(f' python Compress_Your_Stuff.py --decompress --file_path "{args.file_path}"', shell=True)