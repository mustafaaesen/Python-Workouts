#<------------------ Decorator Fonksiyon Kullanımı------------------>

def extra(fonk): #decorator fonksiyonu

    def wrapper(sayilar):  # tekleri ve çiftleri ayrı ayrı ortalama bulan decorator özelliği

        ciftlerToplami=0
        ciftSyilar=0
        teklerToplami=0
        tekSayilar=0


        for i in sayilar:

            if(i%2==0):
                ciftlerToplami+=i #çift sayıları bulup adedini sayan kısım
                ciftSyilar+=1
            
            else:
                teklerToplami+=i #tek sayıları bulup adedini sayan kısım
                tekSayilar+=1
        print("Çift Sayıların Ortalaması--->",ciftlerToplami/ciftSyilar)
        print("Tek Sayıların Toplamı--->",teklerToplami/tekSayilar)

        fonk(sayilar)#aldığı paramtreye geri döner
    return wrapper #fonksiyon genişletilmiş özelliği geri döner




@extra #decorator ile fonksiyonu genişletilmiş özellik ekleyeceksek ilgili fonksiyonu 
def ortalamaBul(sayilar): #bu şekilde başında tanıtmamız gereklidir.
    toplam=0

    for i in sayilar:
        toplam+=i
    
    print("Genel Ortalama--->",toplam/len(sayilar))


print(ortalamaBul([10,20,45,50,60,80]))