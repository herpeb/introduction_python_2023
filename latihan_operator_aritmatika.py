# Tugas No 1
jumlah_murid = 40
matematika = 19
bahasa_inggris = 24
keduanya = 15

# matematika saja
mtk = matematika-keduanya
print(mtk)

# b.inggris saja
bing = bahasa_inggris-keduanya
print(bing)

# total yang menyukai matematika, b.inggris, dan kedunya
total = mtk+bing+keduanya
print(total)

print("{:<20}{:<20}{:<30}{:<10}".format("Matematika","Bahasa Inggris","Matematika & B. Inggris","Total Murid"))
print("{:<20}{:<20}{:<30}{:<10}".format(mtk,bing,keduanya,total))
print("Seharusnya jumlah murid adalah 40, karena baru 28 maka sisanya adalah murid yang tidak menyukai keduanya")
print("Murid yang tidak menyukai keduanya : ", int(jumlah_murid-total))

print("========================================================================")

# Tugas No 2
b = "2 buku dan 1 pensil = 6000" 
a = "2 buku dan 3 pensil = 9000" 

# mencari harga 1 pensil 
# lakukan  a - b
cari_qty_pensil = 3 - 1

cari_qty_buku = 2 - 2

cari_harga_pensil = 9000 - 6000

hasil_harga_pensil = cari_harga_pensil/cari_qty_pensil
print("Harga satu pensil adalah : ", hasil_harga_pensil)

# mencari harga buku, setelah mengetahui harga satu pensil adalah 1500 
# b = 2 buku dan 1 pensil = 6000
c = 6000 - hasil_harga_pensil
d = c / 2
print("Harga satu buku adalah : ", d)
