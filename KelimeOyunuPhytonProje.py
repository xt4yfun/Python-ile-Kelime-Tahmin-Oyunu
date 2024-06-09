import random


# kelime listeleri
sehirler = ['adana', 'adıyaman', 'afyon', 'ağrı', 'amasya', 'ankara', 'antalya', 'artvin',
                    'aydın', 'balıkesir', 'bilecik', 'bingöl', 'bitlis', 'bolu', 'burdur', 'bursa', 'çanakkale',
                    'çankırı', 'çorum', 'denizli', 'diyarbakır', 'edirne', 'elazığ', 'erzincan', 'erzurum', 'eskişehir',
                    'gaziantep', 'giresun', 'gümüşhane', 'hakkari', 'hatay', 'ısparta', 'mersin', 'İstanbul', 'İzmir',
                    'kars', 'kastamonu', 'kayseri', 'kırklareli', 'kırşehir', 'kocaeli', 'konya', 'kütahya', 'malatya',
                    'manisa', 'kahramanmaraş', 'mardin', 'muğla', 'muş', 'nevşehir', 'niğde', 'ordu', 'rize', 'sakarya',
                    'samsun', 'siirt', 'sinop', 'sivas', 'tekirdağ', 'tokat', 'trabzon', 'tunceli', 'şanlıurfa', 'uşak',
                    'Van', 'yozgat', 'zonguldak', 'aksaray', 'bayburt', 'karaman', 'kırıkkale', 'batman', 'şırnak',
                    'bartın', 'ardahan', 'ığdır', 'yalova', 'karabük', 'kilis', 'osmaniye', 'düzce']

#----------------------------------------------------------------
oyuncular=["abdullah pabur","abdürrahim karakoç","abdurrahman kızılay","abdurrahman önül","abidin","alişan"]
#----------------------------------------------------------------
meyve = ["elma", "muz", "çilek", "portakal", "karpuz",
    "armut", "üzüm", "kiraz", "ananas", "mango",
    "kivi", "limon", "nar", "erik", "şeftali",
    "kayısı", "greyfurt", "mandalina", "avokado", "hurma",
    "karpuz", "papaya", "ayva", "muz", "Vişne",
    "kavun", "dut", "trabzon hurması", "yaban mersini", "ahududu"]
#----------------------------------------------------------------
hayvanlar=["köpek","kedi","at","balık","tavşan","tavuk","aslan","yılan","keçi","kuş"]
#----------------------------------------------------------------
esyalar=["masa","sandalye","dolap","koltuk","buzdolabı","televizyon","bilgisayar","telefon"]
#----------------------------------------------------------------
tumkelime=sehirler+oyuncular+meyve+hayvanlar+esyalar

# Rasgele seçim
while True:
    print("hangi katogori de oynamak istersiniz (sehirler 1---oyuncular 2 --- meyve 3 --- hayvanlar 4 --- eşyaşar 5 --- Genel 6) ")
    secim=int(input())
    if secim==1:
        kelime = random.choice(sehirler)
        print("kelime tahmin oyununa hoş geldiniz!")
        print("bir sehir ismi tahmin edin.")
    elif secim==2:
        kelime = random.choice(oyuncular)
        print("kelime tahmin oyununa hoş geldiniz!")
        print("bir oyuncular ismi tahmin edin.")
    elif secim==3:
        kelime = random.choice(meyve)
        print("kelime tahmin oyununa hoş geldiniz!")
        print("bir meyve tahmin edin.")
    elif secim==4:
        kelime = random.choice(hayvanlar)
        print("kelime tahmin oyununa hoş geldiniz!")
        print("bir hayvanlar ismi tahmin edin.")
    elif secim==5:
        kelime = random.choice(esyalar)
        print("kelime tahmin oyununa hoş geldiniz!")
        print("bir esyalar ismi tahmin edin.")
    else:
        kelime = random.choice(tumkelime)
        print("kelime tahmin oyununa hoş geldiniz!")
        print("bir genel ismi tahmin edin.")
    kelime_tahmin = "_" * len(kelime)
    tahmin_edilen_harfler = set()
    haklar = 6
    print(kelime_tahmin)
    
    while haklar > 0 and "_" in kelime_tahmin:
        harf = input("bir harf tahmin edin: ").lower()
        
        if harf in tahmin_edilen_harfler:
            print("bu harfi zaten tahmin ettiniz.")
            continue
        
        tahmin_edilen_harfler.add(harf)
        
        if harf in kelime:
            kelime_tahmin = "".join([harf if kelime[i] == harf else kelime_tahmin[i] for i in range(len(kelime))])
            print("doğru tahmin!")
        else:
            haklar -= 1
            print(f"yanlış tahmin! kalan hakkınız: {haklar}")
        
        print(kelime_tahmin)
    
    if "_" not in kelime_tahmin:
        print("tebrikler! kelimeyi doğru tahmin ettiniz.")
    else:
        print(f"üzgünüm, hakkınız bitti. doğru kelime '{kelime}' idi.")