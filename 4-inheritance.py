#ÖZEL METODLAR 
#ÇAğırılmadığı halde tnaımlı olan olarak gelek metodlardır

class Kitap():
    

    def __init__(self,isim,yazar,sayfa_sayisi,tur): # tanımlanan sınıftan farklı nesneler üretmeye yarar

        print("İnit Fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayisi=sayfa_sayisi
        self.tur=tur

    def __str__(self): # hazır gelen diğer fonksiyondur bir şey return etmezse nesne doğrudan print edilince  tanımlandığı adresi bastırır ekrana

        return "İsim: {}\nYazar: {}\nSayfa Sayisi:{}\nTür:{}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)


    def __len__(self):#sınıfın özellikelrine göre uzunluk gibi bir değer döndürebilir tanımlanmazsa
                      # hatalı değer döndürecektir. Burada sayfa sayısı return edildi
        return self.sayfa_sayisi
    
    def __del__(self): # özellik eklenmezse silinir override edilmeden özellik eklenir
        print("Kitap nesnesi siliniyor...")

kitap=Kitap("İstanbul Hatirası","Ahmet Ümit",560,"Polisiye")
print(kitap) #__str__ ile yapıldı
print(len(kitap))    # __len__ ile yapıldı
del kitap  # __del__ ile yapıldı

print(kitap)  # kitap silindiği için  most recant call hatası verir çünkü kitap yok