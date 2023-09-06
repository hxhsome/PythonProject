"""

"""
import socket
import threading


def socket_server_init():
    socket_server = socket.socket()
    socket_server.bind(("localhost", 8888))
    socket_server.listen(1)

    conn, address = socket_server.accept()
    print(f"客户端地址:{address}")
    data: str = conn.recv(1024).decode("UTF-8")

    print(f"客户端发来的消息是:{data}")

    conn.send(str("我收到了").encode("UTF-8"))

    conn.close()
    socket_server.close()


def socket_client_init():
    socket_client = socket.socket()
    socket_client.connect(("localhost", 8888))
    socket_client.send("您好！".encode("UTF-8"))
    data = socket_client.recv(1024).decode("UTF-8")
    print(f"服务端发来的消息是:{data}")
    socket_client.close()


if __name__ == '__main__':
    threading.Thread(target=socket_server_init).start()
    threading.Thread(target=socket_client_init).start()
