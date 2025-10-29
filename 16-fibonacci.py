class Kuvvet3():  #3. kuvvetlerini alan sınıf

    def __init__(self,max=0): #sınıfn init fonksiyonu gelen max değer ve kuvvet değeri

        self.max=max
        self.kuvvet=0
    
    def __iter__(self):

        return self
    

    def __next__(self):  #iterator ile ilerleyebilemek için next fonksiyonu tanımlanması

          if (self.kuvvet<=self.max): #kuvvet max değerden küçük ise kuvveti alınır
               sonuc = 3**self.kuvvet

               self.kuvvet+=1


               return sonuc
          
          else: # değilse stop iteration hatsı döndürülür
               self.kuvvet=0  # tekrar kullanılabilmesi için kuvvetin 0 lanması gerekiyor
               raise StopIteration
          
kuvvet=Kuvvet3(6) #nesne türetilmesi

iterator=iter(kuvvet) #iteratora atanması

print(next(iterator)) # yazımı


for i in kuvvet: # for döngüsü ile gezilebilri hale getirilmesi
     print(i)



#generator tanımlayarak iterator ile birlikte fibonacci hesaplama

def fibonacci():
     
     a=1
     b=1

     yield a
     yield b


     while True:
          
          a,b=b, a+b # her a değeri b olacak b ise aile b nin toplamı olacak



for sayi in fibonacci():
     
     if (sayi>100000):
          break
     else:
          print(sayi)
     
