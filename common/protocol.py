import json

def encode_message(event):
    return json.dumps(event).encode()

def decode_message(data):
    return json.loads(data.decode())