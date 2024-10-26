import requests
url_post = "https://onx.la/create/shortener/url/public"
payload = {
    'longUrl': 'https://wallstreetbest.com',  
    'token': 'd994f364cdf4c6111.sDNdSUnYwJ0CVU4DqFE5wgZ_xSZRcyKXMRN76wjvrig.5VoSOT62pel2BABO7gd1oW4x_FwFBRfvHHoauGmC2nHGXgg6PKCf7XIxLQ'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Origin': 'https://onx.la',
    'Referer': 'https://onx.la/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}
response_post = requests.post(url_post, data=payload, headers=headers)
if response_post.status_code == 200:
    response_json = response_post.json()
    short_url = response_json.get('urlShort')
    if short_url:
        print(f"URL acortada: {short_url}")
    else:
        print("No se pudo encontrar la URL acortada en la respuesta.")
else:
    print(f"Error en la solicitud POST: {response_post.status_code}")
