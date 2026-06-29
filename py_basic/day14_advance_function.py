import functools
# ---FUNCTION---
# melanjutkan materi function, kita akan membahas tentang decorators, lambda, recursion dan generators

# decorators
'''
Decorators adalah fungsi yang digunakan untuk memodifikasi fungsi lain.
Kita bisa menggunakan decorators untuk menambahkan fungsionalitas tambahan ke fungsi yang sudah ada tanpa mengubah kode fungsi itu sendiri. Decorators biasanya digunakan untuk logging, otentikasi, validasi, dan lain-lain.
Bisa dibilang, kalau decorators adalah fungsi yang menerima parameter berupa fungsi lain, lalu mengembalikan fungsi baru yang telah dimodifikasi.
'''
def capitalize(func):
    '''Ini adalah contoh decorators. Ini akan mengubah tiap huruf menjadi kapital'''
    def kapitalin():
        '''Ini adalah inner function yang akan mengubah tiap huruf menjadi kapital'''
        return func().upper()
    return kapitalin

@capitalize # dekorator dideklarasikan menggunakan tanda '@'. Sintaks: @decorator_name
def sapa():
    return "Halo Didis"

@capitalize # dekorator juga bisa digunakan pada banyak function
def sambutan():
    return "Selamat datang di rumah kami tuan/nyonya!"

print(sapa())
print(sambutan())

# next decorators
'''
Decorators pada dasarnya adalah sebuah function.
Jadi, kita juga bisa melakukan hal yang umum dilakukan pada function, seperti menambahkan parameter, mengembalikan nilai, dan lain-lain.

Lalu, kita juga harus memerhatikan ketetapan metadata function, seperti __name__ dan __doc__. Untuk mempermudah dalam proses pemelilharaan.
Berikut adalah contoh decorators yang lebih kompleks, yang menerima parameter dan mengembalikan nilai.
'''
def editformat(desc):
    '''Ini adalah contoh decorators yang menerima parameter. Ini akan mengubah format string sesuai dengan parameter yang diberikan.'''
    def editformat(func):
        @functools.wraps(func) # Inilah yang dimaksud dengan ketetapan metadata function. Dengan menggunakan functools.wraps, kita bisa menjaga metadata function tetap sama dengan function asli.
        # Supaya kita bisa menggunakan kode di atas, kita harus mengimpor modul functools terlebih dahulu (tertera di paling atas).
        def edit(*args, **kwargs):
            '''Ini adalah contoh decorators yang mengembalikan nilai. Ini akan mengubah format string sesuai dengan parameter yang diberikan.'''
            if desc == "kapital":
                a = func(*args, **kwargs).upper()
            elif desc == "biasain":
                a = func(*args, *kwargs).lower()
            return a
        return edit
    return editformat

@editformat("kapital")
def peringatan(user, pelanggaran):
    '''Ini adlaah kode sederhana untuk memberikan peringatan kepada user yang melakukan pelanggaran.'''
    return f'{user} melakukan pelanggaran hebat. Yakni: {pelanggaran}'

print(peringatan("JujuBagaa", "Menggunakan cheat wall hack"))

def asikin(level):
    def asikin(func):
        @functools.wraps(func)
        def asik(*args, **kwargs):
            if level == "tinggi":
                a = f"Yoo bang {func(*args, **kwargs)}!"
            elif level == "rendah":
                a = f"Yo {func(*args, **kwargs)}."
            return a
        return asik
    return asikin

@asikin("tinggi") # decorators juga bisa digabungkan, dengan menumpuknya di atas function.
@editformat("kapital") # urutan eksekusi akan dimulai dari decorator yang paling dekat dengan function.
def greeting(user):
    return f"Halo, {user}"

print(greeting("Yanto"))
print(f"Perbedaan metadata function antara function yang telah dimodifikasi oleh decorators yang menggunakan functools dan yang tidak:\nTanpa functools: {sapa.__name__} - {sapa.__doc__}\nDengan functools: {peringatan.__name__} - {peringatan.__doc__}")

