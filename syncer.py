#!/usr/bin/python
import os
import sys
import paramiko

def argument_check():
    #will check if arguments are ok

def ip_check():
    for item in sys.argv:
        if '@' in item:
            ippath = item.split('@')[1]
            ip = ippath.split(':')[0]
            command = os.system('ping -c 3'+' '+ip)
            if command == 0:
                path_check()
            else:
                print('no')

def path_check():
    for item in sys.argv:
        if '@' in item:
            ippath = item.split('@')[1]
            host = ippath.split(':')[0]
            user_port = item.split('@')[0]
            if ',' in user_port:
                user = user_port.split(',')[0]
                port = user_port.split(',')[1]
            elif '.' in user_port:
                user = user_port.split('.')[0]
                port = user_port.split('.')[1]
            elif ':' in user_port:
                user = user_port.split(':')[0]
                port = user_port.split(':')[1]
            else:
                user = user_port
        if '–pass' in item:
            secret = item.split('=')[1].strip("'")
            #then paramiko magic
            #then copy_file() will run if ok

def copy_file():
    if sys.argv:
        arguments = ' '.join(sys.argv[1:])
        os.system('rsync' + ' ' + arguments)
    else:
        print('Wrong arguments!')

ip_check()
