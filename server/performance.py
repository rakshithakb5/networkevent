import time

request_count = 0
start_time = time.time()

def log_performance():
    global request_count
    request_count += 1

    elapsed = time.time() - start_time

    if elapsed > 5:
        print(f"\n📊 Throughput: {request_count/elapsed:.2f} req/sec\n")