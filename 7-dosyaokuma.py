#<--------- Dosya Okuma İşlemleri------------->

# r okuma kipiyle dosya açılıp okunur


file=open("bilgiler.txt","r")


try:
    file=open("bilgiler2.txt","r")

except FileNotFoundError: # dosya bulunmuyorsa hata mesajı döndürmek için try exceot bloklarında yazıldı
    print("Böyle Bir Dosya Mevcut Değil!!!")



#<------- For Döngüsüyle Okuma ------>

file=open("bilgiler.txt","r",encoding="utf-8")#dosya türkçe karakter okuyacak şekilde açıldı

for i in file:  #dosya üzerinde döngü ile gezinip değer yazdırma
    print(i)  #tüm satırları alt alta atlamalı yaar 1 satır boşluk verir
             # bunu önlemek için print(i,end="") şeklinde yazılmalı

file.close()


#<-------- read() Fonksiyonu ile Okuma------->

file=open("bilgiler.txt","r",encoding="utf-8")

icerik=file.read()
print("Dosya İçeriği")

print(icerik)


#<--------- readline() Fonksiyonu ile Okuma--------->

file=open("bilgiler.txt","r",encoding="utf-8")

print(file.readline())  #tek satır ookur imleci sonrakine devreder her seferinde
                        #okunacak bir şey kalmazsa boş karakter basar


#<--------- readlines() Fonksiyonu ile Okuma --------->


file=open("bilgiler.txt","r",encoding="utf-8")# her satırı okuyarak bir listeye atabilir böylelikle
                                            # tüm elemanları bastırıbilir

liste=file.readlines()

print(liste)

file.close()


#<-------- Dosyayı Otomatik Kapatmak------------>

# with open kod bloğu altında dosya işlemleri yapıldığında kapatma durumu
#otomatik hale gelir ve unutma gibi durumların önüne geçilip sistem kaynaklarından
#tasarruf edilebilir


with open("bilgiler.txt","r",encoding="utf-8") as file:

    for i in file:
        print(i)    # dosyadaki kayıtları okuyacak




#<------ Dosyalarda İleri Geri İşlemleri------- >

#Dosyada değişken(file) bir imleç gibi satır satır ilerler ve bu şekilde veriyi okur.
# Burada ise tell()  fonksiyonu ile bulunduğumuz byte'ı öğrenip bunun yardımıyla
# seek()   fonksiyonu ile istenilen byte üzerine gidebiliriz


with open("bilgiler.txt","r",encodinf="utf-8") as file:
    file.seek(5)#dosyanın 5. byte ına gidildi
    icerik=file.read(10)# buradan itibaren 10 karakter okur
    file.tell() # bulunulan karakteri söyler

    print(icerik)
    file.seek(0) # işlemler bittikten sonra dosyanın en başına gidilmesi için



