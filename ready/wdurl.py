import requests
from bs4 import BeautifulSoup
url = "https://wdurl.ru/index.html"
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
    'Origin': 'https://wdurl.ru',
    'Referer': 'https://wdurl.ru/',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, data=payload, headers=headers, allow_redirects=False)

if response.status_code == 302:
    redirect_url = response.headers.get('Location')
    print(f"Redirigido a: {redirect_url}")
    
    result_page = requests.get(redirect_url, headers=headers)
    soup = BeautifulSoup(result_page.text, 'html.parser')
    
    result_div = soup.find('div', class_='resultLink')
    if result_div and result_div.a:
        short_url = result_div.a['href']
        print(f"URL acortada final: {short_url}")
    else:
        print("No se encontró el enlace corto en la página.")
else:
    print(f"Error en la solicitud: {response.status_code}")
