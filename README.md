#  Network Event Monitoring System (UDP Based)

A network-based event simulation system that uses UDP sockets to send, process, and monitor system events in real-time.

##  Overview

This project simulates a distributed system where multiple clients (nodes) generate events and send them to a central server.

The server processes incoming events, classifies them, filters unnecessary data, and displays a live monitoring dashboard.



##  Key Features

* **UDP Socket Communication**
  Lightweight and fast event transmission using connectionless sockets

* **Distributed Event Simulation**
  Multiple clients simulate system nodes sending logs

* **Packet Loss Simulation**
  Random packet drops to mimic real network conditions

* **Event Classification System**
  Events categorized into:

  * CRITICAL
  * WARNING
  * NORMAL

* 🧹 **Event Filtering**
  Debug logs are ignored to reduce noise

* 📊 **Live Network Dashboard**
  Displays:

  * Connected clients
  * Event statistics



## 🏗️ Project Structure

```
project/
│
├── server.py              # UDP server handling events
├── client.py              # Event generator (simulated nodes)
├── config.py              # Network configuration
├── event_processor.py     # Event classification & filtering
├── event_format.py        # Serialization / deserialization
```

---

## ⚙️ Technologies Used

* Python
* UDP Socket Programming
* JSON (data serialization)



## 🧪 How It Works

1. Client generates random system events
2. Events are serialized and sent via UDP
3. Packet loss is simulated (20%)
4. Server receives and deserializes events
5. Events are filtered and processed
6. Server classifies events and updates stats
7. Dashboard displays real-time system state



## ▶️ How to Run

### 1. Start Server

```bash
python server.py
```

### 2. Start Client

```bash
python client.py
```

> ⚠️ Update the server IP in `client.py` before running
> (`SERVER_IP = "server_ip_here"`)



## 📊 Event Processing Logic

* FAILURE → CRITICAL
* THRESHOLD → WARNING
* INFO → NORMAL
* DEBUG → Filtered out



## 🔍 Example Behavior

* Client sends: CPU usage high
* Server classifies: WARNING
* Dashboard updates in real-time



## 📈 Future Improvements

* GUI-based monitoring dashboard
* TCP + reliability layer
* Data persistence (logs database)
* Alert system (email/notifications)
* Real-time visualization graphs




## ⭐ Note

This project demonstrates practical concepts of distributed systems, unreliable transport (UDP), and real-time event processing.
