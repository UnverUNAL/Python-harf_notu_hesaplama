def not_hesapla(satır):
    satır = satır.strip()
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim, harf, son_not


with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    kalanlar_listesi = []
    geçenler_listesi = []

    for satır in file:
        isim, harf, son_not = not_hesapla(satır)
        eklenecekler_listesi.append(f"{isim}---------------------->{harf}\n")
        if son_not < 60:
            kalanlar_listesi.append(f"{isim}---------------------->{harf}\n")

        else:
            geçenler_listesi.append(f"{isim}---------------------->{harf}\n")

with open("notlar.txt", "w", encoding="utf-8") as file2:
    file2.writelines(eklenecekler_listesi)

with open("kalanlar.txt", "w", encoding="utf-8") as file3:
    file3.writelines(kalanlar_listesi)
with open("geçenler.txt", "w", encoding="utf-8") as file4:
    file4.writelines(geçenler_listesi)


