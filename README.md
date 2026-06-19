# PyLearn
Projek 90 hari untuk menguasai python.

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
- Operator aritmatika (arithmetic operators)
- Operator penugasan (assignment operators)
- Operator ternary (ternary operator)
- Operator perbandingan (comparison operator)
- Operator logika (logical operators)
- Operator identitas (identity operators)
- Membership operators
- Bitwise operators<br>
**Precedence**<br>
- () parentheses
- ** pangkat/eksponen
- +x, -x, ~x unary plus, minus dan bitwise NOT
- *, /, //, % kali, bagi, floor division, modulus
- +, - pertambahan dan pengurangan
- <<, >> bitwise left dan right shift
- & bitwise AND
- ^ bitwise XOR
- | bitwise OR
- ==, !=, >, >=, <, <=, is, is not, in, not in
- not
- and
- or
### Evaluasi:
Saya menemukan masalah saat mendalami bitwise operator. Tapi setelah saya berhenti sejenak, saya jadi memahaminya. Dan besok saya pasti sudah memahaminya.
### Sumber
[W3School]{https://www.w3schools.com/python/python_operators.asp}

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
[W3School]{https://www.w3schools.com/python/python_booleans.asp}

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