import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

tcp_server_socket.bind(("", 8080))

tcp_server_socket.listen(128)

while True:
    client_socket, addr = tcp_server_socket.accept()

    recv_data = client_socket.recv(100000)
    if len(recv_data) == 0:
        break

    print(recv_data.decode())

    response_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "server:py1.0\r\n"
    response_body = "aaa"
    response_data = response_line + response_headers + "\r\n" + response_body

    client_socket.send(response_data.encode())
    client_socket.close()
