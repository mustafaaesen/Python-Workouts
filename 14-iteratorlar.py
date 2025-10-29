liste =[1,2,3,4,5]


iterator =iter(liste)  #liste objesinde iterator oluşturma

print(iterator)

print(next(iterator))


print(next(iterator))

#iter metodu ile türetilebilir nesne haline gelir next ile sonraki elmanlarına geçiş yapılır
#eğer eleman kalamdıysa ise başlangıca geri dönme stop iteration hatası verir

#FOR DONGÜSÜNDE bu durumdan yararlanılır


while True:

    try:

        print(next(iterator))

    except StopIteration:
        break



#denme amaçlı örnek

class Kumanda ():

    def __init__(self,kanal_listesi):
        self.kanal_listesi=kanal_listesi

        self.index=-1 # başlangıçta 0 a gelmesi için yaıldı

    def __iter__(self):
        return self #onjenin iteratora atanması
    
    def __next__(self):
        self.index+=1

        if(self.index< len(self.kanal_listesi)): # index kanal sayısından hala küçükse sorun yok
                                                #devam edilebilir
            return self.kanal_listesi[self.index]
        
        else:#kanal sayısına eşitse iteration hataı vermeli başa dönemez

            self.index=-1
            raise StopIteration


kumanda=Kumanda(["ATV", " TRT", "FOX", "Kanal D", "Bloomberg"])

iterator=iter(kumanda)

print(next(iterator))
                            
for i in kumanda:
    print(i)