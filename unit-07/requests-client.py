import requests

url = "http://localhost:5000/api/data"
payload = {
    "name": "Mario",
    "age": 30,
    "occupation": "plumber"
}

# The 'json' parameter automatically sets Content-Type to application/json
response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")
