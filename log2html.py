"""
Author      :Hiroaki Ogino
Name        :"log2html.py"
Function    :read login logout time and output to html file.
date        :2017-05-29
usage       :>log2html.py
"""
#coding:utf-8
#file_dir  = "home/mc1.11.2/log/"
file_dir = "./"
file_name = "latest.log"

#html_dir = "/var/www/html/"
html_dir = "./"
html_name = "minelog.html"

f = open(file_dir+file_name,'r')
for row in f:
    if 'logged in' in row:
        print row.strip()
f.close
