#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import paramiko

# def argument_check():
#     #will check if arguments are ok

def ip_check():
    hosts = []
    valid_hosts = []
    for item in sys.argv:
        if '@' in item:
            hosts.append(item)
    for i in hosts:
        host = i.split('@')[1].split(':')[0]
        command = os.system('ping -c 1 '+host)
        if command == 0:
            valid_hosts.append(i)
    if valid_hosts:
        path_check(valid_hosts)

def path_check(hosts):
    for item in sys.argv:
        if '–pass' in item:
            secret = item.split('=')[1].strip("'")
            break
        else:
            secret = ''
    counter = 1
    for i in hosts:
        user_port, host_path = i.split('@')
        host, path = host_path.split(':')
        for separator in ',.:':
            if separator in user_port:
                user, port = user_port.split(separator)
                break
            else:
                user = user_port
                port = ''
        print(str(counter)+'. Username: '+user+', Port: '+port+' , ip: '+host+', Remote path: '+path)
        counter += 1
    if secret:
        print('Password: '+secret)
    # client = paramiko.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # client.connect(hostname=host, username=user, password=secret, port=port)
    # stdin, stdout, stderr = client.exec_command('mkdir -p '+path)


#
# def copy_file():
#     arguments = ' '.join(sys.argv[1:])
#     os.system('rsync '+arguments)
ip_check()