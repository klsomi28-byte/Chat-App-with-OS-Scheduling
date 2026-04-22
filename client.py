import socket
import threading

def receive_messages(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            print("\n" + msg)
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))

    name = input("Enter your name: ")
    client.send(name.encode())

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        receiver = input("Send to (username or 'all'): ")
        priority = input("Priority (lower = higher priority): ")
        message = input("Message: ")

        full_msg = f"{receiver}|{priority}|{message}"
        client.send(full_msg.encode())


start_client()
