import socket
import sys
import os
'''
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
clientsocket.connect((host, port))
print('Connected to server successfully')


msg = clientsocket.recv(1024)
print(msg.decode('utf-8'))
clientsocket.send('A message comes from client.'.encode('utf-8'))
clientsocket.close()

while True:
	msg = input('>>>')
	if not msg:
		break
	clientsocket.sendall(msg.encode())
	msg = clientsocket.recv(1024).decode()
	print('Message Received:' + msg)

clientsocket.close()
'''
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
#tcp_client_socket.bind(("", 8080))
# 连接IP地址和端口
tcp_client_socket.connect(("127.0.0.1", 8080))
file_name = input("请输入要下载的文件：\n")
file_name = file_name.replace('\\', '/')
file_name_withoutpath = file_name.split('/')[-1]
# 文件名编码
tcp_client_socket.send(file_name.encode())
try:
	# 文件传输
	with open("C:/Users/win10/Desktop/" + file_name_withoutpath, "wb") as file:
		while True:
			# 接收数据
			file_data = tcp_client_socket.recv(1024)
			# 数据长度不为0写入文件
			if file_data:
				file.write(file_data)
			# 数据长度为0表示下载完成
			else:
				break
			# 下载出现异常时捕获异常
except Exception as e:
	print("下载异常", e)
# 无异常则下载成功
else:
	print(file_name, "下载成功")
# 关闭客户端
tcp_client_socket.close()