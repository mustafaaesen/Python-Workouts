#<----- DOSYALARDA DEĞİŞİKLİK YAPMAK------>

# 'r+'  kipi ile kullanılarak hem okuma hem yazma sağlar


with open("bilgiler.txt","r+",encoding="utf-8") as file: # r+ ile dosya hem okunur hem dosyaya yazılır

    print(file.read())

    file.seek(10)# dosyada 10. karaktere gidilir
    file.write("DENEME")#bulunduğu yerden itibare(10.karakter) veirlen stringi yazar
    




#<------ DOSYANIN SONUNA EKLEME--------->

# 'a' kipiyle dosya açılınca sonuna gider imleç. Bu şekilde writw ile yazılabilir


with open("bilgiler.txt","a",encoding="utf-8") as file:

    file.write("EN ALT SATIRA EKLENDİ\n")#a ile sonuna gidilmiş dosyaya string ifade ekleme



with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())



#<-------- DOSYANIN BAŞINA EKLEME----------->

#dosyanın tüm içeriği bit değişkene atanıp başına eklenip sonra tekrar dosyaya yazdırılabilir


with open("bilgiler.txt","r+",encoding="utf-8") as file:

    icerik =file.read()# dosyanın içeriği değişkene atandı
    icerik="BAŞINA EKLENDİ\n"+icerik
    file.seek(0)# en başa gidildi
    file.write(icerik)#dosyaya icerik yazıldı


with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())




#<---------- DOSYANIN ORTASINA EKLEME--------- >

#istenilen yere satır satır okuyan readlines() ile listeye alınır
#daha sonra istenilen yere insert() fonksiyonu ile ekleme yapılır
#liste for ile tekrar dosyaya yazdırılır


with open("bilgiler.txt","r+",encoding="utf-8") as file:

    liste=file.readlines()# satır satır okunup listeye atanır
    liste.insert(3,"ARAYA EKLENDİ\n") #istenilen yere eleman eklenir

    for i in liste:
        file.write(i)# listenin tüm elemanları sırayla dosyaya yazdırılır



with open("bilgiler.txt","r+",encoding="utf-8") as file:
    print(file.read())
