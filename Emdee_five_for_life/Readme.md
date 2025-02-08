# Script para obtener y enviar el hash MD5 de un texto en un reto web

Este script interactúa con un servidor web, obtiene un texto desde una etiqueta HTML `<h3>`, calcula su hash MD5 y luego envía ese hash al servidor. El servidor probablemente responderá con una bandera (flag) o un mensaje de éxito.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `requests`: Para realizar solicitudes HTTP.
- `beautifulsoup4`: Para analizar el contenido HTML.
- `lxml`: Parser rápido utilizado por BeautifulSoup.

### Instalación de dependencias

Puedes instalar las dependencias utilizando `pip`:

```
pip install requests beautifulsoup4 lxml
```
## Descripción del código
1. Importación de bibliotecas
```
import requests, hashlib
from bs4 import BeautifulSoup
```
- requests: Permite hacer solicitudes HTTP, como obtener páginas web y enviar datos.
- hashlib: Nos permite generar un hash MD5 del texto.
- BeautifulSoup: Ayuda a analizar el HTML de la página web y extraer información de ella.

## 2. Definición de la URL
```
url = 'http://94.237.54.116:47308/'
```
Esta es la URL del servidor al que se le hará la solicitud para obtener el contenido.

## 3. Creación de una sesión y solicitud GET
```
s = requests.Session()
response = s.get(url)
```

Se crea una sesión persistente con el servidor y luego se realiza una solicitud GET para obtener el contenido HTML de la página.

## 4. Analizar el contenido HTML con BeautifulSoup
```
soup = BeautifulSoup(response.text, 'lxml')
```
Usamos BeautifulSoup para analizar el contenido HTML de la respuesta y facilitar la búsqueda de elementos dentro de la página.

## 5. Buscar la etiqueta <h3>
```
h3_tag = soup.find('h3')
```
Se busca la primera etiqueta <h3> dentro del HTML de la respuesta.

## 6. Extraer el texto y calcular el hash MD5
```
if h3_tag:
    text = h3_tag.text.strip()
    hash_md5 = hashlib.md5(text.encode()).hexdigest()
```
Si la etiqueta <h3> existe, extraemos su texto y calculamos su hash MD5.

## 7. Preparar y enviar los datos
```
myobj = {'hash': hash_md5}
flag = s.post(url, data=myobj)
```
Preparamos un diccionario con el hash calculado y lo enviamos al servidor mediante una solicitud POST.

## 8. Mostrar la respuesta del servidor
```
print(flag.text)
```
Finalmente, mostramos el texto de la respuesta del servidor, que debería ser la bandera o un mensaje de validación.
## 9. Caso en el que no se encuentra la etiqueta <h3>
```
else:
    print("❌ No se encontró la etiqueta <h3> en la respuesta del servidor")
```
Si no se encuentra la etiqueta <h3>, se muestra un mensaje de error indicando que no se pudo obtener la información.

## Ejecución

Para ejecutar el script, simplemente corre el siguiente comando en tu terminal:
```
python3 script.py
```
Asegúrate de haber activado tu entorno virtual, si es que usas uno, y de tener las dependencias instaladas.