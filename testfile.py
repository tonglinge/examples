# -*- coding:utf-8 -*-

import os
import stat

"""
openfile = os.path.dirname(os.path.abspath("__file__")) + "\\source.txt"
file_stat = os.stat(openfile)
print(file_stat)
print(file_stat.st_mode)
print(stat.S_ISDIR(file_stat.st_mode))
print(stat.S_ISFIFO(file_stat.st_mode))
print(os.path.isfile(openfile))
print(stat.S_ISREG(file_stat.st_mode))

with open(file , 'r') as f:
    f.seek(5)
    a = f.readlines(）
"""

openfile = os.path.dirname(os.path.abspath("__file__")) + "\\source3.txt"
c_lines = ["abcdefg\n","higjksldf\n","dki29dfa\n"]
c_str = "abcde\nssss\nccccc"
with open(openfile, 'r+',encoding='utf-8') as f:
    print(f.read())






