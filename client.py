#!/usr/bin/env python3

import socket

HOST = "www.google.com"
PORT = 80

BUFFER_SIZE = 1024

PAYLOAD = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def connect_socket(addr_tup):

	(family, socktype, proto, canonname, sockaddr) = addr_tup

	try:
		s = socket.socket(family, socktype, proto)
		s.connect(sockaddr)
		s.sendall(PAYLOAD.encode())

		full_data = b""
		while True:
			data = s.recv(BUFFER_SIZE)
			if not data: # if data = None
				break
			full_data += data

		print(full_data)

	except e:
		print(e)
		pass
	finally:
		s.close()

def main():

	addr_info = socket.getaddrinfo(HOST, PORT, socket.AF_INET,
									proto=socket.SOL_TCP)
	for addr_tup in addr_info:
		connect_socket(addr_tup)
		break

if __name__ == "__main__":
	main()
