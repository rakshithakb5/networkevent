from datetime import datetime

def process_event(event):
    if event["type"] == "FAILURE":
        level = "CRITICAL"
    elif event["type"] == "THRESHOLD":
        level = "WARNING"
    else:
        level = "NORMAL"

    return {
        "event": event,
        "level": level,
        "time": datetime.now().strftime("%H:%M:%S")
    }