# Code to control the data logs.

import os
import datetime
from time import gmtime, strftime
# So that it is easy to change location of files.
path_to_current = "/home/pi/Desktop/NEA/Final Code/current.txt"
path_to_records = "/home/pi/Desktop/NEA/Final Code/records.txt"

# To create the files if they haven't already.
def file_create(file):
    try: 
        if file == "current":
            o = open(path_to_current, "x")
            o.close
            return False
        elif file == "records":
            o = open(path_to_records, "x")
            o.close()
            return False
        else:
            return "Cannot create file"
    except FileExistsError:
        return True


# To write to current file
def current(data):
    now = strftime("%a, %d %b %Y %X",gmtime())
    file_create("current")
    save = open(path_to_current, "a")
    save.write("Date/time: {} Information: {} \n".format(now, data))
    save.close()
    return "Data Saved sucessfully"


# To write to the records
def records(data):
    now = strftime("%a, %d %b %Y %X",gmtime())
    file_create("records")
    save = open(path_to_records, "a")
    save.write("Date/time: {} Information: {} \n".format(now, data))
    save.close()
    return "Data Saved sucessfully"


# To open the file in the GUI
def open_file(file):
    try:
        if file == "current":
            return open(path_to_current).read()
        elif file == "records":
            return open(path_to_records).read()
        else:
            return "File Not Found."
    except Exception as error:
        return error
        


# The search function
def search(file, target):
    if file == "Current Process":
        search_in = open(path_to_current, "r")
        searchlines = search_in.readlines()
        matching = [item for item in searchlines if target in item]
        if any(target in item for item in searchlines):
            return matching
        else:
            return "Search not found. Please try again."
        search_in.close()
    elif file == "Records":
        search_in = open(path_to_records, "r")
        searchlines = search_in.readlines()
        matching = [item for item in searchlines if target in item]
        if any(target in item for item in searchlines):
            return matching
        else:
            return "Search not found. Please try again."
        search_in.close()
    else:
        return "Error finding file. Please try again."


# To delete the current folder when the program closes.
def current_destroy():
    os.remove(path_to_current)
    return "Current processes data log has been successfully deleted."


