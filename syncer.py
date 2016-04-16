#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import paramiko

# def argument_check():
#     #will check if arguments are ok

def ip_check():
    """
    Parsing attributes for given hosts,
    then checking if hosts are up
    and then calling path_check function with working hosts.
    """
    hosts = []
    valid_hosts = []
    for item in sys.argv:
        if '@' in item:
            hosts.append(item)
    for i in hosts:
        host = i.split('@')[1].split(':')[0]
        command = os.system('ping -c 1 '+host+' &> /dev/null')
        if command == 0:
            valid_hosts.append(i)
    if valid_hosts:
        path_check(valid_hosts)

def path_check(hosts):
    """
    Parsing username, port, host and path,
    and then opening ssh session using paramiko
    for each given host
    """
    for item in sys.argv:
        if '–pass' in item:
            secret = item.split('=')[1].strip("'")
            break
        else:
            secret = ''
    for i in hosts:
        user_port, host_path = i.split('@')
        host, path = host_path.split(':')
        for separator in ',.:':
            if separator in user_port:
                user, port = user_port.split(separator)
                break
            else:
                user = user_port
                port = 0
        ssh = open_sshclient(host, user, port, secret)
        ssh.exec_command('mkdir -p '+path)
        ssh.close()
    copy_file(hosts)

def open_sshclient(host, user, port=0, secret=''):
    """
    Opening ssh session using paramiko.
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    if secret and port:
        ssh_client.connect(hostname=host, username=user, password=secret, port=port)
    elif secret and port==0:
        ssh_client.connect(hostname=host, username=user, password=secret)
    elif not secret and port:
        ssh_client.connect(hostname=host, username=user, port=port)
    else:
        ssh_client.connect(hostname=host, username=user)
    return ssh_client


def copy_file(hosts):
    """
    Making all needed operations according to given attributes with rsync.
    """
    arguments = []
    for item in sys.argv[1:]:
        if '@' not in item and '–pass' not in item:
            arguments.append(item)
    for item in hosts:
        os.system('rsync '+' '.join(arguments)+' '+item)




ip_check()