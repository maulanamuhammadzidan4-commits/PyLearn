# ---Integer/number---
integer = 855987 # Int atau integer adalah semua angka (positif/negatif) tanpa desimal dengan panjang tak hingga
flo = 3.14159 # Float adalah bilangan apapun yang memiliki  satu atau lebih angka desimal
kompleks = 5j # Complex adalah bilangan yang berisi bilangan real dan imajiner

# konversi
a = float(integer) # Mengubah int ke float. Menghasilkan angak integer dengan satu bilangan desimal 0 di belakangnya
b = int(flo) # Mengubah float ke int. Menghasilkan angka integer dari dihapusnya semua bilangan desimal di belakangnya
c = complex(integer) # Mengubah int ke complex. Menghasilkan (int+0j)

print(a, b, c, type(a), type(b), type(c))

# ---String---
singleQuotationM = 'Hai, Dunia!' # String bisa ditandai dengan kutip tunggal maupun ganda
doubleQuotationM = "Hai, Dunia!" # Keduanya sama
print(singleQuotationM + ' ' + doubleQuotationM)

# Kata dalam kata
quotationOnQ1 = "Pria itu bilang 'Aku sudah KULIAH!!'." # Saat memasukan kata-kata dalam kata, jika menggunakan kutip ganda untuk kata utama, maka gunakan kutip tunggal untuk kata-kata yang ingin dimasukkan.
quotationOnQ2 = 'Benda kotak berwarna kuning itu selalu bilang "Aku siap! Aku siap!"' # Lakukan seperti di atas, hanya saja, balik penggunaannya.
print(f"{quotationOnQ1} \n {quotationOnQ2}")

# Kata multibaris
# Untuk membuatnya, pakai tiga tanda kutip, mau itu kutip ganda, maupun tunggal.
kata_kata_hari_ini = """
Jika kau tidak makan,
maka kau akan mati.
Begitu juga dengan
orang yang makan.
"""
kata_kata_buat_besok = '''
Yang makan aja mati,
apalagi yang gak makan.
Makannya,
kalo makan tuh,
dimakan.
'''
print(f"{kata_kata_hari_ini} \n {kata_kata_buat_besok}")

# String is Arrays
"""
String 'diperlakukan' sebagai kumpulan (sequence) dari karakter-karakter yang berurutan.
Misal, kata 'Hello' dianggap 'H', 'e', 'l', 'l', 'o'.
Yang mana bisa dimasukkan ke loop (for loop), melakukan indexing & slicing.
"""
# Contoh indexing dan slicing
hurufAwal = singleQuotationM[0] # Ini adalah contoh indexing. Hasilnya 'H'.
potonganhuruf = doubleQuotationM[1:3] # Ini adalah contoh slicing. Hasilnya "ai"

# Contoh dalam loop
for i in quotationOnQ1:
    print(i)
'''
Hasil:
P
r
i
a
 
i
t
u
 
b
i
l
a
n
g
 
'
A
k
u
 
s
u
d
a
h
 
K
U
L
I
A
H
!
!
'
.
'''

# Periksa panjang string
cek = len(kata_kata_buat_besok) # Fungsi ini akan menghitung jumlah karakter yang ada (semua huruf, angka, simbol, dan spasi)
print(cek) # Hasilnya 81

# Cek string
# Kita bisa mengecek apakah suatu kata ada dalam kumpulan kata.
print("makan" in kata_kata_hari_ini) # Blok kode ini akan menghasilkan nilai Boolean, yang nantinya bisa dimanfaatkan ke blok if dan sebagainya.
if "makan" in kata_kata_buat_besok: # Contoh penerapan di blok if.
    print("Yaudah, makan bang")
else:
    print("Mati dong bang.")
# Ini juga bisa untuk mencari apakah kata itu ada di dalam kata-kata itu. Misal:
if "tidur" not in kata_kata_buat_besok:
    print("Tinggal makan, apa susahnya sihj?!")
    print("Gak ada duit? Kan, ada ginjal.")
else:
    print("Jan begadang bang")

# Modifikasi string\
kapital = quotationOnQ1.upper() # Mengubah seluruh huruf menjadi huruf kapital
kapitil = quotationOnQ2.lower() # Mengubah seluruh huruf menjadi huruf biasa/kapitil
ganti = kata_kata_hari_ini.replace('a', 'o') # Menganti seluruh huruf 'a' menjadi 'o'.
pisah = singleQuotationM.split(',') # Memisahkan kata setelah tanda yang dipilih dalam kurung (",")
print(f"{kapital}\n{kapitil}\n{ganti}\n{pisah}")

# Penggabungan string & Format string
'''
Jika kita langsung menggabungkan string dengan variabel, itu tidak akan bisa. Misal:
umur = 17
print("Saya berumur:" + umur)
Maka kita menggunakan f-string.
'''
noTelp = 628235612534
rupiah = 17
print(f"Hubungi saya di nomor: {noTelp}") # Ini adalah contoh penggunaan f string dasar
print(f'Sekarang rupiah sudah menyentuh angka {rupiah:.3f} per satu dollar.') # F string juga bisa digunakan untuk menambahkan detail pada variabel. Haslnya jadi 17.000.
print(f"Kapa yah rupiah turun ke {17000 - 7000}...") # F string juga bisa digunakan untuk melakukan perhitungan matematika.

# Escape character
'''
Escape character memungkinkan kita untuk melakukan sesuatu yang 'ilegal' di Python.
Seperti menggunakan kutip ganda untuk kata dalam kata ("dia bilang "Saya akan lawan!".") dan lainnya.
'''
# Contoh escape char
teks = "Dia dipanggil \"Jack\" oleh teman sekampusnya dulu." # Menggunakan kutip ganda dalam kutip ganda
kalimat = 'Pria dari solo itu bilang \'saya akan lawan!\' saat berpidato di Jogja.'
print(f'{teks}\n{kalimat}') # Kode "\n" berfungsi untuk membuat garis baru.