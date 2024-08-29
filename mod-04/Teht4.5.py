oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

yritykset = 0


while yritykset < 5:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana.")
        yritykset += 1


if yritykset == 5:
    print("Pääsy evätty.")
