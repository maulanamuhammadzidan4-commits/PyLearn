# PyLearn
Projek 90 hari untuk menguasai python.

### Day 13:
Belajar: Basic Function: positional argument, keyword argument, default argument, arbitrary argument, dan scope
```python
# contoh function
def myFunction(fname, lname):
    print(f"Nama lengkap saya adalah {fname} {lname}")
myFunction("Udin", "Ujang") # positional argument
myFunction(lname="Ujang", fname="Udin") # keyword argument
```
### Materi:
**Function:**<br>
function adalah blok kode yang bisa dipanggil kapanpun dibutuhkan. Function berguna untuk mengurangi pengulangan kode, mempermudah pembacaan kode, dan mempermudah pemeliharaan kode.<br>
**Positional argument:**<br>
Positional argument adalah argumen yang harus diberikan sesuai urutan parameter yang ditentukan dalam function.<br>
**Keyword argument:**<br>
Keyword argument adalah argumen yang diberikan dengan menyebutkan nama parameter yang sesuai. Urutan argumen tidak penting.<br>
**Default argument:**<br>
Default argument adalah argumen yang memiliki nilai default jika tidak diberikan nilai saat pemanggilan function.<br>
**Arbitrary argument:**<br>
Arbitrary argument adalah argumen yang memungkinkan kita untuk menerima banyak argumen. Ada dua jenis arbitrary argument: *args (untuk positional argument) dan **kwargs (untuk keyword argument).<br>
**Scope:**<br>
Scope variable adalah area dimana variable itu bisa diakses. Ada 2 jenis scope variable, yaitu
1. Local scope, yaitu variable yang hanya bisa diakses dalam fungsi itu sendiri.
2. Global scope, yaitu variable yang bisa diakses di seluruh program.<br>
### Evaluasi:
Saya sempat mengalami kendala saat mencoba menerapkan konsep arbitrary argument. Saya sempat bingung bagaimana cara menambahkan item ke list yang sudah ada menggunakan *args. Setelah saya mencoba beberapa kali, akhirnya saya menemukan cara yang tepat untuk menambahkan item ke list menggunakan *args. Saya menggunakan method extend() untuk menambahkan item ke list yang sudah ada.
### Sumber:
[W3School](https://www.w3schools.com/python/python_functions.asp)

## Day 12:
Belajar: Looping (for dan while)
```python
# Contoh while loop
i = 1
while i < 7:
    print(i)
    i += 1

# Contoh for loop
for x in range(7):
    print(x)
```
### Materi:
**While loop**<br>
While loop adalah blok kode yang akan dijalankan selama kondisi tertentu terpenuhi. Jika kondisi tidak terpenuhi, maka blok kode akan berhenti dijalankan.<br>
**For loop**<br>
For loop adalah blok kode yang akan dijalankan untuk setiap item dalam sebuah koleksi (seperti list, tuple, string, dsb.).<br>
### Sumber:
[While loop](https://www.w3schools.com/python/python_while_loops.asp)<br>
[For loop](https://www.w3schools.com/python/python_for_loops.asp)

## Day 11:
Belajar: If statement dan Match statement
```python
# Contoh if statement
x = 10
if x > 5:
    print("x lebih besar dari 5")
else:
    print("x lebih kecil dari atau sama dengan 5")

# Contoh match statement
y = 2
match y:
    case 1:
        print("y adalah 1")
    case 2:
        print("y adalah 2")
    case _:
        print("y bukan 1 atau 2")
```
### Materi:
**IF statement**<br>
If statement adalah blok kode yang akan dijalankan jika kondisi tertentu terpenuhi. Jika kondisi tidak terpenuhi, maka blok kode lain (else) akan dijalankan.<br>
**Match statement**<br>
Match statement adalah blok kode yang akan dijalankan berdasarkan nilai dari sebuah variabel. Jika nilai variabel cocok dengan salah satu case, maka blok kode dalam case tersebut akan dijalankan. Jika tidak ada case yang cocok, maka blok kode dalam case _ (default) akan dijalankan.<br>
### Sumber:
[If statement](https://www.w3schools.com/python/python_conditions.asp)<br>
[Match statement](https://www.w3schools.com/python/python_match.asp)

## Day 10:
Belajar: Dictionary
```python
# Contoh dictionary
myDict = {
    "nama": "Udin",
    "umur": 20,
    "kota": "Bandung"
}
print(myDict["nama"])
```
### Materi:
- Sintaks dictionary
- Aturan dictionary
- Cara mengakses dictionary
### Sumber:
[W3School](https://www.w3schools.com/python/python_dictionaries.asp)

## Day 9:
Mengulas materi
### Materi
Saya mengulas semua materi dari day 1 hingga day 8 dengan menggunakan sebuah mini project yang mewakili 80% materi.

## Day 8:
Belajar: Set dan Frozenset
```python
# Contoh set
mySet = {"Jawa", "Madura", "Bandung"}
print(mySet)
# Contoh frozenset
myFzSet = frozenset({"Jakarta", "Yogyakarta", "IKN"})
print(myFzSet)
```
### Materi:
- Sintaks set dan frozenset
- Aturan set dan frozenset
- Sifat unik operator '^'
### Evaluasi:
Saya sempat kebingungan oleh methode symmetic_difference (lebih tepatnya simbolnya '^'). Yang saya pikirkan, output yang diberikan akan berisi 2 saja (lihat di kode), ternyata saya salah. Karena sifat unik dari simbol '^' yang membuat item yang muncul dengan bilangan ganjil akan dimasukkan, sementara item yang muncul dengan bilangan genap baru diabaikan.
### Sumber:
[W3School](https://www.w3schools.com/python/python_sets.asp)

## Day 7:
Belajar: Tuple
```python
# Contoh tuple
user = ("Udin", "Ujang", "Budi", "Ucup")
print(user[2])
```
### Materi:
- Sintaks tuple
- Aturan dalam tuple
### Evaluasi:
Karena pada dasarnya tuple mirip dengan list (hanya saja tuple itemnya tidak bisa diubah), jadi saya hanya membuat ringkasan singkat tentang sintaks dan aturannya.
### Sumber:
[W3School](https://www.w3schools.com/python/python_tuples.asp)

## Day 6: Py Lists
Belajar: Cara menggunakan, dan mengubah-ubah isi list
```python
# Contoh kode
buah = ['apel', 'semangka', 'kiwi', 'pir']
buah_favorit = [x for x in buah if 'p' in x]
print(buah_favorit)
```
### Materi:
- Cara mengakses list
- Cara menambahkan item ke list
- Cara menduplikasi list
- Cara menghapus isi dan list itu sendiri
### Sumber
[W3School](https://www.w3schools.com/python/python_lists.asp)

## Day 5: Python Operators
Belajar: 8 operator python dan prioritasnya

```python
beruntung = [7, 8, 9]
sial = [4, 13, 17]
if 8 in sial:
    print("Sepertinya aku sedang sial")
else:
    print("Aku representasi dewi Fortuna!")
```
### Materi:
**Operators**<br>
* Operator aritmatika (arithmetic operators)
* Operator penugasan (assignment operators)
* Operator ternary (ternary operator)
* Operator perbandingan (comparison operator)
* Operator logika (logical operators)
* Operator identitas (identity operators)
* Membership operators
* Bitwise operators<br>
**Precedence**<br>
* () parentheses
* ** pangkat/eksponen
* +x, -x, ~x unary plus, minus dan bitwise NOT
* *, /, //, % kali, bagi, floor division, modulus
* +, - pertambahan dan pengurangan
* <<, >> bitwise left dan right shift
* & bitwise AND
* ^ bitwise XOR
* | bitwise OR
* ==, !=, >, >=, <, <=, is, is not, in, not in
* not
* and
* or
### Evaluasi:
Saya menemukan masalah saat mendalami bitwise operator. Tapi setelah saya berhenti sejenak, saya jadi memahaminya. Dan besok saya pasti sudah memahaminya.
### Sumber
[W3School](https://www.w3schools.com/python/python_operators.asp)

## Day 4: Boolean
Belajar: isi dari boolean, pemanfaatan nilai boolean dalam blok if, dan evaluasi nilai menggunakan fungsi bool()

```python
benar = True
if benar:
    print("Ya ya saya setuju")
else:
    print("Saya akan lawan!")
```
### Materi:
**Boolean**<br>
Boolean mewakili nilai True dan False.<br>
**If statement**
Kita bisa memanfaatkan boolean untuk keperluan logika dalam blok kode if. Seperti untuk mengecek apakah harga barang pas di kantong atau tidak.<br>
**Bool() function**<br>
Fungsi ini berfungsi untuk mengevaluasi nilai apapun yang akan mengembalikan nilai True atau False.<br>
Nilai yang memiliki isi (tidak kosong) dalam bentuk apapun akan mengembalikan nilai True (kecuali dalam beberapa kasus). Begitu juga untuk nilai False.<br>
**Sumber:**
[W3School](https://www.w3schools.com/python/python_booleans.asp)

## Day 3: String and Integer
Belajar: tipe data int, dan fleksibilitas string

```python
txt = f"Para pejabat itu seakan tidak peduli pada nilai mata uang yang telah menyentuh {10000 + 7550} per dolarnya." # Ini adalah contoh pengabungan string dan int
txt2 = 'Kapan yah mata uang turun?'
print(f'{txt}\n{txt2}') # Ini adalah contoh penggunaan f string
```
### Materi:
**Number**<br>
Number adalah angka. Ada 3 jenis angka di Python:<br>
- Integer (int): Adalah semua bilangan (posiitf/negatif) tanpa angka desimal di belakangnya dengan panjang tak hingga
- Float: Adalah semua bilangan dengan satu atau lebih angka desimal di belakangnya.
- Complex: Adalah bilangan yang berisi bilangan real dan bilangan imajiner (yang dilambangkan huruf 'j')<br>
**String**<br>
String bisa ditandai dengan tanda kutip tunggal ('), maupun ganda (") (keduanya sama).<br>
String juga diperlakukan sebagai kumpulan dari karakter-karakter yang berurutan. Yang membuat string bisa dimasukkan ke loop (for loop), melakukan indexing dan slicing.<br>
**Sumber:**<br>
- [Number](https://www.w3schools.com/python/python_numbers.asp)
- [String](https://www.w3schools.com/python/python_strings.asp)

## Day 2: Python Variable
Belajar: aturan pembuatan variabel, multiple values, output variabel, dan variabel global

```python
x = 5 # Ini adalah contoh pendeklarasian variabel. Variabel ini juga adalah variabel global
a, b, c = "jawa", "Kalimantan", "Papua" # Ini adalah contoh multiple values
print(a, b, c) # Ini adalah contoh output variabel
```
### Materi:
**Variabel**<br>
Variabel adalah wadah untuk menyimpan data.<br>
**Aturan Pembuatan Variabel**<br>
- Harus diawali oleh huruf atau underscore "_"
- Tidak boleh diawali angka
- Nama variabel hanya berisi karakter alfanumerik dan underscore (A-z, 0-9, dan _)
- Nama variabel peka terhadap huruf besar dan kecil (case sensitive)
- Nama tidak boleh berupa kata kunci Python (seperti print, def, class, dsb.)<br>
**Multiple Values**<br>
Multiple values memungkinkan kita untuk menyimpan beberapa data ke beberapa variabel sekaligus (dalam satu baris), memasukan satu data ke beberapa variabel sekaligus dan bisa untuk mengekstrak data dari list (unpacking).<br>
**Output**<br>
Output adalah cara kita untuk menampilkan hasil. Kita menggunakan statement print().<br>
**Variabel Global**<br>
Variabel global adalah variabel yang dibuat di luar fungsi (seperti pada contoh).<br>

**Sumber:** [W3School](https://www.w3schools.com/python/python_variables.asp)

## Day 1: Python Syntax
Belajar sintaks dasar

```python
# komentar
c = "Hello World"
print(c)
```

### Materi:
* Output: Menggunakan statement print
* Variabel: Cukup menuliskan nama variabel lalu diikuti data
* Komentar: Diawali dengan simbol tag/pagar (#)
* String: Data untuk teks
* Number: Data untuk angka
* Boolean: Logika dasar (benar/salah) <br>

**Sumber:** [W3School](https://www.w3schools.com/python/)