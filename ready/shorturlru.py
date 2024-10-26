import requests
from bs4 import BeautifulSoup
url_post = "https://shorturl.ru/index.html"
payload = {
    'longUrl': 'https://google.com',
    'shortUrlDomain': '1',
    'submitted': '1',
    'customUrl': '',  
    'shortUrlPassword': '', 
    'shortUrlExpiryDate': '',  
    'shortUrlUses': '0',  
    'shortUrlType': '0' 
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Origin': 'https://shorturl.ru',
    'Referer': 'https://shorturl.ru/',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response_post = requests.post(url_post, data=payload, headers=headers, allow_redirects=False)

if response_post.status_code == 302:
    redirect_url = response_post.headers.get('Location')
    if redirect_url:
        print(f"Redirigido a: {redirect_url}")
        response_get = requests.get(redirect_url)
        if response_get.status_code == 200:
            soup = BeautifulSoup(response_get.text, 'html.parser')
            result_link = soup.find('div', class_='resultLink')
            if result_link:
                short_url = result_link.find('a').get('href')
                print(f"URL acortada: {short_url}")
            else:
                print("No se pudo encontrar la URL acortada en la página.")
        else:
            print(f"Error en la solicitud GET: {response_get.status_code}")
    else:
        print("No se encontró la URL de redirección.")
else:
    print(f"Error en la solicitud POST: {response_post.status_code}")
