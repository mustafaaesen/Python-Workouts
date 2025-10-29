from functools import reduce#reduce fonksiyonu import edildi
#<-------- GÖMÜLÜ FONKSİYONLAR ------------>


# ----- map() Fonksiyonu-----

# parametre olarak bir fonksiyon ve liste veya tuple gibi iterator işlemler yapılabilecek
#veri tipi alır. Elemanlarına sırayla paramtere olarak aldığı fonksiyon işlemlerini 
#uygular ve geri döndürür


def double (x):
    return x*2   # elemanın 2 katını gödnüren fonksiyo



liste=list(map(double,[1,2,3,4,5,6,7]))# paramtre olarak double fonsiyonunu ve bir liste aldı
                                   # geri liste adlı listeye dönndürdü


print(liste)

# lamda ile kullanımı

liste1=list(map(lambda x:x**2,(1,2,3,4,5,6,7,8,9)))# lambda ile doğrudan fonksiyon tanımı yapılabilir
                                                    # aldığı tuple elemanlarının karesini liste1 adlı
                                                    #listeye döndürür
print(liste1)

#Çoklu Paramtre------> Birden fazla  tanımlı listeyi paramtre olarak alabilir


liste2=[3,5,7,8,4,9,10]
liste3=[1,2,3,4,5,6,7]

liste4=list(map(lambda x,y:x*y,liste2,liste3))# liste2 ve liste3 ü parametre olarak alıp
                                              # elemanlarını  çarpımını liste4 e döndürür


print(liste4)



#<--------- reduce() Fonksiyonu----------->

#parametre olarak bir fonksiyon ve bir iterator olabilecek veri tipi(liste,tuple) alır
# ilk elemana fonksiyondaki işlemi uygular ve daha sonra ortaya çıkan sonuç ve sıradaki
#elemanı tekrar aynı işlemi uygular. Bu döngü eleman sayısı bitene kadar devam eder


def toplama(x,y):

    return x+y



listetoplam=(reduce(toplama,[12,18,20,10]))  #toplama fonksiyonu ve bir liste parametre aldı
     # ilk iki elemanı toplar ve
     # eleman sayısı bitene kadar:
           # souçla sıradaki elemanı toplar ve sonucu döndürü


print(listetoplam)


#<---- lambda kullanımı

faktoriyel=reduce(lambda x,y: x*y,[1,2,3,4,5])  # listeyi x*y fonksiyonunu uygular
    #pratik olarak faktöriyel hesabına örnek verilebilir
print(faktoriyel)

#PRATİK KULLANIM

def maksimum(x,y):

    if(x>y):
        return x
    else:
        return y
    
maksimum=reduce(maksimum,[10,20,5,-19,45])

print(maksimum)
# liste elemanlarının en büyüğünü pratik olarak buldu



#<----------- filter() Fonksiyonu ------------>

# mantığı reduce ile aynıdır. Ancak fonksiyonu true ya da false döndürür
#dönüş değeri true olanları bir araya getirip geri döndürür

liste5=list(filter(lambda x: x%2==0,[0,1,2,3,4,5,6,7,8])) # listenin çift elemanlarını döndürür

print(liste5)

def asalMi(x):   # asal sayi olup olmadığını döndüren fonksiyon

    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:

        while(i<x):

            if(x%i==0):
                return False
            
            i+=1
        
        return True

liste6=list(filter(asalMi,range(1,100)))# 1-100 arasındaki sayilardan asal olnları bulup geri döndürür

print(liste6)




#<------- zip() Fonksiyonu------->

# iki farklı listenin elemanlarını indislerine göre eşleştirip tuple şeklinde listeye atamaya
#çalışalım

#or liste1[1,2,3,4,5] liste2[6,7,8,9,10,11]
#beklenen sonuc [(1,6),(2,7),(3,8),(4,9),(5,10)]
# normal kodla yapımı


liste7=[1,2,3,4,5,6]
liste8=[6,7,8,9,10,11]

i=0

sonuc=list()

while(i<len(liste7) and i<len(liste8)): # liste indisleri boyunca döner
    sonuc.append((liste7[i],liste8[i]))

    i+=1

print(sonuc)



# BU İŞLEMİ KOLAYLAŞTIRAN FONKSİYONDUR.
# Parametre olarak iki listenin elemanlarını indislerine göre eşleştiri

sonuc2=list(zip(liste7,liste8))
print("Zip Fonksiyonu ile Sonuc",sonuc2)


#<------ enumarate() Fonksiyonu------->
# liste elemanlarını indisleriyle eşleyerek tuple şeklinde başka bir listeye atamaya çalışalım


liste9=["Elma","Armut","Muz","Kiraz"]

j=0
sonuc3=list()

while(j<len(liste9)):
    sonuc3.append((j,liste9[j]))# bulunulan indis ve eleman tuple olarak liseye atandı

    j+=1

print(sonuc3)

print("Enumerate Fonksiyonu ile sonuc",list(enumerate(liste9)))#aynı işlemi tek satırda yazan enumerate fonksiyonu


liste10=["a","b","c","d","f","g"]


for i,j in enumerate(liste10):
    if(i%2==0):
        print(j)   # çift indiste olanları bulmak için enumerate kullanıldı
                   # liste gönderlip tuple dönütünden ilk indise bakıldı çiftse o eleman ekrana
                   #basıldı




#<-------- all()  any()  Fonksiyonları------->

#hepsi ve herhangi adlı fonksiyonda şunları uygula
#hepsi--> eğer değerlerden sadece biri bile False ise False döndürsün
#Aksi durumda True döndürsün

#herhangi---> eğer değerlerden biri bile true ise True döndürsün
#aksi durumda False döndürsün


liste11=[True,False,True,False,True]

def hepsi(liste11):
    for i in liste11:
        if not i: # eğer biri bile false ise kısmı
            return False
        
    return True # aksi durumda tüm değerler True'dur

print("Hepsi Fonksiyonu-->",hepsi(liste11))

def herhangi(liste11):

    for i in liste11:
        if i :#eğer biri bile true ise
            return True
        
    return False # aksi durumda tüm değerler False'tur
    

print("Herhangi Fonksiyonu-->",herhangi(liste11))



# all ve any fonksiyonları bu işlemleri yapmayı kolaylaştırır

#all()--> Değerlerden biri bile False ise False döner (Mantıksal ve gibi (&&))
#any()--> Değerlerden biri bile True ise True döner(Mantıksal veya gibi(||))

print("all() Fonksiyonu ile-->",all(liste11))

print("any() Fonksiyonu ile-->",any(liste11))