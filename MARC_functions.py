# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
""" 
    very much a work in progress
    aim is to have numerous general marc utilities in here
    which can then be pulled through for other scripts
"""

import os
import shutil
import re

from pymarc import MARCReader
from pymarc import Record, Field
from pymarc import XMLWriter
from pymarc import MARCWriter
import pymarc

# -

def get_marc_file_paths():

    marc_file_paths = []

    for file in os.listdir():
        if file.endswith(".mrc"):
            marc_file = file
            marc_file_path = os.path.join(marc_file)
            marc_file_paths.append(marc_file_path)
    return marc_file_paths


def unzip_zips():
    for file in os.listdir():
        if file.endswith(".zip"):
            shutil.unpack_archive(file)


def delete_marc_by_eisbn(marc_file,eisbn_to_delete):
    with open(marc_file, 'rb') as file:
        reader = file
        for record in reader:
            eisbn_field = (record['020']['a'])
            eisbn_pattern = re.search(r"978\d{10}",eisbn_field)
            eisbn_check = eisbn_pattern.group()
            if eisbn == eisbn_to_delete:
                print("{} found, deleting record".format(eisbn))
                del record


def print_eisbns(marc_file):
    with open(marc_file, 'rb') as file:
        reader = MARCReader(file)
        for record in reader:
            eisbn_field = (record['020']['a'])
            eisbn_pattern = re.search(r"978\d{10}",eisbn_field)
            print(eisbn_pattern.group())


def count_records(marc_file):
    with open(marc_file, 'rb') as file:
        reader = MARCReader(file)
        count = 0
        for record in reader:
            count += 1
        return count


