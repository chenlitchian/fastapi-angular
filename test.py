import requests
from datetime import datetime
import os
pid = os.getpid()

url = "http://0.0.0.0:8000/items/"  # Replace with the actual API URL

# Make 10000 GET requests in a loop
for i in range(10000):
    response = requests.get(url+str(i))
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print(f"{pid}: Request {i + 1} complete {response.json()} with status code {response.status_code} at {datetime.now()}")

        # Process the data as needed
    else:
        print(f"Request {i + 1} failed with status code {response.status_code}")

print("All requests completed.")