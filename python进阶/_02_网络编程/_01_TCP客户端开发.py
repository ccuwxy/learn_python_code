import socket

# 1 创建客户端套接字对象
# 参数1：ipv4
# 参数2：选择协议（SOCK_STREAM=》tcp）
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 和服务器套接字建立联系
# 参数：元组（两个元素）
# 元素1：服务器ip地址
# 元素2：服务器端口
tcp_client_socket.connect(("192.168.43.187", 8080))

# 发送数据
tcp_client_socket.send("123".encode("utf-8"))
# 传输数据
# 参数：以字节为单位的接收数据的大小
recv_data = tcp_client_socket.recv(1024)
print("收到服务端数据：", recv_data.decode("utf-8"))
# 关闭客户端套接字
tcp_client_socket.close()
