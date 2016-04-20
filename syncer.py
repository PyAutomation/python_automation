#!/usr/bin/python
# -*- coding: utf-8 -*-
import parser
import finder
import connect
import sys

# Can we add __name__ check? The script will fire when I'll try to import it :(
# Can we also add check for OS type? No rsync exists on Windows, I want to have that message.

# Use moduled structure, I'll explain it during the classes
hosts = parser.machines_parser(sys.argv)
valid_hosts = connect.ip_check(hosts)
local_path = parser.local_path_parser(sys.argv)
remote_path = parser.remote_path_parser(sys.argv)
rsync_keys = parser.rsync_keys_parser(sys.argv)
if not remote_path:
    remote_path = local_path
local_files = finder.find_local_files(local_path, 'f')
local_directories = finder.find_local_files(local_path, 'd')
single_files = parser.single_files(sys.argv)
single_file_path = []
for file in single_files:
    single_file_path.append(finder.find_local_file(local_path, file))
for file in single_file_path:
    if file not in local_files:
        local_files.append(file)
for valid_host in valid_hosts:
    host, user, port = parser.host_user_port_parser(valid_host)
    secret = parser.secret_parser(sys.argv)
    ssh = connect.open_sshclient(host, user, port, secret)
    remote_files = finder.find_remote_files(remote_path, 'f', ssh)
    transfer_files = finder.compare_files(local_files, remote_files, ssh)
    ssh.exec_command('mkdir -p '+remote_path)
    for file in transfer_files:
        connect.copy_file(' '.join(rsync_keys), file, valid_host, remote_path)
    ssh.close()
