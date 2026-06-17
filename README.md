# PyLearn
Projek 90 hari untuk menguasai python.

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