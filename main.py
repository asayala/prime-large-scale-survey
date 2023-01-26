import requests
from requests import Response

url = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods'

r: Response = requests.get(url)
print(f"""
DATE = {r.headers['Date']}  
Content-Type = {r.headers['Content-Type']}
""")

print(f"Status Code: {r.status_code}\n") 

if r.status_code == 200: 
    print("The URL is OK")
elif r.status_code == 404:
    print("The URL is not found")
elif r.status_code ==