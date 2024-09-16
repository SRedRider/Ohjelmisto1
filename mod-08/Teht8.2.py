import mysql.connector


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='shst',
         password='?P455?',
         autocommit=True
         )


def maakoodi(iso):

    sql = f"SELECT type, name, COUNT(*) FROM airport WHERE iso_country='{iso}' GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    # Tarkistetaan, onko tuloksia
    if len(tulos) > 0:
        print(f"Lentokenttien tyypit ja määrät maassa {iso}:")
        for rivi in tulos:
            print(rivi[1])
            # Tulostetaan lentokenttätyyppi ja niiden määrä
            print(f"{rivi[0].capitalize()}: {rivi[2]} kpl")
    else:
        print(f"Ei löytynyt lentokenttiä maakoodilla {iso}.")

    # Suljetaan kursori
    kursori.close()


# Käyttäjän syöte
iso = input("Anna maan maakoodi: ").upper()
maakoodi(iso)