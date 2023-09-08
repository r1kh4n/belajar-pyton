#menghitung luas dan volume pada balok
#input

print("Menghitung Luas Permukaan dan Volume pada balok\n")
p = int(input("masukan panjang : "))
l = int(input("masukan lebar : "))
t = int(input("masukan tinggi : "))

L = 2*(p*1 + p*t + 1*t)
V = p * 1 + t
opsi = int(input("Hitung Luas atau Volume : ?\nTekan 1 jika Luas\nTekan 2 jika volume\nMasukan Nomer : "))

if opsi == 1 :
    print("Luas permukaan balok adalah : ",L)
elif opsi == 2:
    print('Volume balok adalah :',V)
else:
    print("Maaf Pilihan Hanya Ada 1 Atau 2")
