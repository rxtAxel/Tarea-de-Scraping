import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Guido_van_Rossum"
respuesta = requests.get(url)
headers = {
    "User-Agent": "Mozilla/5.0"
}

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text, "html.parser")

Titulo = soup.find("h1").text
print("Titulo:", Titulo)

infobox = soup.find("table", class_=lambda c: c and "infobox" in c)

print("\n=== INFORMACION DE GUIDO ===\n")

for fila in infobox.find_all("tr"):
    th = fila.find("th")
    td = fila.find("td")

    if th and td:
        print(f"{th.text.strip()}: {td.text.strip()}")

print("\n BIOGRAFIA \n")

parrafos = soup.find_all("p")

biografia = parrafos[3].text.strip()
print(biografia)


# Axel De La Rosa Cabral 2025-0375
# Isaura de La Cruz 2025-0240