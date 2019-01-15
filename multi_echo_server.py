#!/usr/bin/env python3

from multiprocessing import Process
import socket
import time

HOST = ""
PORT = 8081
BUFFER_SIZE = 1024

def handle_echo(conn, addr):

	full_data = b""
	while True:
		data = conn.recv(BUFFER_SIZE)
		if not data: break
		full_data += data

	time.sleep(0.5)
	conn.sendall(full_data)
	#conn.close()


def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((HOST, PORT))
		s.listen(1)

		while True:
			conn, addr = s.accept()
			p = Process(target=handle_echo, args=(conn, addr))
			p.daemon = True
			p.start()
			print("Started process", p)

if __name__ == "__main__":
	main()