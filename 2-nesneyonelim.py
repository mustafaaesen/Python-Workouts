#NESNE YONELİMLİ PROGRAMLAMA-METODLAR

# NESNE NİN ÖZELLİKLERİYLE BİRDEN FAZLA YAPILABİLECEK İŞLEMLERİ
#FONKSİYON TANIMLAYARAK YAPMA ŞEKİLLERİNİ İÇERİR ör. bilgileriyazdir gibi


class Yazilimci():  #nesne tanımı

    def __init__(self,isim,soyisim,numara,maas,diller): #nesnenin alacağı parametrelerin 
        self.isim=isim                                  #tanimi
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller

    
    def bilgileriYazdir(self):  #nesnein bilglerini yazdıracak fonksiyon


        print("""

            Yazilimci Nesnesinin Özellikleri
              
            İsim: {}
            
            Soyisim: {}
              
            Numara: {}
              
            Maas:{}
              
            Bildiği Diller:{}

            """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
        
    def zamYap(self,zam_miktari):  # maasa zam yapan metod
        print("Zam yapılıyor...")

        self.maas +=zam_miktari


    def dilEkle(self,yeni_dil): #yeni dil ekleyen metod
        
        print("Dil Ekleniyor...")

        self.diller.append(yeni_dil)



yazilimci1=Yazilimci("Mustafa","ESEN",12345,30000,["C","Python","Java","Qt"]) #Yeni nesne türetimi


yazilimci1.bilgileriYazdir() # nesne içerisindeki fonksiyonu çalıştırma

yazilimci1.dilEkle("Go")
yazilimci1.bilgileriYazdir()