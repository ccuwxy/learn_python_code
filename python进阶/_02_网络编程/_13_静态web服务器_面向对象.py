import socket
import time
import multiprocessing


class WebServer(object):
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        self.tcp_server_socket.bind(("", 8080))

        self.tcp_server_socket.listen(128)

    @staticmethod
    def handle_client_request(client_socket):
        recv_data = client_socket.recv(10000000)
        if len(recv_data) == 0:
            return
        recv_data = recv_data.decode()
        print(recv_data)

        path_list = recv_data.split(" ")
        print(path_list)

        request_path = path_list[1]
        response_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "server:py1.0\r\n"

        try:
            file = open("./static" + request_path, "rb")
            file_data = file.read()
            file.close()
        except Exception as e:
            # 文件不存在会报错
            print("异常信息：", e)
            response_line = "HTTP/1.1 404 Not Found\r\n"
            file_data = "404 Not Found".encode()

        response_body = file_data
        response_data = (response_line + response_headers + "\r\n").encode() + response_body
        client_socket.send(response_data)
        time.sleep(1000)
        client_socket.close()

    def start(self):
        while True:
            client_socket, addr = self.tcp_server_socket.accept()
            sub_process = multiprocessing.Process(target=self.handle_client_request, args=(client_socket,))
            sub_process.start()


if __name__ == '__main__':
    web_server = WebServer()
    web_server.start()
