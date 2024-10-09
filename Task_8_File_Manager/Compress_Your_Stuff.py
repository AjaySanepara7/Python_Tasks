import argparse
import zipfile


parser = argparse.ArgumentParser(description = 'argument parser')
parser.add_argument('--compress', help='--list', action='store_true')
parser.add_argument('--decompress', help='--list', action='store_true')
parser.add_argument('--file_path', type=str, help='--file_name file name')

args = parser.parse_args()

def file_compress(inp_file_names, out_zip_file):
    compression = zipfile.ZIP_DEFLATED
    print(f" *** Input File name passed for zipping - {inp_file_names}")

    print(f' *** out_zip_file is - {out_zip_file}')
    zf = zipfile.ZipFile(out_zip_file, mode="w")

    try:
        for file_to_write in inp_file_names:
            print(f'*** Processing file {file_to_write}')
            zf.write(file_to_write, file_to_write, compress_type=compression)
    except FileNotFoundError as e:
        print(f' *** Exception occurred during zip process - {e}')
    finally:
        zf.close

def file_decompress(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

if args.compress and args.file_path:
    files_to_compress = [args.file_path]
    output_zip = r"F:\Drive E\Python\Python-Tasks\Task_8_File_Manager\Zip_files\zip.py"

    file_compress(files_to_compress, output_zip)

if args.decompress and args.file_path:
    file_decompress(args.file_path, r"F:\Drive E\Python\Python-Tasks\Task_8_File_Manager\Decompressed_zip_files")