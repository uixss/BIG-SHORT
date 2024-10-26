import requests
url_get = "https://rlu.ru/index.sema?a=ujax&sa=links_add&del=0&del2=1&nam=https%3A%2F%2Fgaaoogle.com"
response = requests.get(url_get)
if response.status_code == 200:
    short_url = response.text.strip() 
    print(f"URL acortada: {short_url}")
else:
    print(f"Error en la solicitud GET: {response.status_code}")
