# ---LOOPS---
'''
Ada dua jenis primitive loop di Python:
1. While loop
2. For loop
'''
# ___while loop___
i = 1
# while loop ditulis menggunakan kata kunci while
while i < 7:
    print(i)
    i += 1 # jangan lupa tambahkan var i supaya tidak terjadi infinity
'''
while loop bekerja dengan cara mengecek apakah suatu kondisi itu True.
Jadi kita bisa memasukkan nilai boolean secara langsung. Tapi ini akan mengakibatkan infinity loop.
Jadi jika kondisi sudah bernilai False, loop akan berhenti.
'''

# ___for loop___
# for loop ditulis menggunakan kata kunci for
for x in range(7): # loop ini akan menghasilkan urutan angka dari 0 hingga 6, bukan 7. Karena bisa dibilang loop ini akan membuat urutan angka sebanyak 7 angka. bukan dari 0 ke 7.
    print(x)
# for loop digunakan untuk mengulang suatu urutan (list, tuple, sets, dictionary, bahkan string)
# dalam for loop kita dapat mengeksekusi serangkaian statement dalam tiap item dalam urutan
tuple_tontonan = ("Tensura season 4", "Kanata no Astrea", "Re: Zero season 4", "Absolute Duo")
for i in tuple_tontonan:
    print(i)

for i in "Jawa":
    print(i)

# break statement
# break statement digunakana untuk menghentikan loop seketika.
# break statement bisa digunakan di tiap jenis loop.
while True:
    print("Jawa")
    break
for i in "Sumatra":
    print(i)
    break
# break statement juga bisa dijalankan jika suatu kondisi terpenuhi. Kita mengtgunakan if statement
k = 0
while not False:
    print(k)
    k += 1
    if k == 15:
        break
for x in "Pasangrahan":
    if x == "g":
        break
    else:
        print(x)

# continue statement
# continue statemet digunakan untuk melewati iterasi terkait.
# cara penggunaannya mirip seperti break statement
bilanganGenap = 0
while bilanganGenap < 55:
    bilanganGenap += 2
    if bilanganGenap == 44:
        continue # bilangan 44 akan dilewati.
    print(bilanganGenap)
for i in tuple_tontonan:
    if i == "Re: Zero season 4":
        print("Re: peak 4 dah selesai ditonton")
        continue
    print(i)

# else statement
# else statement akan dijalankan jika loop sudah selesai.
h = 0
while h < 6:
    print(h)
    h += 1
else:
    print("h sudah tidak kurang dari 6")

for i in range(8):
    print(i)
else:
    print("Loop sudah terjadi 8 kali")

# range function
# range function biasanya digunakan pada for loop untuk menghasilkan urutan angka.
'''
range function bisa digunakan dengan 3 cara:
1. range(stop) -> menghasilkan urutan angka dari 0 hingga stop-1
2. range(start, stop) -> menghasilkan urutan angka dari start hingga stop-1
3. range(start, stop, step) -> menghasilkan urutan angka dari start hingga stop-1 dengan step tertentu
'''
# Contoh kode
for i in range(5):
    print(i) # Hasil: 0, 1, 2, 3, 4

for i in range(2, 5):
    print(i) # Hasil: 2, 3, 4

for i in range(2, 10, 2):
    print(i) # Hasil: 2, 4, 6, 8