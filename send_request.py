import requests

url = 'http://4.152.170.66:32240'

try:
    response = requests.get(url, timeout=10)  
    if response.status_code == 200:
        print("Request sent successfully")
        print("Response:", response.text)
    else:
        print("Failed to send request. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Failed to connect:", e)
