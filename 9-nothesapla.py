#<-------- NOT HESAPLAMA ÖRNEĞİ---------->
#Senaryo: dosya.txt adındaki dosyadan öğrencilerin vize ve final notlarını okuyuo
# notlarını hesaplamak


def notHesapla(satir):

    satir=satir[:-1]#her satir sonunda \n olduğu için bir satır atlayarak print eder
       # bu durumu  önleyip alt alta satır boşluğu olmaması adına yapılır

    liste=satir.split(",")# her satiri ',' e göre bölüp listeye atar
    #bu şkeilde liste indislerinden notlara erişilip hesaplama yapılabilir

    isim=liste[0] #listenin ilk indisi isim

    not1=int(liste[1])#ikinci indis ilk not casting edilerek alınır

    not2=int(liste[2])#üçüncü indis ikinci not

    not3=int(liste[3])# dördüncü indis üçüncü not

    #notlara erişildi Harf notu hesaplanabilir

    sonNot=(not1*(3/10))+(not2*(3/10))+(not3*(4/10))# Öğrencinin genel notu heaplandı

    if(sonNot>=90):
        harf="AA"

    elif(sonNot>=85):
        harf="BA"
    elif(sonNot>=80):
        harf="BB"
    elif(sonNot>=75):
        harf="CB"
    elif(sonNot>=70):
        harf="CC"
    elif(sonNot>=65):
        harf="DC"
    elif(sonNot>=60):
        harf="DD"
    elif(sonNot>=55):
        harf="FD"
    else:
        harf="FF"

    
    #Harf notları ve notlar hesaplandı bu şekilde her satır yeni dosyaya yazdırılabilir

    return isim+"--------->"+harf+"\n"





with open("dosya.txt","r",encoding="utf-8") as file:
    #dosya içindeki her satir hesaplama fonksitonuna gönderilmeli

    eklenecekler=[]

    for i in file:

        eklenecekler.append(notHesapla(i))#fonksiyondan dönen değerleri de eklenecekler listesine yazdıracağız


    #eklenecekler listesinin her elemanı yeni bir txt dosyaya yazdırılarak not listesi oluşturulur

    with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler:
            file2.write(i)