# ---IF---
'''
Python mendukung kondisi logika umum dari operasi matematika:
- sama dengan, a == b
- tidak sama dengan, a != b
- kurang dari, a < b
- kurang dari atau sama dengan, a <= b
- lebih besar dari, a > b
- lebih besar dari atau sama dengan, a >= b

Kondisi-kondisi ini dapat digunakan dengan beberapa cara, salah satunya adalah dengan if statement.
'''
# if statement ditulis dengan kata kunci "if".
a = 100
b = 67
if a > b:
    print(f"{a} lebih besar dari {b}")

# Cara kerja if statement
'''
Statement if mengecek suatu kondisi yang akan menghasilkan nilai Boolean.
Jika kondisi True, kode akan dijalankan, dan jika False, kode akan dilewati
'''
if b > 0:
    print(f"{b} adalah nilai positif")

# Indentasi (spasi)
'''
Python menggunakan spasi untuk menandai blok kode dalam if statement.
Tidak seperti bahasa lain yang menggunakan kurung kurawal "{}" untuk menandai blok kode yang mana indentasi dipakai untuk keterbacaan,
Python menggunakan indentasi untuk menandai blok kodenya.
Contoh yang benar:
if a == b:
    print("Jawa")
Contoh salah:
if a == b:
print("Jawa")
Ini akan menyebabkan indentation error
'''

# Menggunakan variabel di kondisi
# Kita bisa menggunakan variabel langsung untuk menentukan nnilai booleannya
c = "Pulau Jawa"
if c:
    print(c)
'''
Jika menggunakan variabel secara langsung, maka nilai boolean yang dihasilkan akan selalu True JIKA NILAI DALAM VAR TIDAK TERMASUK YANG DI BAWAH
Variabel akan mengembalikan nilai False jika:
- tidak berisi ("", [], {}, ())
- Berisi angka 0 (dalam tipe angka apapun)
- berisi kata kunci False
'''

# Elif
'''
elif atau dalam bahasa lain ditulis else if.
"Cek ini jika sebelumnya False", itulah yang dikaakan Python untuk menggambarkan konsep elif.
Cara kerja elif adalah dengan mengecek ekspresi satu persatu dari atas ke bawah.
Dan jika satu ekspresi sudah bernilai True, maka blok kode akan dijalankan dan sisanya akan diabaikan begitu saja.
elif statement bisa digunakan sebanyak yang dibutuhkan
'''
nilai = 90
if nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 65:
    print("C")
elif nilai >= 55:
    print("D")
elif nilai >= 45:
    print("E")

# Else
# Else statement adalah status default dari sebuah percabangan if-elif-else.
angka = 33
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
elif angka == 0:
    print(f"{angka} adalah bilangan nol")
else:
    print(f"{angka} adalah bilangan ganjil")
# else statement akan dieksekusi jika semua kondisi di if statement bernilai False
# else statement juga bisa dugunakan untuk penagnanan kesalahan, validasi dan  penyediaan nilai default
pengguna = "Pierrot113"
if len(pengguna) > 0:
    print(f"Hai, {pengguna}!")
else:
    print("Error: pengguna tidak boleh kosong")

# if shorthand
'''
if statement juga bisa disingkat.
Tapi perhatikan kondisi berikut:
- singkat if statement jika kondisi yang akan dicek tidak terlalu kompleks
- singkat if statement jika ingin membuat tugas singkaat untuk satu kondisi
- jika kondisi yang akan dicek kompleks, gunakan percabangan if-elif-else biasa demi keterbacaan
'''
suhu_celcius = 25
print("Suhu sedang lebih panas!") if suhu_celcius > 27 else print("Suhu aman!")
# Ini disebut conditional expression atau lebih vamiliar disebut operator ternary
angka1 = 255
angka2 = 300
angka_terbesar = angka1 if angka1 > angka2 else angka2 if angka2 > angka1 else "sama"
print(f"Angka terbesar adalah: {angka_terbesar}")

# Logical operators
'''
Operator logika digunakan untuk menggabungkan kondisi statement.
Ada tiga operator logika:
- or, True jika salah satu kondisi True
- and, True jika semua kondisi True
- not, membalikan nilai boolean
'''
suhu, cuaca, libur = 27, "cerah", False
if not(suhu > 27) and cuaca == "cerah" and libur:
    print("Gas keluar!!!")
elif (suhu < 35 and suhu >= 20) and not(cuaca == "cerah") and libur:
    print("jangan keluar! Cuaca tidak cerah!")
elif not(suhu > 27) and cuaca == 'cerah' and not libur:
    print("Semangat sekolah bang!")
elif suhu > 35 or cuaca != "cerah" or not libur:
    print("Situasi tidak mendukung bang")

# Nested if (if bersarang)
'''
Nested if adalah if dalam if.
Nested if bekerja dengan cara mengecek if terluar dan jika if tersebut bernilai True, nested if di dalamnya akan mulai dieksekusi.
Untuk lebih jelasnya lihat contoh berikut:
'''
user = {
    'BabiLoNia6464': {
        'password': '314159',
        'premium': True
    },
    'Pierrot113': {
        'password': '852341',
        'premium': False
    },
    'DarkBlackNoirHitamKuroYami': {
        'password': '777777',
        'premium': True
    }
}
login = ['DarkBlackNoirHitamKuroYami', '777777']
if login[0] in user:
    if login[1] in user[login[0]]['password']:
        if user[login[0]]['premium']:
            print(f"Kami menyambut kedatangan anda kembali yang mulia baginda {login[0]}. Kami telah menunggu kedatangan yang mulia.")
        else:
            print(f"Selamat datang kembali {login[0]}!")
    else:
        print("Password salah!!")
