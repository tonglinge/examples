# -*- coding:utf-8 -*-

import os
import stat

openfilepath = os.path.dirname(os.path.abspath("__file__"))
file1 = openfilepath + "\\1.txt"
file2 = openfilepath + "\\2.txt"
with open(file1,'r') as f1,open(file2,'a+') as f2:
    f2.write(f1.read())

"""
file_stat = os.stat(openfile) # return tuple

print("st_mode:", file_stat.st_mode)    # 权限模式
print("st_ino:", file_stat.st_ino)     # inode number
print("st_dev:", file_stat.st_dev)     # device
print("st_size:", file_stat.st_size)    # 文件的大小，以位为单位
print("uid:", file_stat.st_uid)     # 所有用户的user id
print("gid:", file_stat.st_gid)     # 所有用户的group id
print("st_atime:", file_stat.st_atime)   # 文件最后访问时间
print("st_mtime:", file_stat.st_mtime)   # 文件最后修改时间
print("st_ctime:", file_stat.st_ctime)   # 文件创建时间

stat.S_ISREG(st_mode)  == os.path.isfile(filename)  # 判断是否一般文件
stat.S_ISDIR(st_mode)  == os.path.isdir(filename)   # 判断是否为文件夹
stat.S_ISLNK(st_mode)  == os.path.islink(filename)   # 判断是否链接文件
stat.S_ISSOCK(st_mode)  # 判断是否套接字文件
stat.S_ISFIFO(st_mode)  # 判断是否命名管道
stat.S_ISBLK(st_mode)   # 判断是否块设备
stat.S_ISCHR(st_mode)   # 判断是否字符设置


"""
"""
openfile = os.path.dirname(os.path.abspath("__file__")) + "\\source3.txt"
c_lines = ["abcdefg\n","higjksldf\n","dki29dfa\n"]
c_str = "abcde\nssss\nccccc"
with open(openfile, 'r+',encoding='utf-8') as f:
    print(f.read())


"""

