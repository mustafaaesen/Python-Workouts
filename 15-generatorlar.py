"""
iterable nesneler üretebilmek için kullanılan objelere generator denir

100k değer üretecek şekilde fonksiyon yazıldığında hafıza çok fazla kullanılacağından karmaşık olur

bu fonksiyon generator ile yazılırsa hafıza açısından oldukça tasarruf sağlar

sadece ihtiyaç duyduğumuz anda değeri üretir ve verir

"""


def kareleri_al():

    sonuc=[]

    for i in range(1,6):
        sonuc.append(i**2)

    return sonuc
#bu fonksiyon ile her sayıyı karesi alınıp listede tutuldu kalanalık olunca generator önemi analışılmaya
#başlanıyor

print(kareleri_al())

def kareleri_al1():

    for i in range(1,6):

        #sonuc listesine ve returne gerek yok yield anahtar kelimesi yeterli

        yield i**2
    
generator=kareleri_al1()
#genrator ile türetildi

iterator=iter(generator) #iterator ile gezilebilir hale getirildi

print(next(iterator))

#ürettiği değer bitince stop iteration hatası alınca tekrar başa dönemez
#o değerleri tanımlayınca işi bitmiş olur
#bu yönden dezavantajı vardır görüntülenmek istendiğinde oldukça faydalı yaklaşımdır


def carpimtablosu():

    for i in range(1,11):

        for j in range(1,11):

            yield "{} x {} = {}".format(i,j, i*j) #genrator ile çarpım tablosu



#doğrudan genrator oluşturmak yerine for döngsü içinde kullanım


for i in carpimtablosu():
    print(i) #her yeni değerde yield değer üretecek