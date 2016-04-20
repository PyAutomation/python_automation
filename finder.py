#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

def find_remote_files(remote_path, type, ssh): # Can it be a function like remote_command_runner?
    """
    Finds all files or directories on remote machine, according to given attributes.
    """
    (ssh_in, ssh_out, ssh_err) = ssh.exec_command("find %s -name \"*\" -type %s" % (remote_path, type))
    files = []
    for file in ssh_out.readlines():
        files.append(file.rstrip())
    return files


def find_local_files(local_path, type): # Can it be a function like local_command_runner, a kind of utility package, with different args?
    """
    Finds all files or directories on local machine, according to given attributes.
    """
    local_out = commands.getoutput("find %s -name \"*\" -type %s" % (local_path, type))
    files = []
    for file in local_out.split("\n"):
        files.append(file)
    return files

def find_local_file(local_path, file): # Can it be a function like local_command_runner, a kind of utility package, with different args?
    """
    Finds all single files on local machine, according to given attributes.
    """
    file = commands.getoutput("find %s -name \"%s\" -type f" % (local_path, file))
    return file

def get_remote_md5(file, ssh): # Can it be a function like remote_command_runner, a kind of utility package, with different args?
    """
    Returns hash from remote files.
    """
    md5sum = ''
    (ssh_in, ssh_out, ssh_err) = ssh.exec_command("md5sum %s" % file)
    for line in ssh_out.readlines():
        md5sum = line.split(" ")[0]
    return md5sum

def get_local_md5(file): # Can it be a function like local_command_runner, a kind of utility package, with different args?
    """
    Returns hash from local files.
    """
    local_out = commands.getoutput("md5sum %s" % file)
    return local_out.split(" ")[0]

def compare_files(local_files, remote_files, ssh): # BTW, we can subtract tuples: (1, 3) - (1, 4 6) -> (3)
    """
    Compares hashes and returns list of files, needed to be copied.
    """
    transfer_files = []
    for file in local_files:
        if file in remote_files:
            if get_local_md5(file) == get_remote_md5(file, ssh):
                pass
            else:
                transfer_files.append(file)
        else:
            transfer_files.append(file)
    return transfer_files
