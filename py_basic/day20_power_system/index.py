import json
import db as database
import functools

# deklarasi variabel
used = True
try:
    dasar = database.dasar
    tingkatan = database.tingkat
    jsondasar = json.dumps(dasar, indent=4)
    jsontingkat = json.dumps(tingkatan, indent=4)
except (NameError, AttributeError):
    print("Gagal mengambil database!")
else:
    pilihanAwal = ['DASAR', 'TINGKAT', 'KELUAR']
    nextchoice = {
        'DASAR': ['KONSEP', 'SUMBER'], 
        'TINGKAT': [[str(x) for x in range(1, 9)], tuple(tingkatan['T1'].keys())]
}

# fungsi
# dibungkus menggunakan blok try untuk mencekah error
def perindah(func):
    @functools.wraps(func)
    def ubah(*args, **kwargs):
        hasil = json.dumps(func(*args, **kwargs), indent=4, separators=('; ', ' => '))
        return hasil
    return ubah

def caridasar(lanjutan):
    hasil = dasar[lanjutan.lower()]
    return hasil

@perindah
def caritingkat(tingkat, desc='ALL'):
    if desc == 'ALL':
        hasil = tingkatan[f'T{tingkat}']
        return hasil
    else:
        hasil = tingkatan[f'T{tingkat}'][desc.lower()]
        return hasil

# KODE UTAMA
print('--SELAMAT DATANG DI PENJELASAN POWER SYSTEM---\nDi novel Project Lokantara.')
while used:
    print(f'Pilihan: {", ".join(pilihanAwal)}')
    usinput = input('Apa yang ingin anda ketahui? ').upper()
    dipakai = True
    match usinput:
        case 'KELUAR':
            print("Terimakasih sudah menggunakan kode ini!")
            used = False
        
        case 'DASAR':
            while dipakai:
                nextinput = input('Ingin melihat konsep atau sumber kekuatannya? ').upper()
                if nextinput == pilihanAwal[2]:
                    dipakai = False
                elif nextinput not in nextchoice['DASAR']:
                    print('Mohon masukkan nilai yang benar!')
                    continue
                else:
                    print(f"Ini adalah {nextinput.lower()}nya:\n{caridasar(nextinput)}")
                    continue
        
        case 'TINGKAT':
            while dipakai:
                print(f'(ketik "keluar" untuk berhenti) Ada 8 tingkatan:\n{", ".join(nextchoice['TINGKAT'][0])}\n Keterangan:\n{", ".join((nextchoice['TINGKAT'][1]))}')
                lanjut = input("Ingin melihat tingkat berapa?(masukkan angka 1-8) ").upper()
                if lanjut == pilihanAwal[2]:
                    dipakai = False
                    continue
                try:
                    nextinput = int(lanjut)
                    if not(1 <= nextinput <= 8):
                        print("Hanya ada 8 tingkatan!")
                        continue
                except ValueError:
                    print('Jangan masukkan selain angka!')
                    continue
                else:
                    descinput = input('Apa keterangan yang ingin dilihat?(opsional) ')
                    if descinput == '':
                        print(f'Ini hasilnya:\n{caritingkat(nextinput)}')
                        continue
                    elif descinput.lower() not in nextchoice['TINGKAT'][1]:
                        print(f'Tidak ada deskripsi {descinput} di sini.')
                        continue
                    else:
                        print(f'Ini adalah {descinput}nya:\n{caritingkat(nextinput, descinput)}')
                        continue
        
        case _:
            print(f"Input {usinput} tidak ada!")