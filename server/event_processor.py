from datetime import datetime

def classify_event(event):
    if event["type"] == "FAILURE":
        return "CRITICAL"
    elif event["type"] == "THRESHOLD":
        return "WARNING"
    elif event["type"] == "INFO":
        return "NORMAL"
    return "UNKNOWN"

def filter_event(event):
    # Ignore debug logs
    return event["type"] != "DEBUG"

def process_event(event):
    event["class"] = classify_event(event)
    event["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return event