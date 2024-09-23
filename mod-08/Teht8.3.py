import mysql.connector
from geopy.distance import geodesic


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",  # Tietokannan nimi
    user="shst",  # Käyttäjänimi
    password="?P455?",  # Salasana
    autocommit=True
)


def get_coordinates(icao_code):
    cursor = connection.cursor()

    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    cursor.close()

    if result:
        return (result[0], result[1])
    else:
        print(f"Lentokenttää ICAO-koodilla {icao_code} ei löytynyt.")
        return None



icao_code1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").upper()
icao_code2 = input("Anna toisen lentokentän ICAO-koodi: ").upper()


coords1 = get_coordinates(icao_code1)
coords2 = get_coordinates(icao_code2)


if coords1 and coords2:
    distance = geodesic(coords1, coords2).kilometers
    print(f"Lentokenttien välinen etäisyys on {distance:.2f} kilometriä.")


