'''class Araba():
    model="Renault Megane"
    renk="Gümüş"
    beygir=118
    silindir=4'''


#print(f"Model: {araba.model},Renk: {araba.renk},Beygir:{araba.beygir},Silindir: {araba.silindir}")

     # Özelliklerini tek print satırı komutunda sınıf.  ile özelliklerine erişip yazdırılır.



# Bu şekilde ne kadar nesne türetirsen hepsi aynı özeliklere sahip olur.
#Bunun için class in metodlarından olan __init__ fonksiyonunu tekrar kendin yazıp
# Paramtre alabilecek şekilde güncelleme gereklidir.

class Araba():
  
    def __init__(self,model,renk,beygir,silindir):
        self.model=model
        self.renk=renk
        self.beygir=beygir
        self.silindir=silindir



araba1=Araba("Reanult Megane","Gümüş",110,4)

araba2=Araba("Pegaoute","Siyah",120,4)

print("Araba 1",araba1.model)