else:
    print(f"Maaf, anda siapa ya tuan {login[0]}?")
'''
Terkadang nested if bisa disederhanakan menggunakan operator logika.
perhatikan contoh berikut:
'''
if login[0] in user and login[1] in user[login[0]]['password'] and user[login[0]]['premium']:
    print(f"Kami menyambut kedatangan anda kembali yang mulia baginda {login[0]}. Kami telah menunggu kedatangan yang mulia.")
elif login[0] in user and login[1] in user[login[0]]['password'] and not user[login[0]]['premium']:
    print(f"Selamat datang kembali {login[0]}!")
elif login[0] in user and login[1] not in user[login[0]]['password'] and user[login[0]]['premium']:
    print("Pw salah!")
else:
    print(f"Pengguna {login[0]} tidak ada dalam data.")
'''
catatan:
gunakan nested if jika logika internalnya kompleks atau bergantung pada kondisi eksternal
gunakan operator and jika kedua kondisi sederhana dan sama pentingnya
'''

# pass statement
'''
Pass statement adalah null operation atau operasi kosong.
Tidak akan terjadi apa-apa saat menjalankan kode ini.
'''
a = 2000
b = 1
if a > b:
    pass # Ini tidak akan memberikan apapun.

'''
Kapan menggunakannya?
gunakan pass statement jika:
- membuat struktur kode dan belum menerapkan logikanya
- statement butuh sintaks tapi tidak diperlukan aksi (output)
- sebagai placeholder untuk kode di masa depan saat pengembangan
- dalam fungsi atau class kosong yang rencananya akan diimplementasikan nanti
'''
umur = 16
if umur > 18:
    pass # Tugas: tambahkan kode kemudian
else:
    print("Masih di bawah umur")


'''pass vs comments
komentar akan diabaikan oleh Python.
Tapi pass sebenarnya adalah sebuah statement yang dieksekusi (meski tidak melakukan apa-apa).
Jadi jangan hanya menggunakan komentar untuk menandai kode yang akan dimasukkan kemudian.
Karena itu akan menyebabkan error. Contoh:
if umur > 18:
    # Masukkan kode disini
# ini akan menimbulkan indentasi error
'''

# ---Py Match---
'''
Match statement digunakan untuk melakukan tindakan berbeda berdasarkan case (kasus) yang berbeda.
Daripada menulis banyak if...else, kita bisa menggunakan match statement
sintaks:
match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block

Cara kerja:
ekspresi match dievaluasi sekali
nilai ekspresi dibandingkan dengan nilai masing-masing case
jika cocok, kode terkait aakn dieksekusi
'''
hari = 5
match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")

# Default
# gunakan underscore "_" untuk menentukan nilai default
match hari:
    case 6:
        print("Sekarang Sabut")
    case 7:
        print("Sekarang Minggu")
    case _:
        print("Sedang menunggu weekend...")
'''Note:
Gunakan underscore di akhir case, karena itu akan kompatibel dengan nilai apapun,
jadi simpan itu diakhir supaya menjadi nilai default.
'''
# Gabungkan value
# gunakan pipe charachter "|" sebagai operator or untuk memasukkan beberapa value.
match hari:
    case 1 | 2 | 3 | 4 | 5:
        print("Semangat sekolahnya bang.")
    case 6 | 7:
        print("Liburrr!!!!!!")

# If statement sebagai penjaga
# kita juga bisa menambahkan if statement untuk tambahan pengecekan kondisi. Contoh:
bulan = 6
match hari:
    case 1 | 2 | 3 | 4 | 5 if bulan == 1:
        print("Hari sekolah di bulan Januari")
    case 1 | 2 | 3 | 4 | 5 if bulan == 2:
        print("Hari sekolah di bulan Februari")
    case 1 | 2 | 3 | 4 | 5 if bulan == 3:
        print("Hari sekolah di bulan Maret")
    case 1 | 2 | 3 | 4 | 5 if bulan == 4:
        print("Hari sekolah di bulan April")
    case 1 | 2 | 3 | 4 | 5 if bulan == 5:
        print("Hari sekolah di bulan Mei")
    case 1 | 2 | 3 | 4 | 5 if bulan == 6:
        print("Hari sekolah di bulan Juni")
    case 1 | 2 | 3 | 4 | 5 if bulan == 7:
        print("Hari sekolah di bulan Juli")
    case 1 | 2 | 3 | 4 | 5 if bulan == 8:
        print("Hari sekolah di bulan Agustus")
    case 1 | 2 | 3 | 4 | 5 if bulan == 9:
        print("Hari sekolah di bulan September")
    case 1 | 2 | 3 | 4 | 5 if bulan == 10:
        print("Hari sekolah di bulan November")
    case 1 | 2 | 3 | 4 | 5 if bulan == 11:
        print("Hari sekolah di bulan Oktober")
    case 1 | 2 | 3 | 4 | 5 if bulan == 12:
        print("Hari sekolah di bulan Desember")