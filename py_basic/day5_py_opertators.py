# ---OPETAROS---
'''
Operator digunakan untuk melakukan operasi pada variabel dan nilai. Baik itu operasi matematika (perhitungan), perbandingan maupun lainnya.
Ada 8 operator di Python:
1. Operator aritmatika (arithmetic operators)
2. Operator penugasan (assignment operators)
3. Operator ternary (ternary operator)
4. Operator perbandingan (comparison operator)
5. Operator logika (logical operators)
6. Operator identitas (identity operators)
7. Membership operators
8. Bitwise operators
'''

# 1 Arithmetic operators
# Ini adalah operator matematika. Seperti tambah, kurang, bagi, dll.
a = 5
b = 2
print(a + b) # Operator penambahan
print(a - b) # Operator pengurangan
print(a * b) # Operator perkalian
print(a / b) # Operator pembagian
print(a % b) # Operator modulus
print(a ** b) # Operator pemangkatan
print(a // b) # Operator floor division
'''
Informasi tambahan:
1. Operator pembagian akan memberikan nilai float. Sementara modulus dan floor division memberikan nilai integer.
2. Untuk melakukan pangkat, gunakan tanda bintang dua kali (**). Bukan tanda ini (^).
'''

# 2 Assignment operators
# Operator ini digunakan untuk menetapkan nilai ke variabel
x = 5 # menetapkan kalau variabel 'x' itu berisi 5
x += 7 # sama seperti x = x + 7, hasilnya 12
x -= 2 # konsepnya sama, hasilnya 10
x *= 3 # hasilnya 30
x /= 2 # hasilnya 15.0
x //= 2 # hasilnya 7.0
x %= 2 # hasilnya 1.0
x **= 3 # hasilnya 1.0
y = 5 # menetapkan nilai dari var y. Dalam biner, 5 adalah 0101.
y &= 4 # hasilnya 4
z = 5
z |= 3 # hasilnya 7
f = 5
f ^= 4 # hasilnya 1
g = 5
g >>= 3 # hasilnya 0
h = 5
h <<= 3 # hasilnya 80
print(h := 80) # hasilnya 80

# 3 Ternary operator
# Operator ternary adalah versi ringkas dari blok if elif else. Ini adalah sintaks nya
keputusan = 'Bagus' if h > 75 else 'Biasa' if h == 75 else 'Buruk'
print(keputusan)

# 4 Comparison operator
# Operator ini digunakan untuk mebandingkan 2 nilai. Yang akan enghasilkan nilai boolean
print(a == b) # False (apakah a sama dengan b?)
print(a != b) # True (apakah a tidak sama dengan b?)
print(a > b) # True (apakah a lebih besar dari b?)
print(a < b) # False (apakah a lebih kecil dari b?)
print(a >= b) # True (apakah a lebih besar atau sama dengan b?)
print(a <= b) # False
# Operator perbandingan juga bisa di tumpuk
print(1 > a > 10) # sama seperti (1 > a and a > 10), hasilnya False

# 5 Logical operators
# Ada 3, or, and, dan not
print(a > 1 or a == 67) # logika or memberikan True jika salah satu kondisi bernilai true.
print(b > 1 and b == 2) # logika and memberikan True jika kedua nilai bernilai true
print(not(a > 1 or a == 67)) # logika not membalikan nilai boolean (True jadi False dan sebaliknya)

# 6 Identity operators
# Operator ini punya cara kerja yang mirip seperti operator '=='. Contoh
txt = ["Duh aduh memang asik", "Punya pacar tetangga", "Biaya apel pun irit"]
teks = ["Duh aduh memang asik", "Punya pacar tetangga", "Biaya apel pun irit"]
kalimat = txt
# perbandingan operator is dengan operator '=='
print(txt == teks) # Ini akan menghasilkan True karena operator ini mengecek nilai yang ada di dalamnya.
print(txt is teks) # Sementara itu, operator is akan mengembalikan nilai False. Karena operator ini engecek apakah objek yang ada di dua var itu sama atau tidak.
print(txt is not teks) # Ini menghasilak nilai True
print(txt is kalimat) # Meskipun nilainya sama, karena sebenarnya objek yang ditunjuk oleh var txt dan teks itu berbeda
'''
Informasi tambahan:
1. Perbedaan utama antara operator == dan operator is adalah:
    operator == mengecek nilai, sementara is mengecek objek
2. Operator is sebaiknya hanya digunakan untuk mengecek apakah nilai itu kosong. Seperti
    if txt is null:
'''

# 7 Membership operators
# Operasi ini digunakan untuk mengecek apakah nilai ada dalam suatu objek
mapel = ['MTK', 'IPA', 'IPS', 'PAI']
cek = 'IPA' in mapel
cari = 'IPAS' not in mapel
print(cek) # Menghasilkan True karena 'IPA' ada di list mapel
print(cari) # Menghasilkan True karena 'IPAS' tidak ada di list mapel

# 8 Bitwise operator
# Ini adalah operator yang memanipulasi data dari bilangan binernya.
'''
Ada 6 operator bitwise, yakni:
1. & (AND)
    Menentukan 1 jika kedua nilai 1
2. | (OR)
    Menentukan 1 jika salah satu nilai 1
3. ^ (XOR)
    Menentukan 1 jika nilai berbeda
4. ~x (NOT
    Membalikan semua nilai bit
5. << (Zero fill left shift)
    Geser ke kiri dengan memasukkan angka nol dari kanan dan biarkan bit paling kiri hilang.
6. >> (Signed right shift)
    Geser ke kanan dengan mendorong salinan bit paling kiri dari kiri, dan biarkan bit paling kanan hilang.
'''
d = 6
c = 3

print(d & c)
# 6 == 0110, c == 0011, hasil = 0010 == 2
print(d | c)
# hasil = 0111 == 7
print(d ^ c)
# hasil = 0101 == 5
print(~d)
# hasil -7
print(d << c)
# hasil 0000110 tambah 3 nol dari kanan = 0110000 == 48
print(d >> c)
# hasil 0110 tambah nol dari kiri = 0000 == 0

# ---Python operator precedence (prioritas operator di Python)---
# Operator precedence menjelaskan urutan pelaksanaan operasi.
'''
Urutan pelaksanaan:
1. () parentheses
2. ** pangkat/eksponen
3. +x, -x, ~x unary plus, minus dan bitwise NOT
4. *, /, //, % kali, bagi, floor division, modulus
5. +, - pertambahan dan pengurangan
6. <<, >> bitwise left dan right shift
7. & bitwise AND
8. ^ bitwise XOR
9. | bitwise OR
10. ==, !=, >, >=, <, <=, is, is not, in, not in
11. not
12. and
13. or

Jika operator punya prioritas yang sama, ekspresi dievaluasi dari kiri ke kanan
'''