#MODULLER

#request ve beatifulsoap modulleri ile internetten veri çekme

import requests

from bs4 import BeautifulSoup  # bununla birikte sayfa kaynağındaki veriler html etiketlerine göre parse edilebilir

url= "https://www.firmasec.com/firmalar?q=ankara"

response = requests.get(url) # sayfa url si verilir


print(response) # çekilip çekilmediğini görmek için  
#200 çıktısı biglilerin öekildiğini gösterir

html_icerik=response.content # response ile çekilen içeriği getiri gösterir

soup=BeautifulSoup(html_icerik,"html.parser") # html içeriği ve html parser gönderilerek html sayfası
#görütnülenebilir


print(soup.prettify())  #çektiğimiz web sayfası karşımıza gelir


#belirli etiketleri ondan kaç tane olduğunu vs gibi sonuçları beaitfulsoup ile öğrenebilriz


#linkler için tüm a etiketlerini bulabilriiz


for i in soup.find_all("a"): # linklerin bulunduğu tüm eitketleri döner

    #print(i) bastırmak için
    #print(i.get("href")) # tıklanılabilir kısımları verir
    #sadece yazıları veriir
    print(i.get("text"))

    print("******************************")


print(soup.find_all("div" ,{"class": "listing-item"}))