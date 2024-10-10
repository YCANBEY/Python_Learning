"""
Loops - Döngüler
- For
- While (While döngüsünde döngüyü saydırmazsak sonsuz döngüye gireriz)

contiune (istenilen koşul sağlanana kadar atla)
break    (istenilen koşul sağlandığında döngüden çık)
pass     (pass geçilen yeri çalıştırmadan gider)
range    (aralık) (bizden başlangıç noktası, bitiş noktası ve adım sayısı ister)
(adım sayısını belirtmezsek standart olarak 1 alır)(başlangıç noktasını belirtmezsek standart 0 alır)

"""
#--------------------------------------- FOR DÖNGÜSÜ -----------------------------------------------------------

liste = [(1,2,3),(3,4,5),(5,6,7)]
demet = (1,2,3,4,5,6,8,5,4)
kume = {1,2,3,4,5,5}
sozluk = {"Bir":1, "İki":2, "Üç":3, "Dört":4, "Beş":5}

'''
print("Döngü başladı")
for key,value in sozluk.items():
    print(key,value)

print("Döngü bitti")
'''
'''
for i,j,k in liste: # demet ve küme içinde aynı mantık 
    print(i,j,k)  
'''
'''
for i in demet:
    if i %2 == 0:
        print(f"Çift : {i}")
    else:
        print(f"Tek  : {i}")
'''
'''
mesaj = "Python Öğreniyorum"
for harf in mesaj:
    print(harf)
'''
# yeniListe = [1,2,3,4,5,6,7,8,9,10]
#
# for sayi in yeniListe:
#     if sayi == 5:
#         print("Beşi atladık")
#         continue
#     if sayi == 9:
#         print("Sayı 9 olunca döngü bitti")
#         break
#     print(sayi)

# sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
# ]
#
# for i in sehirler:
#     if i == "Ankara":
#         print("Atladık")
#         continue
#     if i == "Aydın":
#         print("Atladık")
#         continue
#     if i == "Çanakkale":
#         print("Döngü bitti")
#         break
#     print(i)

# print(list(range(0,10,2)))

# for i in list(range(100)):
#     if i %2 == 0:
#         print(f"{i} çifttir")

# -------------------------------------- WHİLE DÖNGÜSÜ -------------------------------------------------------------

# sayac = 0
#
# while sayac < 10:
#     print("Merhaba", sayac)
#     sayac +=1

# sayac = 0
# while True:
#     print("Merhaba",sayac)
#     sayac +=1
#     if sayac == 10:
#         print("Döngü bitti")
#         break

