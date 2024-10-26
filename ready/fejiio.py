import requests
url_post = "https://feji.io/api/shorted-link/guest-create"
payload = {
    'link': 'https://google.com',
    'domain_share': 'feji.us' 
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Origin': 'https://feji.io',
    'Referer': 'https://feji.io/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}
response_post = requests.post(url_post, data=payload, headers=headers)
if response_post.status_code == 200:
    response_json = response_post.json()
    if response_json.get('code') == 1:
        short_url = response_json.get('result')
        print(f"URL acortada: {short_url}")
    else:
        print(f"Error en la respuesta: {response_json.get('msg')}")
else:
    print(f"Error en la solicitud POST: {response_post.status_code}")
