#<-----Fonksiyonları Dönme ve Parametre Olarak Kullanma------>

#Fonksiyonların içeirsinde fonksiyon tanımlayarak farklı değerler return edilebilir

def anaFonksiyon(islem_turu): #aldığı işlem türüne göre elemlanların farklı işlemlerini
                              #dödnüren  ana fonksiyon

    def toplama(*args):   # toplama fonksiyonu
        toplam=0

        for i in args:
            toplam+=i
        
        return toplam
    
    def carpim(*args):

        carpim=1

        for i in args:
            carpim*=i

        return carpim
    
    if(islem_turu=='toplama'):
        return toplama
    else:
        return carpim


fonk1=anaFonksiyon("toplama")
fonk2=anaFonksiyon("carpim")

print(fonk1(1,2,3,4,5,6))
print(fonk2(1,2,3,4,5,6))


#<--------- Argüman Olarak GÖnderme--------->

def toplama(a,b):   #ayrı ayrı 4 işlem yapan fonksiyonların tanımlanması
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anaFonksiyon2(fonk1,fonk2,fonk3,fokn4,islem_turu): #paramtre olarak tüm işlemeri alıp işlem türüne
                                #göre fonksiyonları çaıştıran ana fonksiyon yapısı

    if(islem_turu=="toplama"):
        print("10 ve 50 Toplamı",fonk1(10,50))

    elif(islem_turu=="cikarma"):
        print("20 ile 4 Farkı",fonk2(20,4))

    elif(islem_turu=="carpma"):
        print("4 ve 6 Çarpımı",fonk3(4,6))
    
    elif(islem_turu=="bolme"):
        print("10 ile 2 Bölümü",fokn4(10,2))
    else:
        print("Geçersiz Seçim Yaptınız...")

    
print(anaFonksiyon2(toplama,cikarma,carpma,bolme,"toplama"))
print(anaFonksiyon2(toplama,cikarma,carpma,bolme,"cikarma"))
print(anaFonksiyon2(toplama,cikarma,carpma,bolme,"carpma"))
print(anaFonksiyon2(toplama,cikarma,carpma,bolme,"bolme"))
print(anaFonksiyon2(toplama,cikarma,carpma,bolme,"deneme"))