import requests
from bs4 import BeautifulSoup
url_get = "https://surl.li/es"
session = requests.Session()
response_get = session.get(url_get)
if response_get.status_code == 200:
    soup = BeautifulSoup(response_get.text, 'html.parser')
    csrf_meta_tag = soup.find('meta', {'name': 'csrf-token'})
    if csrf_meta_tag:
        csrf_token = csrf_meta_tag['content']
        print(f"Token CSRF encontrado: {csrf_token}")
        url_post = "https://surl.li/pushData"
        payload = {
            'url': 'https://google.com', 
            'g-recaptcha-response': '03AFcWeA5s68wDmeh_73egR0kTd1FHM1IGs8CeaheNNodpMAR2nRg9z2HHhto58xYsPQUMSNvSmgdXfniFQqVvBrEVoWk6WiJrjh1lRhv6oNM6QyRrwUd17PJQNn53xDi9UKGrInlp4BaDCNcMAQCkmivqsisH9qHBo0pEYj6nxfMxz1H3MCM0gW_P-gmuuuQrCOFJkAEoduEgvMlWr-GzO1-VbE4AtIf-_Bc8VGr4YRBlFNin-far8ceHzI6TAKRGnHLf0z5awYdPr_3sbeMW7AtgXzTW5G5WIQC0YNlRlsj0RVsaiSlARRP8Lnc84T7xrxrmRDmNn3JlVcABogXxOF6G0exbj2wXsl9lLCyERZNZtZKMAcR4tYYrr-d3y7Z3Eg2uNfSKtmJQe3PKOsz4iiiwZbJ-OOZC_rm4pE6a53cZ5da3quRNRwTu-aLt_0dMdAxxWDCXAn0TuExGK4DH9zSrYwIHX88R4DTClblozW-08ywDeHeBlEwTL-fd1LZbfcMwO3gQ03sN-SM_S_AVPqp3d-usWsOleJeK7qAEcwizrvRb1mAmUuRwj8NvSYcRdeV0j1QYXmpbvhkrBJM1Yld0WWhibDa45wtYlajI8TVuVTGRHYl_tCVxQAkZx4gPiim82ZplbrE3NmYwPpM64yWjK1d8UncLvTgvk-qstWjXpRU8vxba-IqIZKPRYRP5_NxskDpNwySGv5U9PkfTaaFQUbnOo8WtsVK382MY6SpZFgw7qoCR53kpJtwOTFIEsDoO2KNmShDqUDrGM28n6TZJdo1rvpvJmUs9wqMHoVoGQUomSXnzojSXMWySUbFr5EYNujDmiM8Bt0Hpg84PhrBRsdcCKCYv_l07lXWwv96s1C9y2xYAnK5bgTm0XjffGkTGR6iutVbb_-OcdvOQImXsI0Im5YkfgXpa68_t-B8PukIVxvfEVSef1JLoPlvjBi_HUjSrEy4QSkQHwGC6YZsC5BxqMK-2vnDw-AvhWKkbDWbcLBI1Eo9HyZGYqgdG_g57kl5uVB3BnyRYKaMk-OV6K4wCRpmgAU8fi9H74FPLpJCW3et5uwYTI54EBuUy-0Co7IoLkFEp7z-XAqnbQJ0LAAVuR3k0D-0nY3OJy7gLgEz4t1onm-UrdRNzs2ckJGslxt2HDXtvmb5y008Ij4-p9D6E7wa0V4HMtDN1E6mjAZN4GWpjIUHEypCL8NaGnFdKLVdfzEg3Cpyllml3qkIHI_QqEQWcZykChxkSwVihMh5yuRlsYF4tZAcnHtT59ccfJxgRQ7Ux2p7oS6-HmZNQvwGN6g3fC__fq9VFoE5-wPlYg21YKtZ_GjE_nIvt4HNN5-f3OujPBAHhDbT3i4BOkirDHStIk4Ipjr_e1KWurxtnY3x80DtPqy2T7PnFciRkbnbLNGwqaG7rMtQqICjILiIiYJFd0qegXnscBfYC19Zd0TfKWKqdK8ddINYyuAPQhfVFSpTC6a6c97BVuYE0Vs1f32-KruAJr5zCSU4LwC7V4dD4Oswg8IzyjJ-NF4U7ZMmT9iPkW6d9MHtpyVCVF0uK015mcnknuGpi42F0c1I7NkLiLBhQCk9WuCwXTZxCj0ldr97YrmoEtmX95KiPP5DLDm9IRlQzk_vN8RxupzDSLeY6ve7BJyXklxERA7U6UKkR3sVOIhWpVpBb2eSPtO0oOjCsKAVaukIf9s7u-DjIt0GxVHmIJGbiLJz9SkUh-ziqpBFoDotAb24FHpkVGeHbfBDpthpeAvA_ePa_M3hsGO4t24dhAGXplkbVGoMO47EDOuR-1JVdQ7qTEwGV6CO23q05xod89QmBcct2DJNIxWiS9TL64c0_Q_RlnVRVcX4KpPnfcNZWaZmviYvhLYFXCTAlwBUTCmzXgQh9ble2o9XItt5vsHT_vLuHqbz9vkWI3eMGEBBWAKbqaKS_8kIzsrseaQ'
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRF-TOKEN': csrf_token,  
            'X-Requested-With': 'XMLHttpRequest'
        }

        response_post = session.post(url_post, data=payload, headers=headers)
        if response_post.status_code == 200:
            response_json = response_post.json()
            if response_json.get("result"):
                short_url = response_json.get("short_url")
                print(f"URL acortada: {short_url}")
            else:
                print("Error en la respuesta:", response_json)
        else:
            print(f"Error en la solicitud POST: {response_post.status_code}")
    else:
        print("No se pudo encontrar el token CSRF.")
else:
    print(f"Error en la solicitud GET: {response_get.status_code}")
