#!/usr/bin/python
# -*- coding: utf-8 -*-

def machines_parser(attributes):
    """
    Returns list of remote machines in "user,port@hostname" format.
    """
    remote_machines = []
    for item in attributes:
        if '@' in item:
            if ':' in item:
                remote_machines.append(item.split(':')[0])
            else:
                remote_machines.append(item)
    return remote_machines

def host_user_port_parser(remote_machine):
    """
    Parses and returns host, user and port.
    """
    user_port, host = remote_machine.split('@')
    for separator in ',.:':
        if separator in user_port:
            user, port = user_port.split(separator)
            break
        else:
            user = user_port
            port = 0 # Port 0, really? Why don't make it SSH default, 22? And what if my port will be a string?
    return host, user, port

def single_files(attributes):
    """
    Returns single files from arguments.
    """
    files = []
    for item in attributes:
        if '.' in item and '/' not in item and '@' not in item:
            files.append(item)
    return files

def local_path_parser(attributes):
    """
    Returns local path from arguments.
    """
    for item in attributes:
        if '/' in item and '@' not in item:
            local_path = item
    return local_path

def remote_path_parser(attributes):
    """
    Returns remote path from arguments.
    """
    for item in attributes:
        if ':/' in item: # What if I mistype path, like :\ ?
            remote_path = item.split(':')[1]
            break
        else:
            remote_path = ''
    return remote_path

def secret_parser(attributes):
    """
    Returns password from arguments.
    """
    for item in attributes:
        if '–pass' in item:
            secret = item.split('=')[1].strip("'")
            break
        else:
            secret = ''
    return secret

def rsync_keys_parser(attributes):
    """
    Returns rsync attributes.
    """
    rsync_keys = []
    for item in attributes:
        if item.startswith('-'): # What if I will set all keys in a row, like -Pxasdafdg, not -P -a ...?
            rsync_keys.append(item)
    return rsync_keys
