#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import paramiko

def ip_check(hosts):
    """
    Returns valid ip addresses.
    """
    valid_hosts = []
    for i in hosts:
        command = os.system('ping -c 1 '+i.split('@')[1]+' > /dev/null')
        if command == 0:
            valid_hosts.append(i)
    return valid_hosts


def open_sshclient(host, user, port, secret):
    """
    Opens ssh session using paramiko.
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

def copy_file(rsync_keys, file, host, remote_path):
    """
    Makes all needed operations according to given attributes with rsync.
    """
    print('rsync ' + rsync_keys + ' ' + file + ' ' + host + ':' + remote_path)
    os.system('rsync '+rsync_keys+' '+file+' '+host+':'+remote_path)