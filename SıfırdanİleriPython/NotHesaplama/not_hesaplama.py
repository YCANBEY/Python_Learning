def not_hesapla(satır):

    satır = satır[:-1]

    liste = satır.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = (not1 * 0.3) + (not2 * 0.3) + (not3 * 0.4)

    if(son_not >= 90):
        harf = "AA"
    elif(son_not >= 85):
        harf = "BA"
    elif(son_not >= 80):
        harf = "BB"
    elif(son_not >= 75):
        harf = "CB"
    elif(son_not >= 70):
        harf = "CC"
    elif(son_not >= 65):
        harf = "DC"
    elif(son_not >= 60):
        harf = "DD"
    elif(son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim,harf


with open("dosya.txt","r",encoding = "utf-8") as file:

    geçenler_listesi = []
    kalanlar_liste = []
    harf_notları = []




    for i in file:
        isim,harf = not_hesapla(i)
        harf_notları.append(isim + "-------->" + harf + "\n")

        if harf == "FF":
            kalanlar_liste.append(isim + "------->" + harf + "\n")
        else:
            geçenler_listesi.append(isim + "------->" + harf + "\n" )


    # notlar.txt dosyası yazma
    with open("notlar.txt","w",encoding="utf-8") as file1:
        for i in harf_notları:
            file1.write(i)

    # geçen öğrencileri geçenler.txt dosyasına yazma
    with open("geçenler.txt","w",encoding="utf-8") as file2:

        for i in geçenler_listesi:
            file2.write(i)

    # kalan öğrencileri kalanlar.txt dosyasına yazma
    with open("kalanlar.txt","w",encoding="utf-8") as file3:

        for i in kalanlar_liste:
            file3.write(i)