plaka_numaralari={
"01" : "Adana",
"02" : "Adıyaman",
"03" : "Afyonkarahisar",
"04" : "Ağrı",
"05" : "Amasya",
"06" : "Ankara",
"07" : "Antalya",
"08" : "Artvin",
"09" : "Aydın",
"10" : "Balıkesir",
"11" : "Bilecik",
"12" : "Bingöl",
"13" : "Bitlis",
"14" : "Bolu",
"15" : "Burdur",
"16" : "Bursa",
"17" : "Çanakkale",
"18" : "Çankırı",
"19" : "Çorum",
"20" : "Denizli",
"21" : "Diyarbakır",
"22" : "Edirne",
"23" : "Elâzığ",
"24" : "Erzincan",
"25" : "Erzurum",
"26" : "Eskişehir",
"27" : "Gaziantep",
"28" : "Giresun",
"29" : "Gümüşhane",
"30" : "Hakkâri",
"31" : "Hatay",
"32" : "Isparta",
"33" : "Mersin",
"34" : "İstanbul",
"35" : "İzmir",
"36" : "Kars",
"37" : "Kastamonu",
"38" : "Kayseri",
"39" : "Kırklareli",
"40" : "Kırşehir",
"41" : "Kocaeli",
"42" : "Konya",
"43" : "Kütahya",
"44" : "Malatya",
"45" : "Manisa",
"46" : "Kahramanmaraş",
"47" : "Mardin",
"48" : "Muğla",
"49" : "Muş",
"50" : "Nevşehir",
"51" : "Niğde",
"52" : "Ordu",
"53" : "Rize",
"54" : "Sakarya",
"55" : "Samsun",
"56" : "Siirt",
"57" : "Sinop",
"58" : "Sivas",
"59" : "Tekirdağ",
"60" : "Tokat",
"61" : "Trabzon",
"62" : "Tunceli",
"63" : "Şanlıurfa",
"64" : "Uşak",
"65" : "Van",
"66" : "Yozgat",
"67" : "Zonguldak",
"68" : "Aksaray",
"69" : "Bayburt",
"70" : "Karaman",
"71" : "Kırıkkale",
"72" : "Batman",
"73" : "Şırnak",
"74" : "Bartın",
"75" : "Ardahan",
"76" : "Iğdır",
"77" : "Yalova",
"78" : "Karabük",
"79" : "Kilis",
"80" : "Osmaniye",
"81" : "Düzce"
}
sehirler = {
    "Adana": ["Aladağ", "Ceyhan", "Çukurova", "Feke", "İmamoğlu", "Karaisalı", "Karataş", "Kozan", "Pozantı",
              "Saimbeyli", "Sarıçam", "Seyhan", "Tufanbeyli", "Yumurtalık", "Yüreğir"],

    "Adıyaman": ["Adıyaman", "Besni", "Çelikhan", "Gerger", "Gölbaşı", "Kâhta", "Samsat", "Sincik", "Tut"],

    "Afyonkarahisar": ["Afyonkarahisar", "Başmakçı", "Bayat", "Bolvadin", "Çay", "Çobanlar", "Dazkırı", "Dinar",
                       "Emirdağ", "Evciler", "Hocalar", "İhsaniye", "İscehisar", "Kızılören", "Sandıklı", "Sinanpaşa",
                       "Sultandağı", "Şuhut"],

    "Ağrı": ["Ağrı", "Diyadin", "Doğubayazıt", "Eleşkirt", "Hamur", "Patnos", "Taşlıçay", "Tutak"],

    "Aksaray": ["Ağaçören", "Aksaray", "Eskil", "Gülağaç", "Güzelyurt", "Ortaköy", "Sarıyahşi"],

    "Amasya": ["Amasya", "Göynücek", "Gümüşhacıköy", "Hamamözü", "Merzifon", "Suluova", "Taşova"],

    "Ankara": ["Akyurt", "Altındağ", "Ayaş", "Balâ", "Beypazarı", "Çamlıdere", "Çankaya", "Çubuk", "Elmadağ",
               "Etimesgut", "Evren", "Gölbaşı", "Güdül", "Haymana", "Kalecik", "Kahramankazan", "Keçiören",
               "Kızılcahamam", "Mamak", "Nallıhan", "Polatlı", "Pursaklar", "Sincan", "Şereflikoçhisar", "Yenimahalle"],

    "Antalya": ["Akseki", "Aksu", "Alanya", "Döşemealtı", "Elmalı", "Finike", "Gazipaşa", "Gündoğmuş", "İbradı",
                "Demre", "Kaş", "Kemer", "Kepez", "Konyaaltı", "Korkuteli", "Kumluca", "Manavgat", "Muratpaşa",
                "Serik"],

    "Ardahan": ["Ardahan", "Çıldır", "Damal", "Göle", "Hanak", "Posof"],

    "Artvin": ["Ardanuç", "Arhavi", "Artvin", "Borçka", "Hopa", "Murgul", "Şavşat", "Yusufeli"],

    "Aydın": ["Bozdoğan", "Buharkent", "Çine", "Didim", "Efeler", "Germencik", "İncirliova", "Karacasu", "Karpuzlu",
              "Koçarlı", "Köşk", "Kuşadası", "Kuyucak", "Nazilli", "Söke", "Sultanhisar", "Yenipazar"],

    "Balıkesir": ["Altıeylül", "Ayvalık", "Balya", "Bandırma", "Bigadiç", "Burhaniye", "Dursunbey", "Edremit", "Erdek",
                  "Gömeç", "Gönen", "Havran", "İvrindi", "Karesi", "Kepsut", "Manyas", "Marmara", "Savaştepe",
                  "Sındırgı", "Susurluk"],

    "Bartın": ["Amasra", "Bartın", "Kurucaşile", "Ulus"],

    "Batman": ["Batman", "Beşiri", "Gercüş", "Hasankeyf", "Kozluk", "Sason"],

    "Bayburt": ["Aydıntepe", "Bayburt (İl merkezi", "Demirözü"],

    "Bilecik": ["Bilecik", "Bozüyük", "Gölpazarı", "İnhisar", "Osmaneli", "Pazaryeri", "Söğüt", "Yenipazar"],

    "Bingöl": ["Adaklı", "Bingöl", "Genç", "Karlıova", "Kiğı", "Solhan", "Yayladere", "Yedisu"],

    "Bitlis": ["Adilcevaz", "Ahlat", "Bitlis", "Güroymak", "Hizan", "Mutki", "Tatvan"],

    "Bolu": ["Bolu", "Dörtdivan", "Gerede", "Göynük", "Kıbrıscık", "Mengen", "Mudurnu", "Seben", "Yeniçağa"],

    "Burdur": ["Ağlasun", "Altınyayla", "Bucak", "Burdur", "Çavdır", "Çeltikçi", "Gölhisar", "Karamanlı", "Kemer",
               "Tefenni", "Yeşilova"],

    "Bursa": ["Büyükorhan", "Gemlik", "Gürsu", "Harmancık", "İnegöl", "İznik", "Karacabey", "Keles", "Kestel",
              "Mudanya", "Mustafakemalpaşa", "Nilüfer", "Orhaneli", "Orhangazi", "Osmangazi", "Yenişehir", "Yıldırım"],

    "Çanakkale": ["Ayvacık", "Bayramiç", "Biga", "Bozcaada", "Çan", "Çanakkale", "Eceabat", "Ezine", "Gelibolu",
                  "Gökçeada", "Lapseki", "Yenice"],

    "Çankırı": ["Atkaracalar", "Bayramören", "Çankırı", "Çerkeş", "Eldivan", "Ilgaz", "Kızılırmak", "Korgun",
                "Kurşunlu", "Orta", "Şabanözü", "Yapraklı"],

    "Çorum": ["Alaca", "Bayat", "Boğazkale", "Çorum", "Dodurga", "İskilip", "Kargı", "Laçin", "Mecitözü", "Oğuzlar",
              "Ortaköy", "Osmancık", "Sungurlu", "Uğurludağ"],

    "Denizli": ["Acıpayam", "Babadağ", "Baklan", "Bekilli", "Beyağaç", "Bozkurt", "Buldan", "Çal", "Çameli", "Çardak",
                "Çivril", "Güney", "Honaz", "Kale", "Merkezefendi", "Pamukkale", "Sarayköy", "Serinhisar", "Tavas"],

    "Diyarbakır": ["Bağlar", "Bismil", "Çermik", "Çınar", "Çüngüş", "Dicle", "Eğil", "Ergani", "Hani", "Hazro",
                   "Kayapınar", "Kocaköy", "Kulp", "Lice", "Silvan", "Sur", "Yenişehir"],

    "Düzce": ["Akçakoca", "Cumayeri", "Çilimli", "Düzce", "Gölyaka", "Gümüşova", "Kaynaşlı", "Yığılca"],

    "Edirne": ["Enez", "Havsa", "İpsala", "Keşan", "Lalapaşa", "Meriç", "Merkez", "Süloğlu", "Uzunköprü"],

    "Elâzığ": ["Ağın", "Alacakaya", "Arıcak", "Baskil", "Elâzığ", "Karakoçan", "Keban", "Kovancılar", "Maden", "Palu",
               "Sivrice"],

    "Erzincan": ["Çayırlı", "Erzincan", "İliç", "Kemah", "Kemaliye", "Otlukbeli", "Refahiye", "Tercan", "Üzümlü"],

    "Erzurum": ["Aşkale", "Aziziye", "Çat", "Hınıs", "Horasan", "İspir", "Karaçoban", "Karayazı", "Köprüköy", "Narman",
                "Oltu", "Olur", "Palandöken", "Pasinler", "Pazaryolu", "Şenkaya", "Tekman", "Tortum", "Uzundere",
                "Yakutiye"],

    "Eskişehir": ["Alpu", "Beylikova", "Çifteler", "Günyüzü", "Han", "İnönü", "Mahmudiye", "Mihalgazi", "Mihalıççık",
                  "Odunpazarı", "Sarıcakaya", "Seyitgazi", "Sivrihisar", "Tepebaşı"],

    "Gaziantep": ["Araban", "İslahiye", "Karkamış", "Nizip", "Nurdağı", "Oğuzeli", "Şahinbey", "Şehitkâmil",
                  "Yavuzeli"],

    "Giresun": ["Alucra", "Bulancak", "Çamoluk", "Çanakçı", "Dereli", "Doğankent", "Espiye", "Eynesil", "Giresun",
                "Görele", "Güce", "Keşap", "Piraziz", "Şebinkarahisar", "Tirebolu", "Yağlıdere"],

    "Gümüşhane": ["Gümüşhane", "Kelkit", "Köse", "Kürtün", "Şiran", "Torul"],

    "Hakkâri": ["Çukurca", "Hakkâri", "Şemdinli", "Yüksekova"],

    "Hatay": ["Altınözü", "Antakya", "Arsuz", "Belen", "Defne", "Dörtyol", "Erzin", "Hassa", "İskenderun", "Kırıkhan",
              "Kumlu", "Payas", "Reyhanlı", "Samandağ", "Yayladağı"],

    "Iğdır": ["Aralık", "Iğdır", "Karakoyunlu", "Tuzluca"],

    "Isparta": ["Aksu", "Atabey", "Eğirdir", "Gelendost", "Gönen", "Isparta", "Keçiborlu", "Senirkent", "Sütçüler",
                "Şarkikaraağaç", "Uluborlu", "Yalvaç", "Yenişarbademli"],

    "İstanbul": ["Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler", "Bakırköy", "Başakşehir",
                 "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü", "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy",
                 "Esenler", "Esenyurt", "Eyüp", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane", "Kartal",
                 "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer", "Silivri", "Sultanbeyli", "Sultangazi",
                 "Şile", "Şişli", "Tuzla", "Ümraniye", "Üsküdar", "Zeytinburnu"],

    "İzmir": ["Aliağa", "Balçova", "Bayındır", "Bayraklı", "Bergama", "Beydağ", "Bornova", "Buca", "Çeşme", "Çiğli",
              "Dikili", "Foça", "Gaziemir", "Güzelbahçe", "Karabağlar", "Karaburun", "Karşıyaka", "Kemalpaşa", "Kınık",
              "Kiraz", "Konak", "Menderes", "Menemen", "Narlıdere", "Ödemiş", "Seferihisar", "Selçuk", "Tire",
              "Torbalı", "Urla"],

    "Kahramanmaraş": ["Afşin", "Andırın", "Çağlayancerit", "Dulkadiroğlu", "Ekinözü", "Elbistan", "Göksun", "Nurhak",
                      "Onikişubat", "Pazarcık", "Türkoğlu"],

    "Karabük": ["Eflani", "Eskipazar", "Karabük", "Ovacık", "Safranbolu", "Yenice"],

    "Karaman": ["Ayrancı", "Başyayla", "Ermenek", "Karaman", "Kazımkarabekir", "Sarıveliler"],

    "Kars": ["Akyaka", "Arpaçay", "Digor", "Kağızman", "Kars", "Sarıkamış", "Selim", "Susuz"],

    "Kastamonu": ["Abana", "Ağlı", "Araç", "Azdavay", "Bozkurt", "Cide", "Çatalzeytin", "Daday", "Devrekani",
                  "Doğanyurt", "Hanönü", "İhsangazi", "İnebolu", "Kastamonu", "Küre", "Pınarbaşı", "Seydiler",
                  "Şenpazar", "Taşköprü", "Tosya"],

    "Kayseri": ["Akkışla", "Bünyan", "Develi", "Felahiye", "Hacılar", "İncesu", "Kocasinan", "Melikgazi", "Özvatan",
                "Pınarbaşı", "Sarıoğlan", "Sarız", "Talas", "Tomarza", "Yahyalı", "Yeşilhisar"],

    "Kırıkkale": ["Bahşılı", "Balışeyh", "Çelebi", "Delice", "Karakeçili", "Keskin", "Kırıkkale", "Sulakyurt",
                  "Yahşihan"],

    "Kırklareli": ["Babaeski", "Demirköy", "Kırklareli", "Kofçaz", "Lüleburgaz", "Pehlivanköy", "Pınarhisar", "Vize"],

    "Kırşehir": ["Akçakent", "Akpınar", "Boztepe", "Çiçekdağı", "Kaman", "Kırşehir", "Mucur"],

    "Kilis": ["Elbeyli", "Kilis", "Musabeyli", "Polateli"],

    "Kocaeli": ["Başiskele", "Çayırova", "Darıca", "Derince", "Dilovası", "Gebze", "Gölcük", "İzmit", "Kandıra",
                "Karamürsel", "Kartepe", "Körfez"],

    "Konya": ["Ahırlı", "Akören", "Akşehir", "Altınekin", "Beyşehir", "Bozkır", "Cihanbeyli", "Çeltik", "Çumra",
              "Derbent", "Derebucak", "Doğanhisar", "Emirgazi", "Ereğli", "Güneysınır", "Hadım", "Halkapınar", "Hüyük",
              "Ilgın", "Kadınhanı", "Karapınar", "Karatay", "Kulu", "Meram", "Sarayönü", "Selçuklu", "Seydişehir",
              "Taşkent", "Tuzlukçu", "Yalıhüyük", "Yunak"],

    "Kütahya": ["Altıntaş", "Aslanapa", "Çavdarhisar", "Domaniç", "Dumlupınar", "Emet", "Gediz", "Hisarcık", "Kütahya",
                "Pazarlar", "Şaphane", "Simav", "Tavşanlı"],

    "Malatya": ["Akçadağ", "Arapgir", "Arguvan", "Battalgazi", "Darende", "Doğanşehir", "Doğanyol", "Hekimhan", "Kale",
                "Kuluncak", "Pütürge", "Yazıhan", "Yeşilyurt"],

    "Manisa": ["Ahmetli", "Akhisar", "Alaşehir", "Demirci", "Gölmarmara", "Gördes", "Kırkağaç", "Köprübaşı", "Kula",
               "Salihli", "Sarıgöl", "Saruhanlı", "Selendi", "Soma", "Şehzadeler", "Turgutlu", "Yunusemre"],

    "Mardin": ["Artuklu", "Dargeçit", "Derik", "Kızıltepe", "Mazıdağı", "Midyat", "Nusaybin", "Ömerli", "Savur",
               "Yeşilli"],

    "Mersin": ["Akdeniz", "Anamur", "Aydıncık", "Bozyazı", "Çamlıyayla", "Erdemli", "Gülnar", "Mezitli", "Mut",
               "Silifke", "Tarsus", "Toroslar", "Yenişehir"],

    "Muğla": ["Bodrum", "Dalaman", "Datça", "Fethiye", "Kavaklıdere", "Köyceğiz", "Marmaris", "Menteşe", "Milas",
              "Ortaca", "Seydikemer", "Ula", "Yatağan"],

    "Muş": ["Bulanık", "Hasköy", "Korkut", "Malazgirt", "Muş", "Varto"],

    "Nevşehir": ["Acıgöl", "Avanos", "Derinkuyu", "Gülşehir", "Hacıbektaş", "Kozaklı", "Nevşehir", "Ürgüp"],

    "Niğde": ["Altunhisar", "Bor", "Çamardı", "Çiftlik", "Niğde", "Ulukışla"],

    "Ordu": ["Akkuş", "Altınordu", "Aybastı", "Çamaş", "Çatalpınar", "Çaybaşı", "Fatsa", "Gölköy", "Gülyalı",
             "Gürgentepe", "İkizce", "Kabadüz", "Kabataş", "Korgan", "Kumru", "Mesudiye", "Perşembe", "Ulubey", "Ünye"],

    "Osmaniye": ["Bahçe", "Düziçi", "Hasanbeyli", "Kadirli", "Osmaniye", "Sumbas", "Toprakkale"],

    "Rize": ["Ardeşen", "Çamlıhemşin", "Çayeli", "Derepazarı", "Fındıklı", "Güneysu", "Hemşin", "İkizdere", "İyidere",
             "Kalkandere", "Pazar", "Rize"],

    "Sakarya": ["Adapazarı", "Akyazı", "Arifiye", "Erenler", "Ferizli", "Geyve", "Hendek", "Karapürçek", "Karasu",
                "Kaynarca", "Kocaali", "Pamukova", "Sapanca", "Serdivan", "Söğütlü", "Taraklı"],

    "Samsun": ["Alaçam", "Asarcık", "Atakum", "Ayvacık", "Bafra", "Canik", "Çarşamba", "Havza", "İlkadım", "Kavak",
               "Ladik", "Ondokuzmayıs", "Salıpazarı", "Tekkeköy", "Terme", "Vezirköprü", "Yakakent"],

    "Siirt": ["Siirt", "Tillo", "Baykan", "Eruh", "Kurtalan", "Pervari", "Şirvan"],

    "Sinop": ["Ayancık", "Boyabat", "Dikmen", "Durağan", "Erfelek", "Gerze", "Saraydüzü", "Sinop", "Türkeli"],

    "Sivas": ["Akıncılar", "Altınyayla", "Divriği", "Doğanşar", "Gemerek", "Gölova", "Hafik", "İmranlı", "Kangal",
              "Koyulhisar", "Sivas", "Suşehri", "Şarkışla", "Ulaş", "Yıldızeli", "Zara", "Gürün"],

    "Şanlıurfa": ["Akçakale", "Birecik", "Bozova", "Ceylanpınar", "Eyyübiye", "Halfeti", "Haliliye", "Harran", "Hilvan",
                  "Karaköprü", "Siverek", "Suruç", "Viranşehir"],

    "Şırnak": ["Beytüşşebap", "Cizre", "Güçlükonak", "İdil", "Silopi", "Şırnak", "Uludere"],

    "Tekirdağ": ["Çerkezköy", "Çorlu", "Ergene", "Hayrabolu", "Kapaklı", "Malkara", "Marmara Ereğlisi", "Muratlı",
                 "Saray", "Süleymanpaşa", "Şarköy"],

    "Tokat": ["Almus", "Artova", "Başçiftlik", "Erbaa", "Niksar", "Pazar", "Reşadiye", "Sulusaray", "Tokat", "Turhal",
              "Yeşilyurt", "Zile"],

    "Trabzon": ["Akçaabat", "Araklı", "Arsin", "Beşikdüzü", "Çarşıbaşı", "Çaykara", "Dernekpazarı", "Düzköy", "Hayrat",
                "Köprübaşı", "Maçka", "Of", "Ortahisar", "Sürmene", "Şalpazarı", "Tonya", "Vakfıkebir", "Yomra"],

    "Tunceli": ["Çemişgezek", "Hozat", "Mazgirt", "Nazımiye", "Ovacık", "Pertek", "Pülümür", "Tunceli"],

    "Uşak": ["Banaz", "Eşme", "Karahallı", "Sivaslı", "Ulubey", "Uşak"],

    "Van": ["Bahçesaray", "Başkale", "Çaldıran", "Çatak", "Edremit", "Erciş", "Gevaş", "Gürpınar", "İpekyolu",
            "Muradiye", "Özalp", "Saray", "Tuşba"],

    "Yalova": ["Altınova", "Armutlu", "Çınarcık", "Çiftlikköy", "Termal", "Yalova"],

    "Yozgat": ["Akdağmadeni", "Aydıncık", "Boğazlıyan", "Çandır", "Çayıralan", "Çekerek", "Kadışehri", "Saraykent",
               "Sarıkaya", "Sorgun", "Şefaatli", "Yenifakılı", "Yerköy", "Yozgat"],

    "Zonguldak": ["Alaplı", "Çaycuma", "Devrek", "Gökçebey", "Kilimli", "Kozlu", "Karadeniz Ereğli", "Zonguldak"]
}

