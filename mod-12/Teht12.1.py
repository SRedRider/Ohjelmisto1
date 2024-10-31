import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        vastaus = requests.get(url)
        if vastaus.status_code == 200:
            data = vastaus.json()
            print(data["value"])
        else:
            print("Vitsin hakeminen epäonnistui.")
    except requests.RequestException as e:
        print("Virhe yhteyden muodostamisessa:", e)

# Käynnistetään ohjelma
hae_chuck_norris_vitsi()
