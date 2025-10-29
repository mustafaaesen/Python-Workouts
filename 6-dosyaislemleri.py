#Dosyalama İşlemleri

"""file=open("bilgiler.txt","w",encoding="utf-8")"""# w tipinde açılan dosya her seferinde siler yeniden açar
#Dosyaya Türkçe Karakter YAzabilmek İçin utf-8 formatında açılır

#Dosyaya veri kaybetmeden ekleme yapmak için "a" kipi ile açmalısın

file=open("bilgiler.txt","a",encoding="utf-8")


file.write("Mustafa ESEN")#Dosyaya Yazma İşlemi
file.write("Necmettin Erbakan Üniversitesi")

#<---- Alt Alta Yazma İşlemi ---->

file.write("Mustafa ESEN\n")
file.write("Necmettin Erbakan Üniversitesi")
file.close()
