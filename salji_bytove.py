#!/usr/bin/python3.6

import sys
import socket

def main(file_path, dest_ip, dest_port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((dest_ip,dest_port))
    dat = open(file_path, mode="rb")
    print()
    soc.send(dat.read())

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))