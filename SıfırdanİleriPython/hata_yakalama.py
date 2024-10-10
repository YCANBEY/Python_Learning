def çift_mi(sayı):

    if isinstance(sayı,int):

        if(sayı % 2 == 0):
            return sayı
        else:
            raise ValueError("Sayı çift değil")
    else:
        raise TypeError("Geçersiz tür, tamsayı bekleniyor")


liste = [34,"asda",25,2,"123a",3]

for i in liste:

    try:
        print(çift_mi(i))
    except (ValueError,TypeError):
        pass
