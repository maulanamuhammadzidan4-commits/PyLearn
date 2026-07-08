import os

belanjaan = open("contoh.txt") # sama seperti open('contoh.txt', 'rt'), ini akan error jika fiile tidak ada
print(f"Daftar belanjaan:\n{belanjaan.read()}") # catatan: jika menggunakan cara ini, pastikan direktori pada terminal yang digunakan untuk menjalankan kode sama dengan file yang disimpan.
belanjaan.close()

with open('contoh.txt', 'a') as daftar_belanja: # untuk menambahkan kata
    daftar_belanja.write('\nJangan lupa beli gas!')

with open('contoh.txt') as daftar_belanja:
    print(daftar_belanja.read())
    daftar_belanja.close()

sebelum_timpa = open('korban_timpa.txt').read()
print(sebelum_timpa)

with open('korban_timpa.txt', 'w') as timpa:
    timpa.write("Setelah ditimpa:\nKalo nimpa, dipikir mas")

with open('korban_timpa.txt') as lihatTimpaan:
    print(lihatTimpaan.read())
    lihatTimpaan.close()

# mode/method 'a', 'w', 'x' akan membuat file jika file tidak ada. Dan mode 'x' akan mengembalikan error jika file ada.
target_ubah = open('target.txt', 'a').write("Jawa jawa jawa jawa jawa jawa")
target_timpa = open('target_timpa.txt', 'w').write("Halah nyocot")
buat_baru = open('newfile.txt', 'x')

with open('target_timpa.txt') as lihat:
    print(lihat.read())
with open('target.txt') as nimpa:
    print(nimpa.read())
with open('newfile.txt') as baru: # kosong
    print(baru.read())

lists_snack = ['- Oero\n', '- Cetos\n', '- Roritos\n', '- Gold Queen']

with open('contoh.txt', 'ab') as tambahSnack:
    snack = f'Daftar Snack:\n{''.join(lists_snack)}'
    tambahSnack.write(snack.encode('utf-8'))

with open('contoh.txt') as lists:
    print(lists.read())

os.remove('tumbal.txt')

if os.path.exists('halah_nyocot.txt'):
    os.remove('halah_nyocot.txt')
else:
    print("File itu tidak ada!")

os.rmdir('pantek')