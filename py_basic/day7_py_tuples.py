# -----TUPLE-----
# Tuple adalah salah satu dari 4 tipe data bawaan Python untuk menyimpan kumpulan data
'''
Pada dasarnya, tuple mirip dengan list. Hanya saja, item dalam tuple tidak dapat diubah.
Ditulis dengan tanda kurung "()". Jika ingin membuat tuple dengan hanya 1 item, harus, harus ditambah koma supaya terdeteksi sebagai tuple. Contoh
tuple = ("Jawa",).
Karena tuple pada dasarnya mirip dengan list, maka seluruh operasi seperti loop, slice dll (kecuali operasi untuk mengubah item), bisa dilakukan.
'''
# Contoh kode
myTuple = ("Kubis", True, 67, ["Dimas", 5j, False])
# Ini akan menyebabkan error:
# myTuple[0] = "Jawa"
# Karena tuple tidak mendukung adanya perubahan (tuple tidak mendukung item assignment)
print(myTuple[:3]) # Hasil: ('Kubis', True, 67)

''' Karena tuple bersifat tidak bisa ditubah, saya menemukan potensi penggunaan:
Tuple bisa digunakan untuk membuat kumpulan variabel tetap untuk keamanan. Seperti untuk menetapkan key untuk dictionary.
'''