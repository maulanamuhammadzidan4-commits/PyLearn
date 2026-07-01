from day10_py_dictionary import anime_watched as anime
# FNUV (string formating, NoneType, user input, VirtualEnv)
# string formating
# f string
Rp = 18
teks = f"Sekarang USD telah mencapai Rp{Rp:.3f} per Dollar nya!"
print(teks)

dua_usd = f"Dua dollar berarti Rp{Rp * 2:.3f}"
print(dua_usd)

dampakrupiahturun = f"Dampak rupiah melemah adalah:\n {'Naiknya harga bahan pangan setinggi langit' if Rp >= 17 else 'Transaksi global akan sangat menyusahkan' if Rp >= 15 else 'Akan sangat sulit jika ingin membeli barang dari luar'}"
print(dampakrupiahturun)

def konversiusdkerp(usd):
    '''Ini berdasarkan data rupiah pada 4 Jun 2026'''
    return usd * 18000

print(f"Lima dollar berarti Rp{konversiusdkerp(5):,}.")
# format() function
# sebenarnya cara kerjanya sama saja, hanya saja fungsi format bisa digunakan untuk membuat format dinamis (bisa membuat template format dan mengambil data dari dict secara fleksibel)
print("Beberapa anime yang pernah saya tonton adalah {Date a Live[alter title]}".format(**anime))
templateTeks = "HP {user}: {hp}"
babiLoNia11 = templateTeks.format(user="BabiLoNia11", hp=34)
udjangdings1212 = templateTeks.format(user="Udjangdings1212", hp=60)
print(f"{babiLoNia11}\n{udjangdings1212}")
# catatan: ini adalah kelebihan yang dimiliki dungsi format(). Lebih baik gunakan f string jika ingin lebih cepat

# None
# None adalah konstanta khsus di python untuk mewakili ketiadaan nilai
x = None
print(x, type(x))

# user input
userinput = input("Mau ubah berapa dollar ke rp bang? ")
print(f"{userinput} adalah Rp{konversiusdkerp(int(userinput)):,}.") # fungsi input akan selalu memberikan hasil str. Jadi harus ubah terlebih dulu.

# VirtualEnv
'''
karena virtualenv ini tidak bisa diakses di luar folder project, maka saya tidak bisa menampilkan hasilnya. Jadi saya hanya menulis catatan ini saja.

Virtualenv adalah sebuah tool yang digunakan untuk membuat lingkungan python terisolasi.
Dengan virtualenv, kita bisa menginstal paket-paket python tertentu tanpa mempengaruhi instalasi python global di sistem kita.
Ini sangat berguna ketika kita bekerja pada beberapa proyek yang membutuhkan versi paket yang berbeda.

Cara menggunakan virtualenv:
1. Install virtualenv jika belum terpasang:
    pip install virtualenv
2. Buat lingkungan virtual baru:
    virtualenv nama_lingkungan
3. Aktifkan lingkungan virtual:
    - Di Windows:
        nama_lingkungan\Scripts\activate
    - Di macOS/Linux:
        source nama_lingkungan/bin/activate
4. Setelah lingkungan virtual aktif, kita bisa menginstal paket-paket yang dibutuhkan menggunakan pip.
5. Untuk keluar dari lingkungan virtual, cukup ketik:
    deactivate
'''