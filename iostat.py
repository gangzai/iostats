# -*- coding:utf-8 -*-
#!/usr/in/python
#FIlename:iostat.py

'''/
#Version:1.0
#Author:WangZhigang
#Date:2015-07-14
'''

import os
import time
import sys

FILE_NAME = 'iostat.txt'

def getiostat(cmd,num):#get iostat and del the num line in file
    #cmd = 'iostat -x -t'
    (ret) = os.popen3(cmd)
    if(ret[2].readlines()):
        return ret[2]
    result = ret[1].readlines()#read from tty
    if(num != -1):
        del result[num]#remove the num line from result
    for each in result:
        if(each != '\n'):
            print each
    fp = open(FILE_NAME, 'a')
    fp.writelines(result)
    fp.close()
    return 0

if __name__ == '__main__':
    count = 1
    cmd = 'iostat -t'
    print 'Welcome to IO Monitor!'
    if(os.path.isfile(FILE_NAME)):#file exist
        print 'File ' + FILE_NAME + ' exists, whether delete it or not?(y/n)'
        ifdel = raw_input()
        if(ifdel == 'y'):#del
            (ret) = os.popen3('rm -rf ./' + FILE_NAME)
            if(ret[2].read()):
                sys.exit(1)
        elif(ifdel == 'n'):
            pass
        else:
            print 'Input error, exit!'
            sys.exit(1)
    print 'How long do you want to monitor?(Seconds)'
    monitor_time = int(raw_input()) 
    print 'Please input interval(Seconds)'
    interval = int(raw_input())
    print 'Please input command to execute(default:"iostat -t")'
    cmd = raw_input()
    if(interval!=0):
        count = monitor_time/interval
    if(count>0):
        res = getiostat(cmd,-1)#display first line
        time.sleep(interval)
    else:
        print 'count = monitor/interval,must be larger than 1!'
    while(count>0):     
        res = getiostat(cmd,0)#do not display first line
        time.sleep(interval)
        if(res!=0):
            break
        count = count - 1
        print 'Press Ctrl+C to exit!!!\n'
    print 'Exiting....'
     

