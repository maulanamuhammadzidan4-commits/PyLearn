# ---SET---
# Set adalah salah satu dari 4 tipe data bawaan Python yang berfungsi untuk menyimpan berbagai item dalam satu variabel.
# Set tidak bisa diubah, tidak diindex, dan tidak diurutkan. Ditulis dengan kurung kurawal "{}"
data = {True, 1, "Rahasia", 3.14, ("Jawa", False), 18, False, 0} # Sama seperti 4 tipe lainya, set juga bisa menampung tipe data apapun.
print(data) # Karena set tidak diurutkan, maka hasil yang keluar akan acak urutannya.
'''Catatan:
Meski tidak bisa diubah, set masih bisa menghapus dan menambahkan item baru.
Set tidak memperbolehkan nilai duplikat.
Set menganggap True dan 1 sama. Sama halnya seperti False dan 0, set akan menganggapnya sebagai nilai duplikat dan hanya menampilkan nilai yang paling pertama muncul (dalam sintaks)
'''
# Access set items
# Karena set tidak diurutkan dan tidak di index, maka cara mengaksesnya berbeda.
# Kita bisa mengggunakan for loop untuk mengakses dan menampilkan isi datanya.
for i in data:
    print(i)
# Kita juga bisa menghasilkna nilai True atau False dengan mencari data dalam set
print("Rahasia" in data) # Hasil: True

# Add set item
'''Ada beberapa cara untuk menambahkan data baru:
1. add()
2. update(), dalam metode ini, kita bisa memasukkan iterable apapun
'''
char = {"Kazuma", "Subaru", "Ainz", "Tanya"}
char.add("Naofumi")
print(char, type(char))
newChar = ["Seiya", "Cid"]
char.update(newChar)
print(char, type(char))

# Remove set item
'''Ada beberapa cara untuk menghapus data yang sudah ditetapkan di set:
1. remove() atau discard() untuk menghapus satu item.
2. pop(), jika menggunakan ini, item yang dihapus acak. Karena set tidak diindex
3. clear() dan del, ini akan menghapus keseluruhan

catatan:
jika nilai yang dihapus menggunakan metode remove() tidak ada, itu akan menghasilkan error. Sementara discard tidak memberikan error
metode clear() hanya menghapus seluruh isi item, tapi del akan menghapus seluruh item beserta set itu sendiri
'''
# char.remove("Rimuru") ini akan menyebabkan error
char.remove("Seiya")
print(char)
char.discard("Rudeus")
print(char)

# Join sets
'''Cara untuk menggabungkan set:
1. union() atau simbol '|' dan update() untuk menggabungkan keseluruhan item
2. intersection() atau simbol '&' metode ini hanya menyimpan nilai duplikat (item yang sama di tiap set)
3. difference() atau simbol '-' metode ini mempertahankan item set pertama yang tidak ada di set lain.
4. symmetric_difference() atau simbol '^' untuk menggabungkan semua item kecuali item duplikat

catatan:
semua metode bekerja dengan cara menyalin item kemudian disimpan di variabel baru
semua simbol hanya bisa menggabungkan tipe data set
pada metode 2 sampai 4, kita bisa menambahkan kata kunci '_update()'. Ini akan merubah set asal
'''
iseQuart1Char = {"Megumin", "Emilia", "Albedo", "Visha"}
iseQuart2Char = {"Megumin", "Emilia", "Albedo", "Visha", "Raphtalia", "Ristarte"}
iseQuart3Char = {"Megumin", "Emilia", "Albedo", "Visha", "Raphtalia", "Alpha"}

heroine = iseQuart1Char.union(iseQuart2Char, iseQuart3Char)
print(heroine)
heroineUtama = iseQuart1Char & iseQuart2Char & iseQuart3Char
print(heroineUtama)
differenceHeroine = iseQuart2Char - iseQuart3Char - iseQuart1Char
print(differenceHeroine)
symmetricDiffHeroine = iseQuart2Char ^ iseQuart1Char ^ iseQuart3Char
print(symmetricDiffHeroine) # Ini akan mengembalilkan semua nilai kecuali 'Raphtalia' karena sifat unik operator '^'. Jika item muncul ganjil, itu akan dimasukkan, tapi kalau item muncul genap, itu akan diabaikan.

# Frozenset
# Frozenset adalah set yang tidak bisa diubah sama sekali.
# Membuatnya cukup menggunakan kata kunci frozenset.
secondHeroine = frozenset({"Aqua", "Rem", "Shalltear"})
print(secondHeroine, type(secondHeroine))

'''Catatan:
frozenset tidak bisa diubah menggunakan metode manipulasi apapun
'''