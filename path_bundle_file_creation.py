import os
import re
from platformdirs import user_documents_path

document_path = user_documents_path()

def test_file_creation():
    unpacked_data = "usernames, passwords, and social security numbers, all that"
    with open(f"{document_path}/unpacked_data.txt", "w") as f:
        f.write(unpacked_data)

def file_check(path):
    try:
        os.path.exists(path)
        return True
    except:
        return False
        print("File check error")

def path_count(path):
    count = 0
    for char in path:
        count += 1
    return str(count) + "^"

def packing(path): #function to pack the data within specified format and return a packed file
    if file_check(path):
        with open(path, "r") as f:
            data = f.read()

    count = path_count(path)
    package = str(count) + path + data
    with open(f"{document_path}/packed_data.txt", "w") as f:
        f.write(package)

def peel_count(data):
    data_without_count = ""
    for char in data:
        if char != "^":
            data_without_count += char
        else:
            break
    return data_without_count

def peel_path(ct, data): #returns path
    beg = rf"^{ct}\^" 
    number_removed = re.sub(beg, "", data, count=1)
    extracted_path = ""

    c = 0
    while c < int(ct):
        extracted_path += number_removed[c]
        c += 1
    return extracted_path
    
def unpacking(path): #grab packed and unpack and direct it using the headed info
    if file_check(path):
        with open(path, "r") as f:
            data = f.read()

        count = peel_count(data)
        peeled_path = peel_path(count, data)
    
        with open(peeled_path, "w") as f:
            f.write(data[int(count) + (len(count) + 1):])

'''---------------------------------------------------------------------------'''
test_file_creation()
# packing(f"{document_path}/unpacked_data.txt")
# unpacking(f"{document_path}/packed_data.txt")