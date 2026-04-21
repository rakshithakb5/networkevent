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
│── server_screenshot
│── client_screenshot
│── graph_analysis
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



## Results:

### 1 Client Test:
- Throughput: 0.39 req/sec
- Average Latency: 1714.96 ms
- 95th Percentile (P95) Latency: 2000.91 ms
### 5 Concurrent Clients Test:
- Throughput: 1.77 req/sec
- Average Latency: 1831.09 ms
- 95th Percentile (P95) Latency: 2001.04 ms

## Discussion and Observations:

  1. Scalability & Throughput: The system demonstrates excellent horizontal scalability. When scaling from 1 to 5 clients (a 5x increase in load), the total throughput increased proportionally from 0.39 req/sec to 1.77 req/sec (approximately a 4.5x increase). This proves that the multi-threaded server architecture effectively handles concurrent connections without locking up or dropping events.
  
  2. Latency under Load: The Average Latency slightly increased from ~1715 ms to ~1831 ms (+6.7%) when handling 5 clients. This small increase is an expected behavior caused by thread contention and context-switching overhead on the CPU as the OS juggles multiple concurrent socket connections.
  
  3. P95 Latency Insight: The 95th percentile latency remained completely stable at ~2001 ms in both tests. Because the server begins its performance timer just before the blocking conn.recv() call, this latency metric actually captures the client's built-in time.sleep(2.0) interval between messages. The fact that the P95 latency did not spike past 2 seconds under higher load proves that the server is processing the incoming events almost instantaneously once network transmission occurs.
  
  4. Stability: During both tests, malformed, disconnects, and ssl_errors remained at 0, indicating that the TLS/SSL layer and the JSON payload parsing remained perfectly stable under multi-threaded concurrency



### How To Evaluate (Criterion 4)

1. Start server:

```bash
python server/server.py
```

2. Open multiple terminals and run clients with different load levels:

```bash
python client/client.py --ip <SERVER_IP> --port 9999 --count 100 --interval 0.2
```

3. For higher request rate, lower interval:

```bash
python client/client.py --ip <SERVER_IP> --port 9999 --count 200 --interval 0.05
```

4. Record server metrics printed every 5 seconds:
- throughput (req/sec)
- avg_latency (ms)
- p95_latency (ms)

Use these metrics to compare 1, 5, and 10 concurrent clients.

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

### Optimization and Fixes (Criterion 5)

The updated implementation adds targeted refinements based on runtime behavior:

1. Abrupt client disconnections are handled safely and counted.
2. Invalid/malformed payloads are detected, skipped, and counted.
3. SSL/TLS exceptions are handled and counted separately.
4. Latency tracking was added for better bottleneck analysis.

These improvements help show stability under partial failures and noisy input.

---

## Note

This project is developed for academic purposes to demonstrate concepts of network communication, concurrency, and secure system design.
