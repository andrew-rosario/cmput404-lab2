import socket, sys


def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")


def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s


def main():
    try:
        host_server = 'localhost'
        port = 8001
        message_to_send = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
        buffer_size = 4096


        s = create_tcp_socket()

        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        s.connect((host_server, port))

        send_data(s, message_to_send)
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()


if __name__ == "__main__":
    main()
