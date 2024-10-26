import requests
import json
url_post = "https://dr-api.encurtador.dev/encurtamentos"
payload = {
    'url': 'https://google.com' 
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Origin': 'https://www.urlshort.dev',
    'Referer': 'https://www.urlshort.dev/',
    'Content-Type': 'application/json'
}
response_post = requests.post(url_post, data=json.dumps(payload), headers=headers)
if response_post.status_code in [200, 201]:
    response_json = response_post.json()
    short_url = response_json.get('urlEncurtada')
    if short_url:
        print(f"URL acortada: {short_url}")
    else:
        print("No se pudo encontrar la URL acortada en la respuesta.")
else:
    print(f"Error en la solicitud POST: {response_post.status_code}")
