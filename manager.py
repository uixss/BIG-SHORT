import requests
import json
from bs4 import BeautifulSoup
from requests_toolbelt.multipart.encoder import MultipartEncoder
import sys
def clckru(url_e):
    try:
        shin_agent = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
        }
        shin_gets = requests.get('https://clck.ru/--?url=' + url_e, headers=shin_agent).text
        return shin_gets.strip()
    except Exception as e:
        return ""


def feji_short(url):
    try:
        url_post = "https://feji.io/api/shorted-link/guest-create"
        payload = {'link': url, 'domain_share': 'feji.us'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url_post, data=payload, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('code') == 1:
                return response_json.get('result')
            else:
                return  ""
        else:
            return ""
    except Exception as e:
        return ""


def goo_su_short(url):
    try:
        session = requests.Session()
        response = session.get("https://goo.su/")
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
        url_post = "https://goo.su/frontend-api/convert"
        payload = {"url": url, "is_public": 1}
        headers = {
            "X-CSRF-TOKEN": csrf_token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response_post = session.post(url_post, data=payload, headers=headers)
        if response_post.status_code == 200:
            response_json = response_post.json()
            if response_json.get("successful"):
                return response_json['short_url']
            else:
                return ""
        else:
            return ""
    except Exception as e:
        return ""

def rlu_short(url):
    try:
        url_get = f"https://rlu.ru/index.sema?a=ujax&sa=links_add&del=0&del2=1&nam={url}"
        response = requests.get(url_get)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Error RLU.ru: {response.status_code}"
    except Exception as e:
        return f"Error RLU.ru: {e}"

def shortlink_net_short(url):
    try:
        multipart_data = MultipartEncoder(
            fields={
                'longurl': url,
                'cust': '',
                'message': '',
                'name': '',
                'email': ''
            }
        )
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
            'Content-Type': multipart_data.content_type
        }
        response = requests.post("https://www.shortlink.net/create.php", data=multipart_data, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        short_url = soup.find('input', {'id': 'urlbox'}).get('value')
        return short_url
    except Exception as e:
        return ""

def surl_li_short(url):
    try:
        session = requests.Session()
        response_get = session.get("https://surl.li/es")
        soup = BeautifulSoup(response_get.text, 'html.parser')
        csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']
        url_post = "https://surl.li/pushData"
        payload = {'url': url}
        headers = {'X-CSRF-TOKEN': csrf_token}
        response_post = session.post(url_post, data=payload, headers=headers)
        if response_post.status_code == 200:
            return response_post.json().get('short_url')
        else:
            return ""
    except Exception as e:
        return ""


def encurtador_dev_short(url):
    try:
        url_post = "https://dr-api.encurtador.dev/encurtamentos"
        payload = {'url': url}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
            'Origin': 'https://www.urlshort.dev',
            'Referer': 'https://www.urlshort.dev/',
            'Content-Type': 'application/json'
        }
        response_post = requests.post(url_post, data=json.dumps(payload), headers=headers)
        if response_post.status_code in [200, 201]:
            response_json = response_post.json()
            url = response_json.get('urlEncurtada', 'No se encontró la URL acortada en la respuesta.')
            return "https://"+url
        else:
            return ""
    except Exception as e:
        return ""

def onx_la_short(url):
    try:
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
                return short_url
            else:
                print(" ")
        else:
            return ""
    except Exception as e:
        return ""

def shorturl_ru_short(url):
    try:
        url_post = "https://shorturl.ru/index.html"
        payload = {
            'longUrl': url,
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
            response_get = requests.get(redirect_url)
            if response_get.status_code == 200:
                soup = BeautifulSoup(response_get.text, 'html.parser')
                result_link = soup.find('div', class_='resultLink')
                return result_link.find('a').get('href') if result_link else "No se encontró la URL acortada."
            else:
                return f""
        else:
            return ""
    except Exception as e:
        return ""
def shorturl_at_short(url):

        url_post = "https://www.shorturl.at/shortener.php"
        payload = {
            'u': url 
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
               return short_url.get('value')
            else:
                print(" ")
        else:
            print(f" ")

def wdurl_ru_short(url):
    try:
        url_post = "https://wdurl.ru/index.html"
        payload = {
            'longUrl': url,
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
        response_post = requests.post(url_post, data=payload, headers=headers, allow_redirects=False)
        if response_post.status_code == 302:
            redirect_url = response_post.headers.get('Location')
            response_get = requests.get(redirect_url)
            soup = BeautifulSoup(response_get.text, 'html.parser')
            result_link = soup.find('div', class_='resultLink')
            return result_link.a['href'] if result_link and result_link.a else "No se encontró el enlace corto."
        else:
            return ""
    except Exception as e:
        return ""

def Main():
    url_input = sys.argv[1]

    results = []
    results.append(clckru(url_input))
    results.append(feji_short(url_input))
    results.append(goo_su_short(url_input))
    results.append(rlu_short(url_input))
    results.append(shortlink_net_short(url_input))
    results.append(surl_li_short(url_input))
    results.append(encurtador_dev_short(url_input))
    results.append(onx_la_short(url_input))
    results.append(shorturl_ru_short(url_input))
    results.append(shorturl_at_short(url_input))
    results.append(wdurl_ru_short(url_input))

    return results

if __name__ == "__main__":
    resultado = Main()
    for idx, res in enumerate(resultado, 1):
        print(f"{idx}: {res}")
