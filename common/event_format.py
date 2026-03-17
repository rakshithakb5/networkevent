import json

def create_event(event_type, message, node_id):
    return {
        "node_id": node_id,
        "type": event_type,
        "message": message
    }

def serialize_event(event):
    return json.dumps(event).encode()

def deserialize_event(data):
    return json.loads(data.decode())