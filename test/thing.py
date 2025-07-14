import requests, os
os.system("clear")

response = requests.get("http://127.0.0.1:5000/users")

# Check the status code
print(response.status_code)

# Get the response content as text
print(response.text)

# Or parse JSON (if the response is JSON)
data = response.json()
print(data)