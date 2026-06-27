# ---FUNCTION---
# function adalah '<div>' atau pengangkut blok kode yang akan dijalankan jika fungsi itu dipanggil.
def perkalian(n, a):
    return n * a
print(perkalian(6, 7))
def sapa():
    print("Hai!")
sapa()

# argument & parameter
user = {
    "Guest": {
        'pw': "",
        'prem': False
    },
    "Idingz22": {
        'pw': 'jawaJawirIreng',
        'prem': True
    },
    "Yant00!": {
        'pw': 'aLAMANKKK',
        'prem': False
    }
}
def login(usName, pw): # usName dan pw adalah parameter
    if usName in user:
        if pw == user[usName]['pw']:
            if user[usName]['prem']:
                sapa = f"Selamat datang kembali yang mulia {usName}. Kami selalu menunggu kedatangan anda."
            else:
                sapa = f"Selamat datang kembali {usName}."
        else:
            sapa = "Password salah."
    else:
        sapa = "Anda siapa ya?"
    print(sapa)

def premAcc(usName = "Guest"): # kita juga bisa menetapkan nilai isi default dari parameter
    user_name = usName
    premium_access = user[usName]['prem']
    if premium_access:
        akses = f"{user_name} berhak mengakses fitur premium!"
    else:
        akses = f"{user_name} tidak punya hak untuk mengakses fitur premium!"
    print(akses)

userName = user.keys()  # contoh: GLOBAL scope (di luar fungsi)

def uraikanDaftar(daftar):
    for i in daftar:
        print(i)

def cekPrem(usName):
    if usName in user:
        if user[usName]['prem']:
            print(f'{usName} sudah Prem!!')
        else:
            print(f'{usName} belum prem!')
    else:
        print(f"Tidak ada {usName} di sini!")

login('Idingz22', 'jawaJawirIreng') # isi dalam tanda kurung adalah argument
login('Udingssz11', 'ikanHiu Mukbang timunm') # ini disebut positional 
login(pw = 'aLAMANKKK', usName = 'Yant00!') # ini disebut keyword argument atau disingkat kwargs
login('Yant00!', 'apa ya?')
premAcc("Idingz22")
cekPrem("jajang111")
premAcc()
uraikanDaftar(userName) # kita bisa memasukkan tipe data apapun dalam argumen

def daftar(database, usName, /, *, pw, prem = False):
    '''positional arg (, /) dan kwarg (*, ) juga bisa ditentukan di parameternya.
    
    artinya, tiap sebeulm simbol /, argument harus posotional
    dan setelah simbol *, argumen harus keyword
    '''
    database.update({usName: {'pw': pw, 'prem': prem}})
    return "Proses daftar selesai!"

daftar(user, "jajang111", pw = "Hyton", prem = False) # positional arg dan kwarg juga bisa digabungkan.
premAcc("jajang111")

# argument *args & **kwargs
# args adalah singkatan arbitrary argument
# kwarg adalah singkatan arbitrary keyword argument

# args
def tambahList(database, *item):
    # *args memungkinkan kita untuk menerima banyak argumen positional.
    database.extend(item)
    print(type(item), type(database)) # *args akan menjadi tuple yang berisi semua argumen yang diteruskan.
    print(database)
    return "Item berhasil ditambahkan!"

def total_rata_maximum_minimum(*angka):
    n = angka
    if len(n) == 0:
        return 0, 0, 0, 0
    else:
        def total():
            total = 0
            for num in n:
                total += num
            return total
        def rata():
            return total() / len(n)
        def maxim():
            max_num = n[0]
            for num in n:
                if num > max_num:
                    max_num = num
            return max_num
        def minim():
            min_num = n[0]
            for num in n:
                if num < min_num:
                    min_num = num
            return min_num
        
        total_nilai = total()
        rata_rata_nilai = rata()
        nilai_max = maxim()
        nilai_min = minim()
        
        return total_nilai, rata_rata_nilai, nilai_max, nilai_min

