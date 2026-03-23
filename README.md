# Secure Network Event Monitoring System

## Overview

This project implements a secure networked application using low-level TCP socket programming in Python. The system simulates a distributed environment where multiple clients generate network events and send them to a centralized server.

All communication between clients and the server is secured using SSL/TLS. The server handles multiple concurrent client connections, processes incoming events, and maintains basic performance metrics.

---

## Objectives

* Implement TCP socket communication
* Support multiple concurrent clients
* Design a structured communication protocol
* Ensure secure communication using SSL/TLS
* Evaluate system performance under multiple client loads
* Handle runtime errors and edge cases

---

## System Architecture

```id="2j6j6x"
+-------------+        Secure TCP        +----------------------+
|   Client 1  | -----------------------> |                      |
+-------------+                          |                      |
                                         |                      |
+-------------+        Secure TCP        |        Server        |
|   Client 2  | -----------------------> |   (Multi-threaded)   |
+-------------+                          |                      |
                                         |                      |
+-------------+        Secure TCP        |                      |
|   Client N  | -----------------------> |                      |
+-------------+                          +----------------------+
```

---

## Project Structure

```id="cibsmh"
network-event-monitor/
│
├── server/
│   ├── server.py
│   ├── secure_socket.py
│   ├── event_processor.py
│   ├── performance.py
│   ├── config.py
│
├── client/
│   ├── client.py
│   ├── secure_socket.py
│
├── common/
│   ├── protocol.py
│
├── certs/
│   ├── server.pem
│   ├── server.key
│
├── .gitignore
│   ├── certs/
├
└── README.md
```

---

## Technologies Used

* Python 3
* TCP Socket Programming
* SSL/TLS using OpenSSL
* Multi-threading
* JSON for communication protocol

---

## Security Implementation

Secure communication is implemented using SSL/TLS. The server uses a self -signed certificate and private key generated using OpenSSL to establish encrypted connections with clients. The Python `ssl` module is used to wrap sockets for secure data transmission.

---

## Communication Protocol

The system uses a JSON-based protocol for data exchange.

Example message:

```id="9ezgtd"
{
  "type": "FAILURE",
  "msg": "Node down"
}
```

---

## Features

### Multi-Client Support

The server supports multiple concurrent clients using threading.

### Event Classification

Events are categorized into:

* FAILURE → Critical
* THRESHOLD → Warning
* INFO → Normal

### Secure Communication

All communication is encrypted using SSL/TLS.

### Performance Monitoring

Basic throughput measurement is implemented on the server.

### Error Handling

Handles:

* Client disconnections
* Invalid data
* SSL handshake issues

---

## Setup Instructions

### 1. Clone the Repository

```bash id="hzscvo"
git clone <your-repository-link>
cd network-event-monitor
```

---

### 2. Install Dependencies

No additional Python dependencies are required.
Ensure OpenSSL is installed and available in the system PATH.

### 3. Generate SSL Certificate (OpenSSL)

Run the following command inside the `certs` folder:

```bash id="p1wrro"
openssl req -new -x509 -days 365 -nodes -out server.pem -keyout server.key
```

Provide required details when prompted.

---

### 4. Run the Server

```bash id="f3r4u7"
cd server
python server.py
```

---

### 5. Run Client(s)

```bash id="31rco2"
cd client
python client.py
```

Multiple clients can be run in separate terminals or systems.

---

## Performance Evaluation

| Number of Clients | Observation              |
| ----------------- | ------------------------ |
| 1                 | Stable performance       |
| 5                 | Moderate load handling   |
| 10                | Increased resource usage |

---

## Limitations

* Uses self-signed SSL certificates
* No graphical user interface
* Basic performance analysis only

---

## Future Enhancements

* Web-based dashboard
* Database integration
* Advanced performance metrics
* Load balancing

---

## Evaluation Mapping

| Requirement            | Implementation Details     |
| ---------------------- | -------------------------- |
| Socket Programming     | TCP sockets used           |
| Concurrency            | Multi-threading            |
| Security               | SSL/TLS using OpenSSL      |
| Protocol Design        | JSON-based                 |
| Performance Evaluation | Throughput measurement     |
| Optimization           | Error handling implemented |

---

## Note

This project is developed for academic purposes to demonstrate concepts of network communication, concurrency, and secure system design.
