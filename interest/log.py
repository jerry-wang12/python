#!/usr/bin/python
# -*-coding:UTF-8-*-
#在当前目录创建日志文件，并为日志添加前缀

import os,time

TIMEFORMAT = "%Y%m%d"
TIMEFORMATFORDOC = "%A %B.%d/%Y %I:%M %p %Z"
localtime =  time.localtime(time.time())
filename = time.strftime(TIMEFORMAT,localtime)+"-logfile.txt"
print filename

def writetofile(filename):
    fileobj = open(filename,'w')
    fileobj.write("#jerry@mac `s log, now is "+time.strftime(TIMEFORMATFORDOC,localtime));
    fileobj.close()


if(os.path.exists(filename)):
    print "该日志文件已经存在",filename
    os.system('subl '+filename)
else:
    print "在当前目录下创建日志文件",filename
    os.system('touch '+filename)
    writetofile(filename)
    os.system('subl '+filename)


# if(os.path.exist()):

