import time
import threading
import matplotlib.pyplot as plt


request_count = 0
malformed_count = 0
disconnect_count = 0
ssl_error_count = 0
latencies_ms = []

time_history = []
throughput_history = []

start_time = time.time()
last_report = start_time
lock = threading.Lock()


def _p95(values):
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = int(0.95 * (len(ordered) - 1))
    return ordered[idx]


def log_performance(latency_ms=None):
    global request_count, last_report

    now = time.time()
    with lock:
        request_count += 1
        if latency_ms is not None:
            latencies_ms.append(float(latency_ms))

        elapsed = now - start_time
        if now - last_report >= 5:
            throughput = request_count / elapsed if elapsed > 0 else 0.0
            avg_latency = (sum(latencies_ms) / len(latencies_ms)) if latencies_ms else 0.0
            p95_latency = _p95(latencies_ms)

            print(
                "\n📊 Performance"
                f" | throughput={throughput:.2f} req/sec"
                f" | avg_latency={avg_latency:.2f} ms"
                f" | p95_latency={p95_latency:.2f} ms"
                f" | malformed={malformed_count}"
                f" | disconnects={disconnect_count}"
                f" | ssl_errors={ssl_error_count}\n"
            )
            
            # Store history for the graph
            time_history.append(elapsed)
            throughput_history.append(throughput)
            
            last_report = now


def show_final_graph():
    """Generates the graph using matplotlib when the server stops."""
    if not time_history:
        print("Not enough data collected to plot a graph yet.")
        return
        
    plt.figure(figsize=(10, 5))
    plt.plot(time_history, throughput_history, marker='o', linestyle='-', color='b')
    plt.xlabel("Time Running (seconds)")
    plt.ylabel("Throughput (req/sec)")
    plt.title("Server Throughput Over Time")
    plt.grid(True)
    plt.show()


def log_malformed():
    global malformed_count
    with lock:
        malformed_count += 1


def log_disconnect():
    global disconnect_count
    with lock:
        disconnect_count += 1


def log_ssl_error():
    global ssl_error_count
    with lock:
        ssl_error_count += 1


class PerformanceMonitor:
    def _init_(self, interval=2):
        self.request_count = 0
        self.start_time = time.time()
        self.interval = interval

        self.time_data = []
        self.throughput_data = []

    def log_request(self):
        """Call this every time an event/request is processed"""
        self.request_count += 1

        elapsed = time.time() - self.start_time

        if elapsed >= self.interval:
            throughput = self.request_count / elapsed

            print(f"[PERFORMANCE] Time: {elapsed:.2f}s | Throughput: {throughput:.2f} req/sec")

            # Store data for graph
            self.time_data.append(elapsed)
            self.throughput_data.append(throughput)

            # Reset counters
            self.request_count = 0
            self.start_time = time.time()

    def plot_graph(self):
        """Plot throughput vs time graph"""
        if not self.time_data:
            print("No data to plot!")
            return

        plt.figure()
        plt.plot(self.time_data, self.throughput_data)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Throughput (req/sec)")
        plt.title("System Performance Analysis")
        plt.grid()

        plt.show()
