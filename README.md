# PyLearn
Projek 90 hari untuk menguasai python.

## Day 21:
Belajar: OOP & dasar class (class/object, __init__() method, dan parameter self)
```python
class MyClass:
    x = 255
p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)
```
### Materi:
**OOP Object Oriented Programing:**<br>
Python adalah bahasa yang berorientasi objek, yang memungkinkan untuk menyusun kode menggunakan class dan object untuk pengorganisasian dan penggunaan kembali yang lebih baik. Ini memberikan keunggulan:
1. Membuat struktur yang jelas pada program
2. Membuat kode lebih mudah dipelihara, digunakan kembali dan di-debug
3. Menjaga kode supaya tetap DRY (Don't Repeat Yourself (kode tidak ditulis berulang))
4. Membuat aplikasi dengan kode yang elbih sedikit<br>
**Class/Object:**<br>
Class adalah sebuah cetak biru untuk membuat objek.<br>
Analogi: buah (class), apel, pisang, nanas, semangka, pepaya (objek)
**__init__ method:**<br>
Init method adalah sebuah fungsi yang akan dijalankan otomatis saat class disiapkan.Method ini digunakan untuk menetapkan nilai pada properti objek.
**self parameters:**<br>
Parameter self adalah referensi yang merujuk pada 'isi' di class.<br>
Ini digunakan untuk mengakses properti dan method yang ada dimiliki class tersebut. Ini berguna supaya properti atau method yang akan dipilih tidak salah.
### Sumber:
[OOP](https://www.w3schools.com/python/python_oop.asp)
[Class/Object](https://www.w3schools.com/python/python_classes.asp)
[Self_parameters](https://www.w3schools.com/python/python_class_self.asp)

## Day 20:
Saya memperbaiki dan menganti nested if dengan blok match case demi keterbacaan. saya meningkatkan kemanan dengan menambahkan supaya user hanya bisa mengetikan 1 sampai 8. Versi perbaikan ini mencakup lebih banyak materi.

## Day 19:
Saya membuat sebuah mini project untuk menyegarkan kembali pemahaman saya. Project ini mencakup garis besar (inti) dari semua materi yang telah saya pelajari.

## Day 18:
Saya tidak belajar hari ini saya hanya membaca-baca ulang materi.

## Day 17:
Belajar FNUV (lagi), string Formatting, None, User input, VirtualEnv
```python
# Contoh string formatting
nama = "Udin"
umur = 20
print("Nama saya adalah {} dan umur saya adalah {}".format(nama, umur))
# atau
print(f"Nama saya adalah {nama} dan umur saya adalah {umur}")
# Contoh None
x = None
if x is None:
    print("x adalah NoneType")
# Contoh user input
nama = input("Masukkan nama Anda: ")
print(f"Nama Anda adalah {nama}")
# Contoh VirtualEnv
# VirtualEnv digunakan di luar kode, jadi tidak ada contoh kode di sini
```
### Materi:
**String Formatting:**<br>
String formatting adalah cara untuk menyisipkan nilai ke dalam string. Ada beberapa cara untuk melakukan string formatting di Python, termasuk menggunakan metode `format()` dan f-string.<br><br>
**None:**<br>
None adalah tipe data khusus di Python yang hanya memiliki satu nilai, yaitu `None`. Ini digunakan untuk menunjukkan bahwa sebuah variabel tidak memiliki nilai.<br><br>
**User Input:**<br>
User input adalah cara untuk menerima data dari pengguna melalui terminal atau konsol. Fungsi `input()` digunakan untuk membaca input dari pengguna.<br><br>
**VirtualEnv:**<br>
VirtualEnv adalah alat untuk membuat lingkungan Python yang terisolasi. Ini memungkinkan Anda untuk menginstal paket dan modul Python tanpa memengaruhi instalasi Python global Anda. Ini sangat berguna untuk mengelola dependensi proyek yang berbeda.<br><br>
### Evaluasi:
Saya sempat lupa kalau fungsi input selalu mengembalikan string, jadi saya harus mengkonversinya ke tipe data yang sesuai jika diperlukan.
### Sumber:
[String Formating](https://www.w3schools.com/python/python_string_formatting.asp)
[None](https://www.w3schools.com/python/python_none.asp)
[User Input](https://www.w3schools.com/python/python_user_input.asp)
[VirtualEnv](https://www.w3schools.com/python/python_virtualenv.asp)

## Day 16:
Belajar: JRePT (singkatan lagi), JSON, RegEx, PIP, Try-except-else-finally
```python
import json
import re
# conoth pengelolaan json
jsonitem = '{"Nama": "Udin", "Status": "WNI", "Berlaku hingga": "Seumur hidup"}'
teks = {'game': 'PGR', 'status': 'aktif'}
dictkan = json.loads(jsonitem)
jsonkan = json.dumps(teks)
# contoh regex
kalimat = "Orang di desa kan gak pake dollar"
cari = re.search('gak pake', kalimat)
if cari:
    print("Itumah yang ngomong gak pake otak")
# pip digunakan di luar kode
# contoh blok kode try
try:
    print(x)
except NameError:
    print("Gak ada var itu bang!")
except TypeError:
    print("Salah tulis kali bang")
else:
    print("Kodenya normal...:")
finally:
    print("Blok try selesai!!!")
```
### Materi:
**JSON:**<br>
JSON adalah sintaks untuk menyimpan dan bertukar data. JSON adalah teks yang ditulis menggunakan JS object notation.<br>
Konversi JSON ke Python:
1. Menggunakan fungsi loads() (jangan lupa untuk mengimpor modul json dulu)
Konversi Python ke JSON:<br>
Kita bisa mengubah tipe data primitive di Python (kecuali complex) ke JSON dan juga tipe data semua tipe data koleksi (kecuali sets dan tuple yang akan menjadi list). Dengan menggunakna fnugsi dumps().<br>
Konversi:<br>
| Python | JSON |
| :---: | :---: |
| Dict | Object |
| List | Array |
| Tuple | Array |
| Float | Number |
| None | null |

**RegEx:**<br>
regEx (regular expression) adalah urutan karakter yang membentuk pola pencarian.<br>
regex bisa digunakan untuk memeriksa apakah sebuah string punya pola pencarian yang ditentukan.<br><br>
**PIP:**<br>
Pip adalah pengelola package (paket) atua modul.<br>
Paket adalah sekumpulan file yang dibutuhkan untuk menggunkan modul.<br><br>
**Try...Except:**
Ini adalah penyelamat kode. Krena jika ditemukan suatu kesalahan dalam kode, Python akan langusng menghentikan program. Dengan blok kode ini, kita bisa mencegah hal tersebut.<br><br>
### Evaluasi:
Saya sempat megnira kalau cara penulisan JSON itu sama seperti Python (bebas untuk menggunkana kutip satu maupun dua), ternyata tidak. Dan itu sempat error. Tapi saya menyadarinya dan segera memperbaikinya.<br>
Saya juga sempat tidak memahami konsep RegEx, tapi setelah saya mencoba beberapa kode dan melihat contoh kode, saya pun jadi mengerti.
### Sumber:
[JSON](https://www.w3schools.com/python/python_json.asp)
[RegEx](https://www.w3schools.com/python/python_regex.asp)
[PIP](https://www.w3schools.com/python/python_pip.asp)
[Try...Except](https://www.w3schools.com/python/python_try_except.asp)

## Day 15:
Belajar: RAIMDM (singkatan yang saya buat sendiri), range, array, iterator, module, datetime, math
```python
import datetime
import math
# contoh range
print(list(range(1, 10, 3)))
# contoh array
mycar = ["Porche", "Lamborgini", "GTR"]
print(mycar[1])
# conoth iterator
mobil = iter(mycar)
print(next(mobil))
# contoh module
# module menggunakan kata kunci import supaya bisa digunakan seperti di atas
print(math.sqrt(32))
# contoh datetime
sekarang = datetime.datetime.now()
print(sekarang.strftime("%a"))
# contoh math
phi = math.pi
print(phi)
```
### Materi:
**Range:**<br>
Range adalah sebuah fungsi yang akan mengembalikan sebuah urutan angka yang immutable.<br>
Syntax: range(start, stop, step)<br><br>
**Array:**<br>
Sebenarnya tidak ada array di Python. Jadi sebagai gantinya, kita bisa menggunakan list untuk menggnatikan array.<br><br>
**Iterator:**<br>
Iterator adalah sebuah objek yang dapat dihitung dan dicek satu persatu. Secara teknis, iterator di python adalah sebuah objek yang menerapkan protokol iterator. Yang terdiri dari __iter__() dan __next__().<br>
Iterator dan iterable berbeda:<br>
- Iterator adalah objek yang secara teknis menerapkan protokol iterator
- Iterable adalah objek yang menghasilkan iterator seperti (list, tuple, dict, set, dan str)<br><br>
**Module:**<br>
Modul adalah sebuah 'kotak perkakas' yang bisa digunakan berkali-kali. Atau bisa dibilang modul adalah jembatan yang memungkinkan kita untuk mengakses kode dalam file lain tanpa harus copypas.<br>
Gunakan kata kunci import untuk mendeklarasikan sebuah modul.<br><br>
**Datetime:**<br>
Datetime adalah sebuah modul bawaan Python untuk bekerja dengan waktu. Karena di Python tidak ada tipe data khusus untuk menyimpan data waktu, maka datetime ini menjadi sebuah penyelamat karena bisa membuat semacam tipe data khusus untuk waktu.<br><br>
**Math:**<br>
Math adalah modul bawaan Python yang memungkinkan kita untuk melakukan operasi matematika dengan lebih kompleks dari biasanya.
### Evaluasi:
Saya sempat mengahadapi typeerror di bagian modul. Tapi setelah saya telaah sumber masalahnya, saya menemukannya dan dapat memperbaikinya. Saya juga sempat kesulitan untuk menguraikan pemahaman saya tentang materi ini. Lalu saya mencoba menggunakan AI untuk memperdalam pemahaman, dan saya pun bisa memahaminya.
### Sumber:
- [Range](https://www.w3schools.com/python/python_range.asp)
- [Array](https://www.w3schools.com/python/python_arrays.asp)
- [Iterator](https://www.w3schools.com/python/python_iterators.asp)
- [Module](https://www.w3schools.com/python/python_modules.asp)
- [Datetime](https://www.w3schools.com/python/python_datetime.asp)
- [Math](https://www.w3schools.com/python/python_math.asp)

## Day 14:
Belajar: Advance Function: decorators, lambda function, map(), filter(), sorted(), dan generator
```python
# Contoh decorator
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dipanggil.")
        func()
        print("Setelah fungsi dipanggil.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Contoh lambda function
add = lambda x, y: x + y
print(add(5, 3))
# Contoh map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
# Contoh filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Contoh sorted()
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)
# Contoh generator
def my_generator():
    for i in range(5):
        yield i
print(list(my_generator()))
```
### Materi:
**Decorator:**<br>
Decorator adalah fungsi yang digunakan untuk memodifikasi perilaku fungsi lain. Decorator menerima fungsi sebagai argumen dan mengembalikan fungsi baru yang telah dimodifikasi.<br>
**Lambda Function:**<br>
Lambda function adalah fungsi anonim yang didefinisikan menggunakan kata kunci `lambda`. Lambda function biasanya digunakan untuk operasi sederhana dan singkat.<br>
**Map():**<br>
Map() adalah fungsi built-in yang digunakan untuk menerapkan fungsi tertentu ke setiap item dalam iterable (seperti list) dan mengembalikan iterator baru dengan hasilnya.<br>
**Filter():**<br>
Filter() adalah fungsi built-in yang digunakan untuk menyaring item dalam iterable berdasarkan kondisi tertentu dan mengembalikan iterator baru dengan item yang memenuhi kondisi tersebut.<br>
**Sorted():**<br>
Sorted() adalah fungsi built-in yang digunakan untuk mengurutkan item dalam iterable. Fungsi ini mengembalikan list baru dengan item yang telah diurutkan.<br>
**Generator:**<br>
Generator adalah fungsi yang menggunakan kata kunci `yield` untuk menghasilkan nilai satu per satu. Generator memungkinkan kita untuk menghemat memori karena tidak menyimpan semua nilai sekaligus, melainkan menghasilkan nilai saat dibutuhkan.<br>
### Evaluasi:
Saya sempat mengalami kendala saat mencoba menuslikan semua itu. Letak kesalahan saya adalah saya kurang memahami konsep argument dan parameters. Saya sempat melakukan type error karena saya salah menuliskan argument. Setelah saya mencoba memahami dengan melihat contoh kode, saya jadi lebih faham dan mampu memperbaiki kesalahan saya.
### Sumber:
[W3School](https://www.w3schools.com/python/python_functions.asp)

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