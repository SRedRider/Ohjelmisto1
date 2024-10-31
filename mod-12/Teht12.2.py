import requests


def hae_saa(paikkakunta, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"
    try:
        vastaus = requests.get(url)
        if vastaus.status_code == 200:
            data = vastaus.json()
            lampotila_kelvin = data["main"]["temp"]
            lampotila_celsius = lampotila_kelvin - 273.15  # Muunnos Kelvinistä Celsius-asteiksi
            saakuvaus = data["weather"][0]["description"]

            print(f"Sää {paikkakunta}: {saakuvaus.capitalize()}, lämpötila: {lampotila_celsius:.1f} °C")
        else:
            print("Paikkakuntaa ei löytynyt tai virhe pyynnössä.")
    except requests.RequestException as e:
        print("Virhe yhteyden muodostamisessa:", e)



paikkakunta = input("Anna paikkakunnan nimi: ")
api_key = "API AVAIN"
hae_saa(paikkakunta, api_key)
