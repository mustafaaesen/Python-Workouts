class Calisan():

    def __init__(self,isim,maas,departman):  #Ana sınıf olan Çalışan sınıfı tanımı yapıldı
        print("Çalışan sınıfı init fonksiyonu...")

        self.isim=isim
        self.maas=maas
        self.departman=departman

    def bilgileriYazdir(self):
        print("Çalışan sınıfı bilgileri...")

        print("İsim: {}\nMaas: {}\nDepartman: {}".format(self.isim,self.maas,self.departman))

    
    def departmanDegistir(self,yeni_departman):
        self.departman=yeni_departman



class Yonetici(Calisan):  #Çalışan sınıfının özelliklerini miras alacak yönetici sınıfı

    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yönetici sınıfı init fonksiyonu")

        self.isim=isim
        self.maas=maas
        self.departman=departman
        self.kisi_sayisi=kisi_sayisi


    def bilgileriYazdir(self):
        print("Yönetici sınıfı bilgileri...")

        print("İsim: {}\nMaas: {}\nDepartman: {}\nSorum Olduğu Kişi Sayısı".format(self.isim,self.maas,self.departman,self.kisi_sayisi))
              # bilgileriGöster medtodunun override edilmesi

    def zamYap(self,zam_miktari):
        self.maas+=zam_miktari


#super ANAHTAR KELİMESİ

#mirzs alınan metodunun özelliklerini kullanmayı sağlayan kelimedir. Böylelikle 
#override edilmesi durumunda hazırda kullanılan metod özelliklerini tekardan yazmaya gerek kalmaz
#miras alınan  nesnenin init fonksiyonu kulalnılır


class Yonetici(Calisan):


    def __init__(self,isim,maas,departman,kisi_sayisi):
        super.__init__(isim,maas,departman)

        print("Yönetici sınıfı init fonksiyonu")

        self.kisi_sayisi=kisi_sayisi

#şeklinde miras alınan özellikleri tekrardan yazdan kullanılabilir hale gelebilir