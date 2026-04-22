#  Chat Application with OS Scheduling (FCFS & Priority)
Developed a real-time chat system using socket programming and multi-threading, implementing FCFS and Priority Scheduling algorithms to manage message delivery efficiently.

##  Overview
This project is a **real-time multi-client chat system** built using Python sockets.
Unlike traditional chat apps, this system integrates **Operating System scheduling algorithms** to control how messages are delivered.

 Instead of sending messages instantly, the server uses:
* **FCFS (First Come First Serve)**
* **Priority Scheduling**
to simulate **CPU scheduling in real systems**.

##  Key Features
*  Multi-client communication (Client-Server architecture)
*  Private messaging (user-to-user)
*  Broadcast messaging (send to all users)
*  FCFS Scheduling (default queue processing)
*  Priority Scheduling (urgent messages first)
*  Multi-threaded server (handles multiple clients simultaneously)

##  System Design
Client → Server → Message Queue → Scheduler → Delivery

### Mapping OS Concepts:

| OS Concept  | Project Implementation |
| ----------- | ---------------------- |
| Process     | Message                |
| CPU         | Server                 |
| Ready Queue | Message Queue          |
| Scheduling  | Message delivery order |

## Tech Stack
* Python
* Socket Programming
* Threading
* Queue-based Scheduling

##  How to Run
### 1️. Start Server
bash
python server.py

### 2️. Start Clients (multiple terminals)
bash
python client.py

## Usage
### Broadcast Message

Send to: all
Priority: 1
Message: Hello everyone

### Private Message
Send to: sanjana
Priority: 2
Message: Hi sanjana

##  Author
Sanjana K L


