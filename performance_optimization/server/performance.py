import time
import threading


request_count = 0
malformed_count = 0
disconnect_count = 0
ssl_error_count = 0
latencies_ms = []

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
            last_report = now


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
