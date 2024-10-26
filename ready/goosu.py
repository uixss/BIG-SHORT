import requests
from bs4 import BeautifulSoup
url_token = "https://goo.su/"
session = requests.Session()
response = session.get(url_token)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
print(f"Token CSRF: {csrf_token}")
url_post = "https://goo.su/frontend-api/convert"
payload = {
    "url": "https://google.com",
    "alias": "",
    "is_public": 1,
    "password": ""
}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-CSRF-TOKEN": csrf_token,  
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Origin": "https://goo.su",
    "Referer": "https://goo.su/"
}

response_post = session.post(url_post, data=payload, headers=headers)

if response_post.status_code == 200:
    response_json = response_post.json()
    print("Respuesta:", response_json)
    if response_json.get("successful"):
        short_url = response_json['short_url'] 
        long_url = response_json['link']['long_url']  
        print(f"URL acortada: {short_url}")
        print(f"URL original: {long_url}")
    else:
        print("Error en la respuesta:", response_json.get("message", ""))
else:
    print(f"Error en la solicitud: {response_post.status_code}")
