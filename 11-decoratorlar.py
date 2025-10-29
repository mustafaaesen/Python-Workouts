#<---------İÇ İÇE FONKSİYONLAR VE DECORATORLAR--------- >

# *args ve **kwargs ---> fonksiyonlara esnek şekilde parametreler gönderimini sağlarlar

# *args ---> fonksiyona gönderilen sayısız paramtereyi demet şeklinde alımını sağlar

def fonksiyon(*args):

    for i in args:

        print(i)#gelen değerleri ekrana basar


print(fonksiyon(1,2,3,4,5,6,7)) #fonksiyonun kullanımı


def fonksiyon2(isim,*args):

    print("İsim:",isim) # aldığı paramtrelerden ilkini isim değişkenine eşitler diğerlerini
                        #demet olarak listelemeye dvam eder
    print("<---------->")

    for i in args:
        print(i)
    
print(fonksiyon2("Mustafa",1,2,3,4,5,6))



#  **kwargs ---> parmatreleri sözlük yapısı oluşturacak şekilde eşlenik olarak alan yapıdır


def fonksiyon3(**kwargs):

    print(kwargs)


print(fonksiyon3(isim="Mustafa",soyisim="ESEN",numara="19010011047"))


#dönfü ile gezinimi szlük yapısı olduğu için 2 boyutlu matris mantığı iledir.

def fonksiyon4(**kwargs):

    for i,j in kwargs.items():

        print("Argüman İsmi:",i,"Argüman Değeri",j)
    

print(fonksiyon4(isim="Hüseyin",soyisim="HAKLI",numara=123456))



#Hybrid Kullanımları

def fonksiyon5(*args,**kwargs):  #birlikte kullanımda ilk göndeirlenleri demet eşlenik geleni kwargs olark alır


    for i in args:

        print(i)

        print("<--------------->")

    for i,j in kwargs.items():

        print(i,j)


print(fonksiyon5(1,2,3,4,5,isim="Mustafa",soyisim="ESEN",numara=19010011047))



#İÇ İÇE FONKSİYONLAR

#fonksiyonlar da birer obje olduğu için birbirleri içerisinde kullanılabilirler

def fonksiyon6(*args):

    def toplama(args):

        toplam=0

        for i in args:
             toplam+=i   # iç ie tanımlı iki fonksiyon ile gelen değerlerin toplanması

        
        return toplam
    print(toplama(args))


print(fonksiyon6(1,2,3,4,5,6,7))