import socket, sys,os
from multiprocessing import Process


def send_data_binary(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload)
    except socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")


def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")


def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip


def main():
    os.fork()
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    outgoing_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8001))

    remote_host = 'www.google.com'
    port = 80
    buffer_size = 4096
    ip_to_connect = get_remote_ip(remote_host)

    outgoing_socket.connect((ip_to_connect,port))

    server_socket.listen(2)

    client_to_forward, addr = server_socket.accept()

    data_received = client_to_forward.recv(buffer_size)

    print(f"Message received from client: {data_received}")

    send_data_binary(outgoing_socket, data_received)
    data_received = outgoing_socket.recv(buffer_size)

    print(f"Message received from Google: {data_received}")

    send_data_binary(client_to_forward,data_received)
    server_socket.close()
    outgoing_socket.close()

if __name__ == "__main__":
    process = Process(target=main)
    process.start()
    process.join()
    #main()