# lambda
'''
Lambda adalah fungsi anonim (tanpa nama) yang dapat dibuat dengan sintaksis singkat. 
Lambda biasanya digunakan untuk operasi sederhana yang hanya membutuhkan satu baris kode.
Lambda dapat menerima beberapa argumen, tetapi hanya dapat memiliki satu ekspresi.
'''
x = lambda a, b: a + b # contoh lambda function  # noqa: E731
print(x(5, 10))
'''
Lambda akan sangat kuat jika digunakan dalam fungsi.
'''
def pangkat(n):
    return lambda a: a ** n

kuadrat = pangkat(2)
kubik = pangkat(3)
print(kuadrat(15), kubik(5))

'''
Fungsi bawaan lambda:
1. map(), digunakan untuk mengubah tiap elemen (seperti dalam list). sintaks: map(function, iterable)
2. filter(), digunakan untuk menyaring element berdasarkan kondisi tertentu. dintaks: filter(fungsi_kondisi, iterable)
3. sorted(), digunakan unutk mengurutkan element. sintaks: sorted(iterable, key=fungsi_pembobot, reverse=False)
'''
angka = [3, 6, 8, 2, 1, 5, 9, 4]
kaliDua = list(map(lambda x: x*2, angka))
cariGenap = list(filter(lambda x: x%2 == 0, angka))
urutkan = list(sorted(angka, key=lambda x: x))
print(kaliDua, cariGenap, urutkan)

# recursion
'''
Recursion adalah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan masalah.
Kita harus berhati-hati saat menggunakan recursion karena dapat menyebabkan stack overflow jika tidak ada kondisi berhenti yang jelas.
Recursion biasanya digunakan untuk menyelesaikan masalah yang dapat dipecah menjadi sub-masalah yang lebih kecil, seperti perhitungan faktorial, pencarian dalam struktur data pohon, dan lain-lain.
'''
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def hitungMaju(awal, akhir):
    if awal == akhir:
        print(awal)
        print("Hitungan selesai!")
    else:
        print(awal)
        hitungMaju(awal + 1, akhir)

print(faktorial(6))
hitungMaju(0, 10)

'''Catatan:
- tiap recursion pasti punya 2 bagian, base case (yang menghentikan rekursi) dan recursive case.
- harus menetapkan base case supaya tidak fungsi tidak terus terusan memanggil dirinya sendiri yang akan menyebabkan error stack overflow.
'''
def fibonacci(n):
    # base case
    if n <= 1:
        return n
    else:
        # recursive base
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(4))

# generators
'''
Generators adalah fungsi yang bisa dihentikan dan dilanjutkan kembali, sehingga bisa menghasilkan nilai secara bertahap.
Kode dalam generator belum dieksekusi, hanya dikompilasi.
Generator menggunakan kata kunci yield untuk menghasilkan nilai, dan dapat digunakan untuk menghemat memori saat bekerja dengan data besar.
Generator hanya akan dieksekusi saat kita memintanya, sehingga bisa lebih efisien daripada membuat seluruh daftar sekaligus.
'''
def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4

for value in myGenerator():
    print(value)

# generator sebenarnya adalah function. hanya saja generator menggunakan kata kunci yield sebagai pengganti return.

def loopPanjang(n):
    for i in range(n):
        yield i

loop = loopPanjang(10000000)
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))

# generator expression
# konsepnya mirip seperti list comprehension. Hanya saja ini menggunakan tanda kurung.
generator = (x for x in range(10))
print(list(generator))

def fibonacciGenerator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

deretFibonacci = fibonacciGenerator()
for i in range(100):
    print(next(deretFibonacci))

# generators method
# send() mthod
def pesan_rahasia():
    while True:
        dapat = yield
        print(f"Pesan rahasia: {dapat}")

pesan = pesan_rahasia()
next(pesan) # siapkan generator
pesan.send(855987)
pesan.send("LKSDhonf")

# close method
def nomor():
    try:
        yield 1
        yield 2
        yield 3
        yield 4
    finally:
        print("Generator telah ditutup.")

gen = nomor()
print(next(gen))
gen.close() # menutup generator, sehingga tidak bisa digunakan lagi.