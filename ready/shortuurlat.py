import requests
from bs4 import BeautifulSoup
url_post = "https://www.shorturl.at/shortener.php"
payload = {
    'u': 'https://gooagle.com'  
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Origin': 'https://www.shorturl.at',
    'Referer': 'https://www.shorturl.at/',
    'Content-Type': 'application/x-www-form-urlencoded'
}
response_post = requests.post(url_post, data=payload, headers=headers)
if response_post.status_code == 200:
    soup = BeautifulSoup(response_post.text, 'html.parser')
    short_url = soup.find('input', {'id': 'shortenurl'}) 
    if short_url:
        print(f"URL acortada: {short_url.get('value')}")
    else:
        print("No se pudo encontrar la URL acortada en la página.")
else:
    print(f"Error en la solicitud POST: {response_post.status_code}")
