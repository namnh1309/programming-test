#!/usr/bin/env python2

import shlex
import socket
import subprocess


# support command ALLOW_COMMANDS
# if need support more command append command to ALLOW_COMMANDS
ALLOW_COMMANDS = ['ls', 'pwd', 'df', 'touch', 'mkdir']


def main():
    server_port = 12000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print 'The server is ready to receive'
    while True:
        connection_socket, addr = server_socket.accept()
        command_str = connection_socket.recv(1024)
        commands = shlex.split(command_str)
        print command_str
        print commands

        if not commands:
            connection_socket.send('You enter emtpy string!')
            connection_socket.close()
            continue

        if commands[0] not in ALLOW_COMMANDS:
            connection_socket.send('command not support')
            connection_socket.close()
            continue

        try:
            proc = subprocess.Popen(
                commands,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
        except OSError:
            out = ''
            err = "You are trying to execute a non-existent file"
        except ValueError:
            out = ''
            err = "Command that you input error"
        if out:
            result = out
        else:
            result = err
        connection_socket.send(result)
        connection_socket.close()


if __name__ == '__main__':
    main()
