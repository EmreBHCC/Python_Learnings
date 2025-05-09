from multiprocessing import Process
import time

# İşlem fonksiyonu
def karesini_hesapla(sayi):
    print(f"{sayi} sayısının karesi hesaplanıyor...")
    time.sleep(1)  # Hesaplama uzun sürüyormuş gibi simülasyon
    print(f"{sayi}^2 = {sayi ** 2}")

if __name__ == "__main__":
    sayilar = [2, 4, 6, 8, 10]

    islemler = []

    # Her sayı için bir işlem başlat
    for sayi in sayilar:
        p = Process(target=karesini_hesapla, args=(sayi,))
        islemler.append(p)
        p.start()

    # Tüm işlemlerin bitmesini bekle
    for p in islemler:
        p.join()

    print("Tüm işlemler tamamlandı.")
