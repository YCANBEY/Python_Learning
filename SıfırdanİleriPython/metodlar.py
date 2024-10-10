class yazılımcı():

    def __init__(self,isim,soyisim,numara,maaş,diller):

        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def bilgilerigöster(self):

        print("""
        Yazılımcı objesinin özellikleri
        İsim: {}
        
        Soyisim: {}
        
        Numara: {}
        
        Maaş: {}
        
        Bildiği Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))


    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor...")
        self.maaş += zam_miktarı

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor....")
        self.diller.append(yeni_dil)

    def numara_degistir(self,yeni_numara):
        print("Numara değiştiriliyor...")
        self.numara = yeni_numara


yazılımcı = yazılımcı("Yiğit","Canbey",12345,3000,["Python","Java"])

yazılımcı.bilgilerigöster()

yazılımcı.dil_ekle("GoLang")

yazılımcı.bilgilerigöster()

yazılımcı.zam_yap(500)

yazılımcı.bilgilerigöster()

yazılımcı.numara_degistir(54321)

yazılımcı.bilgilerigöster()