list_buah = []
list_anime = []
print(total_rata_maximum_minimum(12, 34, 67, 11, 10, 5))
print(total_rata_maximum_minimum(6))
tambahList(list_buah, "Apel", "Manggis", "Pisang", "Mangga")
tambahList(list_anime, "KonoSuba", "Re Zero", "JoJo Kimyou na Bouken")

print(list_anime, list_buah)

# kwargs
def daftarAnime(database, **anime): # **kwargs memungkinkan kita untuk menerima banyak argumen keyword
    database.update(anime)
    print(type(anime), type(database)) # **kwargs akan menjadi dictionary yang berisi semua argumen yang diteruskan.
    print(database)
    return "Anime berhasil ditambahkan!"

anime_watched = {}
daftarAnime(anime_watched, KonoSuba = {'alter title': 'Kono Subarashii Sekai ni Shukufuku wo!', 'char': ["Aqua", "Megumin", "Darkness", "Kazuma"], 'full name': ("Aqua", "Megumin", "Lalatina Dustiness Ford", "Kazuma Satou"), 'genre': ["Comedy", "Fantasy", "Isekai"]}, ReZero = {'alter title': 'Re: Zero Kara Hajimaru Isekai Seikatsu', 'char': ["Subaru", "Emilia", "Beako", "Patrasche"], 'full name': ("Natsuki Subaru", "Emilia", "Beatrice", "Patrasche"), 'genre': ["Drama", "Fantasy", "Isekai"]})
print(anime_watched)

# scope variable
'''
Scope variable adalah area dimana variable itu bisa diakses. Ada 2 jenis scope variable, yaitu
1. Local scope, yaitu variable yang hanya bisa diakses dalam fungsi itu sendiri.
2. Global scope, yaitu variable yang bisa diakses di seluruh program.
'''

# local scope
def local_scope():
    local_var = "Ini adalah local variable"
    print(local_var) # local variable hanya bisa diakses dalam fungsi itu sendiri.
# global scope
global_var = "Ini adalah global variable"

# global keyword
def global_scope():
    global global_var # jika ingin mengubah nilai global variable, kita harus menggunakan keyword global
    global_var = "Ini adalah global variable yang diubah"
    print(global_var) # global variable bisa diakses di seluruh program.

# nonlocal keyword
def outer_function():
    outer_var = "Ini adalah outer variable"
    def inner_function():
        nonlocal outer_var # jika ingin mengubah nilai outer variable, kita harus menggunakan keyword nonlocal
        outer_var = "Ini adalah outer variable yang diubah"
        print(outer_var) # outer variable bisa diakses di seluruh fungsi dalam fungsi itu sendiri.
    inner_function()
    print(outer_var) # outer variable bisa diakses di seluruh fungsi dalam fungsi itu sendiri.

# closure
def outer_function_closure():
    outer_var = "Ini adalah outer variable"
    def inner_function_closure():
        print(outer_var) # inner function bisa mengakses outer variable
    return inner_function_closure # inner function dikembalikan sebagai nilai dari outer function

# the LEGB rule
'''
LEGB adalah singkatan dari Local, Enclosing, Global, Built-in. Ini adalah aturan yang digunakan Python untuk menentukan urutan pencarian variable.
1. Local: Python akan mencari variable di local scope (dalam fungsi itu sendiri)
2. Enclosing: Jika tidak ditemukan, Python akan mencari variable di enclosing scope (fungsi yang membungkus fungsi itu sendiri)
3. Global: Jika tidak ditemukan, Python akan mencari variable di global scope (di seluruh program)
4. Built-in: Jika tidak ditemukan, Python akan mencari variable di built-in scope (di dalam Python itu sendiri)
'''
x = "Global"
def outer_function_LEGB():
    x = "Enclosing"
    def inner_function_LEGB():
        x = "Local"
        print(f"Inner: {x}") # Local
    inner_function_LEGB()
    print(f"Enclosing: {x}") # Enclosing
outer_function_LEGB()
print(f"Global: {x}") # Global