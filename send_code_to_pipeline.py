import os
import requests
import json

# Replace this with your pipeline HTTP endpoint
URL = "https://caaecd16-2026-460e-8501-9e6563a1b2cf-http-us-west2-cf.aws.edgedelta.com"

# Folder containing your code
CODE_DIR = "edgedelta-ai-demo"

def send_file(filepath):
    """Read a file and send its contents as a log to Edge Delta."""
    with open(filepath, "r") as f:
        payload = {
            "type": "code_file",
            "filename": os.path.relpath(filepath, CODE_DIR),
            "contents": f.read()
        }
        try:
            response = requests.post(URL, json=payload)
            if response.status_code == 200:
                print(f"Sent {filepath} successfully")
            else:
                print(f"Failed to send {filepath}: {response.status_code} {response.text}")
        except Exception as e:
            print(f"Error sending {filepath}: {e}")

# Walk through code directory and send all .py files
for root, _, files in os.walk(CODE_DIR):
    for file in files:
        if file.endswith(".py"):
            send_file(os.path.join(root, file))
