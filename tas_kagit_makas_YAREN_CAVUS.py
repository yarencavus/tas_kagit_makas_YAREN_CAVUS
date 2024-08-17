import random  #Bilgisayarın oyunda rastgele seçim yapabilmesi için random modülü

def tas_kagit_makas():
    #Karşılama mesajı ve kuralların açıklanması
    print("Taş Kağıt Makas Oyununa Hoş Geldiniz!")
    print("Kurallar: taş makası, makas kağıdı, kağıt taşı yener.\nİlk iki turu kazanan oyunu kazanır.")
    print("Oyundan çıkmak için 'x' tuşuna basabilirsiniz.\n")

    # Oyundaki seçenekler listesi
    secenekler = ["taş", "kağıt", "makas"]

    while True:  #Oyunun ana döngüsü
        oyuncu_galibiyet = 0  #Oyuncunun galibiyet sayısı
        bilgisayar_galibiyet = 0  #Bilgisayarın galibiyet sayacı
        oynanan_tur = 0  #Oynanan tur sayısı

        while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:  #Oyuncu ya da bilgisayar iki galibiyete ulaşana kadar döngü devam eder
            oyuncu_secimi = input("İlk hamlenizi seçiniz (taş, kağıt, makas): ").lower()

            if oyuncu_secimi == 'x':  #Oyundan çıkış
                print("Oyundan çıkılıyor :(")
                return

            if oyuncu_secimi not in secenekler:  #Hatalı giriş yapılması durumunda oyuncudan geçerli bir seçenek girmesi istenir
                print("HATALI GİRİŞ!\nTaş, kağıt, makas seçeneklerinden birini seçiniz!")
                continue

            bilgisayar_secimi = random.choice(secenekler)  #Bilgisayar taş kağıt makas seçeneklerinden birini rastgele seçer
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            oynanan_tur += 1  #Oynanan tur sayısı bir artırılır

            #Oyuncu ve bilgisayarın seçimine göre kazanan ya da beraberlik belirleme
            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif oyuncu_secimi == "tas" and bilgisayar_secimi == "makas":
                print("Kazandınız!")
                oyuncu_galibiyet += 1  #Oyuncunun galibiyetine bir eklenir
            elif oyuncu_secimi == "kagit" and bilgisayar_secimi == "tas":
                print("Kazandınız!")
                oyuncu_galibiyet += 1
            elif oyuncu_secimi == "makas" and bilgisayar_secimi == "kagit":
                print("Kazandınız!")
                oyuncu_galibiyet += 1
            else:
                print("Kaybettiniz.")
                bilgisayar_galibiyet += 1  #Bilgisayarın galibiyetine bir eklenir

            #Skorlar ve oynanan turun yazdırılması
            print(f"SKOR\nSiz: {oyuncu_galibiyet}\nBilgisayar: {bilgisayar_galibiyet}")
            print(f"Oynanan tur sayısı: {oynanan_tur}")

        #Kazananı belirleme
        if oyuncu_galibiyet == 2:
            print("Oyunu kazandınız!")
        else:
            print("Oyunu bilgisayar kazandı.")
        print(f"Oynanan tur sayısı: {oynanan_tur}")

        #Oyuncuya oyuna devam edip etmemek istediğinin sorulması
        oyuna_devam = input("Oyuna tekrar başlamak ister misiniz? (evet/hayır): ").lower()

        if oyuna_devam != "evet":
            print("Oyun bitti! Tekrar görüşmek üzere.")
            break  # Oyun sona erdi

tas_kagit_makas()
