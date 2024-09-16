import mysql.connector


def maakoodi(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]}, ja se sijaitsee kunnassa {rivi[1]}")


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='shst',
         password='?P455?',
         autocommit=True
         )

icao = input("Anna maan nimi ICAO koodi: ")
maakoodi(icao)
