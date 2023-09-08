import math

#Menghitung Volume Tabung
#input

print("MENGHITUNG VOLUME TABUNG")


r=float(input("masukan jari-jari : "))
t=float(input("masukan tinggi : "))

pi=math.pi
V=round(pi*(r*r)*t,2)
c=22/7
L=int(2*c*r*(t+r))

opsi = int(input("Hitung Luas atau Volume : ?\nTekan 1 jika Luas\nTekan 2 jika volume\nMasukan Nomer : "))

if opsi == 1 :
    print("Luas permukaan balok adalah : ",L)
elif opsi == 2:
    print('Volume balok adalah :',V)
else:
    print("Maaf Pilihan Hanya Ada 1 Atau 2")