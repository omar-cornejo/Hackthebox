import requests, hashlib  # 1
from bs4 import BeautifulSoup  # 2

url = 'http://94.237.54.116:47308/'  # 3

s = requests.Session()  # 4
response = s.get(url)  # 5

soup = BeautifulSoup(response.text, 'lxml')  # 6

# Buscar la etiqueta h3
h3_tag = soup.find('h3')  # 7

if h3_tag:  # 8
    text = h3_tag.text.strip()  # 9
    hash_md5 = hashlib.md5(text.encode()).hexdigest()  # 10

    myobj = {'hash': hash_md5}  # 11
    flag = s.post(url, data=myobj)  # 12

    print(flag.text)  # 13
else:  # 14
    print("❌ No se encontró la etiqueta <h3> en la respuesta del servidor")  # 15
