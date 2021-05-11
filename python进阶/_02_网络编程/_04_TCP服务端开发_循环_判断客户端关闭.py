import socket

# 参数1：ipv4
# 参数2：tcp协议
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 端口复用作用：一单服务端关闭 端口立刻释放
# 参数1：socket选项列表（SOL）
# 参数2：地址复用
# 参数3：True：开启选项 False：（默认）不开启
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 参数：元组(两个元素)IP地址，端口号

tcp_server_socket.bind(("", 8080))


# 参数：最大监听个数（排队处理最大等待数量）
# tcp_server_socket从主动套接字变成了被动套接字
tcp_server_socket.listen(128)

# <返回值>是元组（和客户端进行通讯的socket，客户端的地址信息）
# 拆包语法
client_socket, client_addr = tcp_server_socket.accept()

while True:
    # 对二进制进行解码
    client_data = client_socket.recv(1024)
    if len(client_data) == 0:
        break
    client_data = client_data.decode("utf-8")
    print("收到客户端数据：", client_data)

    send_data = "121212".encode("utf-8")
    client_socket.send(send_data)

client_socket.close()
tcp_server_socket.close()




