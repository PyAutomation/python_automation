#!/usr/bin/python
import os
import sys
import paramiko

def argument_check():
    #will check if arguments are ok

def ip_check():
    for item in sys.argv:
        if '@' in item:
            ip_path = item.split('@')[1]
            host = ip_path.split(':')[0]
            command = os.system('ping -c 3 '+host)
            if command == 0:
                path_check()
            else:
                print('Remote host is down')

def path_check():
    for item in sys.argv:
        if '@' in item:
            user_port, host_path = item.split('@')
            host, path = host_path.split(':')
            for separator in ',.:':
                if separator in user_port:
                    user, port = user_port.split(separator)
                    break
                else:
                    user = user_port
                    port = ''
        if '–pass' in item:
            secret = item.split('=')[1].strip("'")
        else:
            secret = ''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command('mkdir -p '+path)



def copy_file():
    arguments = ' '.join(sys.argv[1:])
    os.system('rsync '+arguments)