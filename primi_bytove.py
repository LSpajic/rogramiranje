#!/usr/bin/python3.6
import socket
import sys
from giga_file import give_dir_items
#otvori socket na nekom portu
# slusaj da dodje konekcija
# primi bajtove
# vrati "hvala!"


def main(server_ip, server_port):
    content1_temp = """\n<html><body> FILES IN {}:<ul>"""
    content2 ="""<li>{}: <a href="{}">{}</a></li>"""
    content3 ="""</ul></body></html>\n"""
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((server_ip, server_port))
    soc.listen()
    conn_socket, conn_info = soc.accept()
    #print(conn_socket)
    #print(conn_info)
    while 1:
        cli_msg = conn_socket.recv(1024).decode('ascii')    
        x = cli_msg.split("\n")
        line1 = x[0].split(" ")
        line2 = x[1].split(" ")
        line3 = x[2]

        print(cli_msg)

        dicti = {"method" : line1[0] , "path" : line1[1] , "protocol" : line1[2].strip() , "User-Agent":line3[12:len(line3)], "host" : line2[1]}
        html_header = "{} {}\nServer: LovroServer\nContent-Length: {}\nContent-Type: text/html\nConnection: keep-alive\n\n"
        path = "." + dicti['path']
        content1 = content1_temp.format(path)
        status = "200 OK"
        try:
                dirs = give_dir_items(path)
                posalji = ""
                for link,vrsta in dirs:
                        posalji += content2.format(vrsta, "/" + path + "/" + link, link)
                if len(dirs) == 0:
                        posalji = "EMPTY"
                content = content1 + posalji + content3
        except FileNotFoundError as fnfe:
                status = "404 Not Found"
                content = ""

        html_header = html_header.format(dicti["protocol"], status, str(len(content)))
        print(html_header)
        conn_socket.sendall((html_header + content).encode())

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
