# Kullanıcıdan sayı al
sayi = int(input("Bir sayı gir: "))

# Asal mı kontrol et
if sayi > 1:
    for i in range(2, sayi):
        if (sayi % i) == 0:
            print(sayi, "asal bir sayı değildir.")
            break
    else:
        print(sayi, "asal bir sayıdır.")
else:
    print(sayi, "asal bir sayı değildir.")
