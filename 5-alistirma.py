#NYP ile kumanda tasarımı

import random
import time

class Kumanda():

     # objenin yapıcı metod tanımı
    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):


        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tvAc(self):# Televizyonu açacak fonksyion


        if(self.tv_durum=="Acik"):
            print("Televizyon Zaten Açık !!!")

        else:
            print("Televizyon Açılıyor...")

            self.tv_durum="Acik"

    
    def tvKapa(self): #TV kapatan fonksiyon

        if(self.tv_durum=="Kapali"):

            print("Televizyon Zaten Kapali!!!")

        else:
            print("Televizyon Kapatiliyor...")

            self.tv_durum="Kapali"
        
    
    def sesAyarla(self):

        while True:

            cevap=input("Sesi Azaltmak Icin---> '<'\nSesi Arttirmak Icin---> '>'\nCikis Icin--->Cikis")


            if(cevap=='<'):  # ses azaltmak icin

                if(self.tv_ses!=0): #sesin negatif değer kontrolü
                    self.tv_ses -= 1
                    print("Ses Durumu",self.tv_ses)

            elif(cevap=='>'):

                    if(self.tv_ses!=32): # üst değer tanımı

                        self.tv_ses+=1
                        print("Ses Durumu",self.tv_ses)

                
            else:
                    print("Ses Güncellendi!!!",self.tv_ses)
                    break

    
    def kanalEkle(self,kanal_ismi): #kanal ekleyen fonksyion
        print("Kanal Ekleniyor...")
        time.sleep(1)#gerçekçilik açısından bekletecek 1 saniye

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi!!!")

    def rastgeleKanal(self):# tuşa basildiginda rastgele kanala gececek fonksiyon

        rastgele=random.randint(0,len(self.kanal_listesi)-1) # aralik tanimi 0 ile kanla sayisi kadar

        self.kanal=self.kanal_listesi[rastgele] # kanal gucenlleme

        print("Şuanki Kanal",self.kanal)



    def __len__(self):

        return len(self.kanal_listesi)# kanal sayisini döndürecek 
    

    def __str__(self): #print durumunda calisacak str fonksiyonu

        return "TV Durumu: {}\nTV Ses : {}\nKanal Listesi: {}\nŞuanki Kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)



kumanda=Kumanda()#nesne türetilmesi

print("""


Televizyon Ugulamasi

      1--- TV Aç

      2--- TV Kapat

      3--- Ses Ayarlari

      4--- Kanal Ekle

      5--- Kanal Sayisini Ogren

      6--- Rastgele Kanala Gec

      7--- Televizyon Bilgileri

      CIKIS ICIN 'q' YA BASIN
     

""")


while True:

    islem=input("Yapmak Istediginiz Islemi Seciniz")

    if(islem=="q"):

        print("Program Sonlandiriliyor...")

        break
    elif(islem=="1"):

        kumanda.tvAc()

    elif(islem=="2"):
        kumanda.tvKapa()

    elif(islem=="3"):
        kumanda.sesAyarla()

    elif(islem=="4"):
        kanal_isimleri=input("Kanal Isimlerini Virgul(,) Ile Ayirarak Giriniz")
        kanal_listesi=kanal_isimleri.split(",")#girilen stringi verilen karaktere göre ayirarak liste yapar

        for eklenecekler in kanal_listesi:
            kumanda.kanalEkle(eklenecekler) #kanallari kanal listesine gezerek ekler

    elif(islem=="5"):

        print("Kanal Sayisi",len(kumanda))#kanal listesinin boyuu yazdirarak kanal sayisi yazdirildi

    
    elif(islem=="6"):
        kumanda.rastgeleKanal()

    elif(islem=="7"):

        print(kumanda)# str fonksiyonuna nesne gönderilerek bilgileri return eder

    
    else:
        print("Hatali Giris Yaptiniz!Lutfen Tekrar Deneyiniz")





    

