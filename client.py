#!/usr/bin/python3

import socket, sys

def creat_tcp_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    print(f"IP address of {host} is {remote_ip}")
    return remote_ip

def send_data(serversocket, payload):
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("Send failed.")
        sys.exit()
    print("Payload send successfully")

def main():
    try:
        host = 'www.google.com'
        port = 80
        payload = f"GET / HTTP/1.0\nHOST: {host}\r\n\n"
        buffer_size = 4096

        s = creat_tcp_socket()

        remote_ip = get_remote_ip(host)
        s.connect((remote_ip, port))
        print(f"Socket connected to {host} on IP {remote_ip}.")

        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data = full_data + data

        print(full_data)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()


