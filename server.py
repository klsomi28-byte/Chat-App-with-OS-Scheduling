import socket
import threading
import time

# ===============================
# GLOBAL DATA
# ===============================

clients = []
client_names = {}

message_queue = []

# Change to "PRIORITY" to enable priority scheduling
SCHEDULING_MODE = "FCFS"


# ===============================
# HANDLE CLIENT
# ===============================
def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()

            # Format: receiver|priority|message
            receiver, priority, message = msg.split("|")

            data = {
                "sender": client,
                "receiver": receiver,
                "priority": int(priority),
                "message": message
            }

            message_queue.append(data)

        except:
            print("Client disconnected")
            if client in clients:
                clients.remove(client)
            break


# ===============================
# SCHEDULER (CORE LOGIC)
# ===============================
def scheduler():
    while True:
        if message_queue:

            # Apply PRIORITY scheduling if enabled
            if SCHEDULING_MODE == "PRIORITY":
                message_queue.sort(key=lambda x: x["priority"])

            data = message_queue.pop(0)

            sender = data["sender"]
            receiver_name = data["receiver"]
            message = data["message"]

            sender_name = client_names.get(sender, "Unknown")

            formatted_msg = f"{sender_name}: {message}"

            # ===============================
            # BROADCAST MESSAGE
            # ===============================
            if receiver_name.lower() == "all":
                for client in clients:
                    try:
                        if client != sender:  # avoid sending to self
                            client.send(formatted_msg.encode())
                    except:
                        pass

            # ===============================
            # PRIVATE MESSAGE
            # ===============================
            else:
                for client, name in client_names.items():
                    if name == receiver_name:
                        try:
                            client.send(formatted_msg.encode())
                        except:
                            pass

        time.sleep(1)


# ===============================
# MAIN SERVER
# ===============================
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen()

    print("🚀 Server started on port 5000...")

    # Start scheduler thread
    threading.Thread(target=scheduler, daemon=True).start()

    while True:
        client, addr = server.accept()
        print(f"✅ Connected: {addr}")

        # Receive client name
        name = client.recv(1024).decode()
        client_names[client] = name
        clients.append(client)

        print(f"👤 User '{name}' joined")

        # Start client thread
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    start_server()
