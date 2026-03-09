import urllib.request
import urllib.error
import json

url = "http://localhost:5000/api/data"
payload = {
    "name": "Mario",
    "age": 30,
    "occupation": "plumber"
}

# Convert dictionary to a JSON string and then to bytes
data = json.dumps(payload).encode('utf-8')

# Create the request object and specify the header
req = urllib.request.Request(url, data=data, method='POST')
req.add_header('Content-Type', 'application/json')

try:
    # Send the request
    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        body = response.read().decode('utf-8')
        print(f"Status Code: {status_code}")
        print(f"Response: {body}")
except urllib.error.URLError as e:
    print(f"Connection Error: {e}")
