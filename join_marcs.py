import shutil, os, sys

import pyperclip

files_loc = pyperclip.paste()

if os.path.exists(files_loc) != True:
    files_loc = input("Please enter file path for folder containing marcs to be joined: ")

if len(sys.argv) > 1:
    if sys.argv[1].endswith(".mrc"):
        output_file_name = sys.argv[1]
    else:
        output_file_name = sys.argv[1] + ".mrc"
else:
    output_file_name = "output_file.mrc"

def join_marcs_in_folder(files_loc, output_file_name):
    output_file_path = os.path.join(files_loc, output_file_name)
    with open(output_file_path, "wb") as output_file:
        for file in os.listdir(files_loc):
            if file.endswith(".mrc") and file != output_file_name:
                file_loc = os.path.join(files_loc, file)
                with open(file_loc, "rb") as input_file:
                    shutil.copyfileobj(input_file, output_file)
                    input_file.close()
                    
join_marcs_in_folder(files_loc, output_file_name)