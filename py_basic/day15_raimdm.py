import day13_basic_function as myfungsi
from day14_advance_function import angka as myangka
import datetime
import math
# ---RAIMDM---
'''
RAIMDM adalah singkatan yang saya buat sendiri. Isinya:
Range
Array
Iterator
Module
Datetime
Math

Jadi sekarang materinya mencakup semua itu.
'''
# Range
# syntax: range(start, stop, step)
x = range(6) # ini menghasilkan urutan angka dari 0 sampai 5 (membuat 6 angka dari 0)
y = range(2, 7) # ini akan menghasilkan urutan angka yang dimulai dari 2 dan berakhir di 6
z = range(0, 10, 2) # Ini akan menghasilkan urutan angka dari 0, sampai 8 (lompat 2, jadi 9 tidak masuk)
print(list(x), list(y), list(z))
# fungsi range akan mengembalikan urutan angka yang tak berubah (immutable)
# kumpulan anka ini memiliki tipe data tersendiri yang deisebut range
print(y[4]) # kita juga bisa melakukan slicing terhadap range
print(x[:4])
print(4 in x) # dan juga semua hal yang biasanya dilakukan pada list
print(6 in x)
print(len(z))

# array
# python sebenarnya tidak punya dukungan bawaan untuk array.
# tapi kita bisa menggunakan list sebagai gantinya.
animetertonton = ["KonoSuba", "Date a Live", "Re: Zero", "Overlord", "Youjo Senki"]
print(animetertonton[1])
animetertonton.append("Dr. Stone")
animetertonton.append("Tate no Yuusha")
print(animetertonton[6])
animetertonton.pop(6)
animetertonton[5] = "JoJo Bizzare Adventure"
print(animetertonton)
for i in animetertonton:
    print(i)

# iterator
# iterator adalah objek yang bisa dihitung dan ditelusuri satu-satu
'''
secara teknis, objek disebut iterator jika menerapkan iterator protocol:
__iter__()
__next__()

Ini akan dipelajari lebih lanjut di pyclass
'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# iterator & iterable
'''
iterator adalah objek yang dapat dihitung dan ditelusuri satu persatu
iterable adalah objek yang menghasilkan iterator (list, tuple, dict, set, str)
'''
playlistanime = ("COTE", "Tensura", "Gnosia", "Mushoku Tensei") # ini iterable
iteratorgwehj = iter(playlistanime) # ini iterator
print(next(iteratorgwehj))
print(next(iteratorgwehj))
for i in iteratorgwehj:
   print(i)
for i in playlistanime:
   print(i)

# module
'''
anggaplah modul itu sama seperti library.
yang berisi kumpulan fungsi yang dapat digunakan.

modul juga tidak hanya berisi fungsi, tapi juga bisa berisi variabel dll.

cara menggunakan modul:
1. buat dulu fungsi atau sesuatu yang ingin di modulkan
2. pastikan fungsi itu ada dalam file .py
3. gunakan perintah import (seperti di awal) untuk membuat jembatan supaya bisa diakses
'''

myfungsi.login("Didz66", "67676767")
for i in myfungsi.anime_watched:
   print(i)

# datetime
'''
ini adalah modul untuk membuat tanggal sebagai objek tanggal (karena pada dasanya tanggal bukan sebuah tipe data)
'''
waktusekarang = datetime.datetime.now() # ini akan mengembalikan informasi tahun-bulan-tanggal jam:menit:detik.mikrodetik sekarang
print(waktusekarang)

tahun_tidak_gacor = datetime.datetime(2019, 12, 31)
print(tahun_tidak_gacor)

print(waktusekarang.strftime("%B")) # nama bulan lengkap
print(waktusekarang.strftime("%A")) # nama hari full

# math
'''
Python memiliki serangkaian fungsi matematika bawaan
termasuk modul matematika yang ekstensif
yang memungkinkan untuk melakukan tugas-tugas matematika pada angka.
'''
# fungsi bawaan (min(), max(), abs(), pow())
n = myangka
minimum = min(n)
maksimum = max(n)
print(minimum, maksimum)
print(abs(-8.67)) # nilai absolut (positive)
print(pow(4, 3)) # pangkat

# fungsi import (sqrt(), ceil(), floor(), .pi)
akar = math.sqrt(1024) # akar
bulatAtas = math.ceil(3.5) # bulatkan nilai ke atas
bulatBawah = math.floor(3.5) # bulatkan nilai ke bawah
phi = math.pi # nilai pi (3.141...)

print(akar, bulatAtas, bulatBawah, phi)