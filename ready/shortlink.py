import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bs4 import BeautifulSoup
url = "https://www.shortlink.net/create.php"
multipart_data = MultipartEncoder(
    fields={
        'longurl': 'https://google.com', 
        'cust': '',
        'message': '', 
        'name': '',  
        'email': '' 
    }
)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Origin': 'https://www.shortlink.net',
    'Referer': 'https://www.shortlink.net/',
    'Content-Type': multipart_data.content_type 
}
response = requests.post(url, data=multipart_data, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    short_url = soup.find('input', {'id': 'urlbox'}).get('value')
    print(f"URL acortada: {short_url}")
else:
    print(f"Error en la solicitud: {response.status_code}")
