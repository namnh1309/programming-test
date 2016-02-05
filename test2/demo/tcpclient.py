#!/usr/bin/env python2

import socket


def main():
    server_name = '127.0.0.1'
    server_port = 12000
    while True:
        command = raw_input('input-command:')
        if not command:
            continue
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_name, server_port))
        client_socket.send(command)
        modified_sentence = client_socket.recv(1024)
        print 'output-from-server:'
        print modified_sentence
        client_socket.close()


if __name__ == '__main__':
    main()
