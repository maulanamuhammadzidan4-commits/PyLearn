# -----LISTS-----
# List adalah satu dari 4 tipe data bawaan Python untuk menyimpan kumpulan data.
# List dibuat menggunakan kurung siku "[]"
list_mapel = ["Matematika", "IPA", "IPS", "PAI", "Sejarah"]
# Item dalam list diurutkan, dapat diubah, dan memungkinkan nilai duplikat
# Item dalam list diindeks, dimulai dai [0]
print(list_mapel[0] + list_mapel[1]) # Hasilnya Matematika dan IPA
# Karena item disimpan dalam index, maka itu memungkinkan nilai yang duplikat
buah = ['apel', 'tomat', 'pisang', 'tomat', 'semangka']
# Untuk mengetahui panjang list, gunakan fungsi len()
print(len(buah)) # Hasilnya 5
# Item dalam list bisa berupa tipe data apapun. Bahkan list itu sendiri
contohList = ["Judul", 67, True, ["Gacor", False, 13], "Penutup"] # List dalam list disebut nested list

# Access list
# Untuk mengakses list, kita bisa langsung memilih indexnya (list[0]), ataupun menggunakan operator slice
print(contohList[2])
print(contohList[3:5])
print(contohList[-1]) # Kita juga bisa mengggunakan index min. Ini akan mengambil nilai paling akhir.

# Cek jika item ada
# Kita bisa mengecek apakah suatu nilai ada dalam list. Kita operator membership "in"
cek = "Matematika" in list_mapel
print(cek)

# Ubah item list
contohList[3][1:3] = True, 7 # Kita bisa mengubah nilai dalam list menggunakan cara ini. Ini akan mengubah data dari index yang dipilih dan menghapus data sebelumnya
list_mapel.insert(-1, "Bahasa Indonesia") # Maupun dengan menggunakan fungsi insert(). Fungsi ini mengganti isi data dari index yang dipilih tanpa mengganti isi data (data sebelumnya akan bergeser)
print(contohList)
print(list_mapel)

# Menambahkan item
list_mapel.append("Basa Sunda") # Kita bisa menambahkan item menggunakan fungsi append(). Fungsi ini akan menambahkan item ke akhir list.
contohList.insert(0, "Jawa") # Kita juga bisa menggunakan fungsi insert untuk menambahkan item
pengangkutContoh = []
pengangkutContoh.extend(buah + contohList) # Fungsi extend digunakan untuk menggabungkan 2 atau lebih list
print(list_mapel)
print(contohList)
print(pengangkutContoh)

# Menghapus list
list_mapel.remove("Sejarah") # Menghapus item yang isinya 'Sejarah'. Jika ada nilai duplikat, maka fungsi ini hanya menghapus index pertama.
contohList.pop(3) # Menghapus item berdasarkan index. Jika dalam kurung dikosongkan, itu akan menghapus seluruh isi dalam list
del buah[4] # Sama seperti pop(), tapi jika tidak menggunakan kurung siku (dikosongkan), maka itu akan menghapus listnya itu sendiri. Itu akan membuat error jika akan di print()
pengangkutContoh.clear() # Menghapus seluruh isi list, tapi listnya masih ada, dengan nilai yang kosong

print(f'{list_mapel}\n{contohList}\n{buah}\n{pengangkutContoh}')
# Loop list
# Kita bisa menampilkan isi list menggunakan loop.
for i in buah:
    print(i)

# List Comprehension
# Ini adalah versi ringkas dari for loop. Yang digunakan untuk membuat list baru yang mana isinya sama seperti list lama
newList = [x for x in buah if 'p' in x]
print(newList)
''' Syntax
[expression for item in iterable if condition == True]
'''

# Sort()
# Ini adalah fungsi untuk menyortir item dalam list secara alphanumeric(A-z, 0-9)
list_mapel.sort()
print(list_mapel)


# Copy list
list_baru = list_mapel.copy()
print(list_baru)