sayac = 0
while sayac <= 3:
    print('''
    Ne yapmak istiyorsunuz ? 
    Plaka numaraları için 1'e, İlçeler için 2'ye basınız.Programdan çıkmak için 3'e basınız
    ''')

    istek = int(input("1/2/3: "))

    if istek == 1:
        hangiPlaka = input("Plaka kodunu giriniz: ")
        if hangiPlaka in plaka_numaralari:
            print(f"Girdiğiniz plaka kodu:\n{hangiPlaka} - ",plaka_numaralari[hangiPlaka])
        else:
            print("Hatalı giriş yaptınız, tekrar deneyiniz.")
    elif istek == 2:
        hangiSehir = input("İlçelerini görmek istediğiniz şehirin baş harfini büyük olacak şekilde giriniz: ")
        if hangiSehir in sehirler:
            print(f"Girdiğiniz şehire ait bilgiler:\n{hangiSehir} - ",sehirler[hangiSehir])
        else:
            print("Hatalı giriş yaptınız, tekrar deneyiniz.")
    elif istek == 3:
        print("İyi günler")
        break
    else:
        print("Hatalı giriş yaptınız, tekrar deneyiniz.")
    sayac +=1
    if(sayac >= 4):
        print("Kullanım hakkınız bitmiştir.")
