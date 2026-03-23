# Secure Network Event Monitoring System

## Overview

This project presents a secure networked application developed using low-level socket programming in Python. The system simulates a distributed environment where multiple client nodes generate network-related events and transmit them to a centralized server.

All communication between clients and the server is carried out over a secure TCP connection using SSL/TLS. The server is responsible for handling concurrent client connections, processing incoming data, classifying events, and maintaining basic performance metrics.

---

## Objectives

* Implement network communication using TCP sockets
* Support multiple concurrent client connections
* Design a structured communication protocol
* Ensure secure data transmission using SSL/TLS
* Evaluate system performance under varying loads
* Handle runtime errors and edge cases effectively

---

## System Architecture

```
+-------------+        Secure TCP        +----------------------+
|   Client 1  | -----------------------> |                      |
+-------------+                         |                      |
                                       |                      |
+-------------+        Secure TCP       |        Server        |
|   Client 2  | ----------------------->|   (Multi-threaded)   |
+-------------+                         |                      |
                                       |                      |
+-------------+        Secure TCP       |                      |
|   Client N  | ----------------------->|                      |
+-------------+                         +----------------------+
```

---

## Project Structure

```
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
│   ├── generate_cert.py
│
└── README.md
```

---

## Technologies Used

* Python 3
* TCP Socket Programming
* SSL/TLS for secure communication
* Threading for concurrency
* JSON for message formatting

---

## Security Implementation

The system uses SSL/TLS to encrypt communication between clients and the server. A self-signed certificate is generated using the `cryptography` library. The server wraps its socket using an SSL context, and the client establishes a secure connection using the same protocol.

---

## Communication Protocol

The system uses a lightweight JSON-based protocol for data exchange.

Example message:

```
{
  "type": "FAILURE",
  "msg": "Node down"
}
```

---

## Features

### Multi-Client Support

The server handles multiple clients simultaneously using threading. Each client connection is processed independently.

### Event Classification

Incoming events are categorized into different levels:

* FAILURE → Critical
* THRESHOLD → Warning
* INFO → Normal

### Secure Communication

All data transmitted between client and server is encrypted using SSL.

### Performance Monitoring

The server tracks request handling rate (throughput) over time.

### Error Handling

The system accounts for:

* Client disconnections
* Invalid or malformed data
* SSL handshake failures

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <your-repository-link>
cd network-event-monitor
```

---

### 2. Install Dependencies

```
pip install cryptography
```

---

### 3. Generate SSL Certificate

```
cd certs
python generate_cert.py
```

---

### 4. Run the Server

```
cd ../server
python server.py
```

---

### 5. Run Client(s)

```
cd ../client
python client.py
```

Multiple clients can be run in separate terminals to simulate concurrent nodes.

---

## Performance Evaluation

| Number of Clients | Observation                          |
| ----------------- | ------------------------------------ |
| 1                 | Low load, stable response            |
| 5                 | Moderate load, consistent throughput |
| 10                | Increased load, higher CPU usage     |

---

## Limitations

* Uses self-signed certificates instead of trusted certificate authorities
* Command-line interface only (no graphical dashboard)
* Basic performance metrics without detailed analysis

---

## Future Enhancements

* Web-based monitoring dashboard
* Persistent storage using a database
* Retry mechanism for failed transmissions
* Load balancing for improved scalability

---

## Evaluation Mapping

| Requirement             | Implementation Details             |
| ----------------------- | ---------------------------------- |
| Socket Programming      | TCP sockets used                   |
| Concurrency             | Multi-threaded server              |
| Security                | SSL/TLS encryption implemented     |
| Protocol Design         | JSON-based communication           |
| Performance Evaluation  | Throughput measurement             |
| Optimization & Handling | Error handling and stability fixes |

---

## Author

Rakshitha K.B

---

## Note

This project is developed as part of coursework to demonstrate practical understanding of network programming, secure communication, and system design principles.
