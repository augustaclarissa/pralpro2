#Nama : Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Struktur Kontrol Percabangan

'''Kafe Peacumber akan mengadakan event natal pada tanggal 25 Desember 2021. 
Kafe tersebut hanya akan mengeluarkan 2 menu saat itu, yaitu Green Tea dan Red Velvet. Harga Green Tea Rp 27.000 dan Redvelvet Rp 29.000.
Karena merayakan natal, maka akan ada diskon 30% untuk karyawan dan 10% untuk peserta event yang bukan karyawan.
Buatlah program untuk Kafe Peacumber!'''

#input : menu yang dipilih dan pemesan (karyawan / peserta reguler)
#proses : if, elif, else. harga asli - (harga asli *diskon)
#output : besar diskon dan total harga

print("Daftar Menu Spesial Natal :")
print("1. Green Tea")
print("2. Red Velvet")
menu = int(input("Silahkan masukkan pesanan (1 / 2): "))
gt = 27000
rv = 29000
pemesan = input("Pemesan (Karyawan / Reguler) : ")
diskonKaryawan = 0.3
diskonReguler = 0.1

if menu == 1 and pemesan == "Karyawan":
    print("Anda mendapat diskon sebesar 30%")
    print("Total harga yang harus dibayar = Rp ", gt-(gt*diskonKaryawan))
elif menu == 1 and pemesan == "Reguler":
    print("Anda mendapat diskon sebesar 10%")
    print("Total harga yang harus dibayar = Rp ", gt-(gt*diskonReguler))
elif menu == 2 and pemesan == "Karyawan":
    print("Anda mendapat diskon sebesar 30%")
    print("Total harga yang harus dibayar = Rp ", rv-(rv*diskonKaryawan))
elif menu == 2 and pemesan == "Reguler":
    print("Anda mendapat diskon sebesar 10%")
    print("Total harga yang harus dibayar = Rp ", rv-(rv*diskonReguler))
else:
    pass