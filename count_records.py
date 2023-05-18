import os
import sys

from pymarc import MARCReader

def count_records(marc_file):
    with open(marc_file, 'rb') as file:
        reader = MARCReader(file)
        count = 0
        for record in reader:
            count += 1
        return count


if len(sys.argv) != 2:
    print("Please provide a valid file path.\nUsage 1: py count_records.py 'path_to_file'\nusage 2: py count_records.py 'path_to_folder'")
    sys.exit()

arg = sys.argv[1]

if os.path.exists(arg):        
    marc_path = sys.argv[1]
else:
    marc_path = "" 
    while os.path.exists(marc_path) != True:
        marc_path = input("Please enter a valid file path: ")

if os.path.isfile(marc_path):
    count = count_records(marc_path)
    file_name = os.path.basename(marc_path)
    print(f"file name: {file_name}      records in file: {count}")
    sys.exit()

else:
    # if folder loop through folder 
    for file in os.listdir(marc_path):
        if file.endswith(".mrc"):
            count = count_records(marc_path)
            file_name = os.path.basename(marc_path)
            print(f"file name: {file_name}      records in file: {count}")
            sys.exit()



