import os, re, sys

import pyperclip, pymarc

if len(sys.argv) > 1:
    files_loc = sys.argv[1]

if len(sys.argv) <= 1:
    files_loc = pyperclip.paste()

if os.path.exists(files_loc) != True:
    files_loc = input("Please enter file path for folder containing marcs to be joined: ")

success_count = 1
error_count = 0

for marc_file in os.listdir(files_loc):
    # get all marc files in folder 
    if marc_file.endswith(".mrc"):
        # create file path
        marc_file_loc = os.path.join(files_loc,marc_file)
        # open marc file
        with open(marc_file_loc, 'rb') as file:
            reader = pymarc.MARCReader(file, to_unicode=True, force_utf8=True)
            for record in reader:
                try:
                    eisbn_field = record['020']['a']
                    eisbn_pattern = re.search(r"978\d{10}", eisbn_field)
                    output_file_name = str(eisbn_pattern.group()) + ".mrc"
                    output_file_loc = os.path.join(files_loc, output_file_name)
                    
                except TypeError as e:
                    print(f"Type Error wih {record}\nError message: {e}")
                    # count error
                    error_count += 1
                    continue
                except UnicodeEncodeError as e:
                    print(f"Unicode Error wih {record}\nError message: {e}")
                    # count error
                    error_count += 1
                    continue

                # count success
                success_count += 1
                with open(output_file_loc, 'wb') as out:
                    try:
                        out.write(record.as_marc())
                    except UnicodeEncodeError as e:
                        print(f"Unicode Error wih {record}\nError message: {e}")
                        # count error
                        error_count += 1
                        continue

print(f"Total error count: {error_count}")
print(f"total files split: {success_count}")      
