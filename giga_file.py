#!/usr/bin/python3.6
import os
from os import listdir
from os.path import isfile, join

def give_dir_items(path):
    lista = os.listdir(path)
    result = []

    for dat in lista:
        if os.path.isfile(dat):
            result.append((dat, "file"))
        elif os.path.isdir(dat):
            result.append((dat, "directory"))
        else:
            result.append((dat, "special"))
    return result

def main():
    path = "."
    result = give_dir_items(path)
    print(result)

if __name__ == "__main__":
    main()