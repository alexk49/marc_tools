import shutil, os, sys

import pyperclip
import pymarc

if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    files_loc = sys.argv[1]
else:
    files_loc = pyperclip.paste()

if len(sys.argv) < 1:
    files_loc = pyperclip.paste()

if os.path.exists(files_loc) != True:
    files_loc = input("Please enter file path for folder containing marcs to be joined: ")
 
for file in os.listdir(files_loc):
    if file.endswith(".mrc"):
        output_file_name = file.replace(".mrc",".xml")
        file_loc = os.path.join(files_loc, file)
            
        output_file_path = os.path.join(files_loc, output_file_name)
            
        with open(file_loc, "rb") as input_file:
            reader = pymarc.MARCReader(input_file)
            writer = pymarc.XMLWriter(open(output_file_path, "ab"))
            for record in reader:
                writer.write(record)
            writer.close()