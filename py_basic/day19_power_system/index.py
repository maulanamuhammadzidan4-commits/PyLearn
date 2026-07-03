import json
import db as database

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
try:
    def caridasar(lanjutan):
        hasil = dasar[lanjutan.lower()]
        return hasil
    def caritingkat(tingkat, desc='ALL'):
        if desc == 'ALL':
            hasil = tingkatan[f'T{tingkat}']
            return json.dumps(hasil, indent=4, separators=('; ', ' => '))
        else:
            hasil = tingkatan[f'T{tingkat}'][desc.lower()]
            return hasil
except TypeError:
    hasil = "Error, nilai awal dan lanjut harus diisi!"

# KODE UTAMA
print('--SELAMAT DATANG DI PENJELASAN POWER SYSTEM---\nDi novel Project Lokantara.')
while used:
    print(f'Pilihan: {", ".join(pilihanAwal)}')
    usinput = input('Apa yang ingin anda ketahui? ').upper()
    dipakai = True
    if usinput not in pilihanAwal:
        print('Input itu tidak ada!')
        continue
    else:
        if usinput == pilihanAwal[2]:
            print("Terimakasih sudah menggunakan kode ini!")
            used = False
        elif usinput == pilihanAwal[0]:
            while dipakai:
                nextinput = input('Ingin melihat konsep atau sumber kekuatannya? ').upper()
                if nextinput == pilihanAwal[2]:
                    dipakai = False
                elif nextinput not in nextchoice['DASAR']:
                    print('Mohon masukkan nilai yang benar!')
                    continue
                else:
                    print(f"Ini adalah {nextinput.lower()}nya: {caridasar(nextinput)}")
                    continue
        elif usinput == pilihanAwal[1]:
            while dipakai:
                print(f'(ketik "keluar" untuk berhenti) Ada 8 tingkatan: {', '.join(nextchoice['TINGKAT'][0])}\n Keterangan: {', '.join((nextchoice['TINGKAT'][1]))}')
                lanjut = input('Lanjut? ').upper()
                if lanjut == pilihanAwal[2]:
                    dipakai = False
                    continue
                try:
                    nextinput = int(input("Ingin melihat tingkat berapa?(masukkan angka) "))
                except ValueError:
                    print('Jangan masukkan selain angka!')
                    continue
                else:
                    descinput = input('Apa keterangan yang ingin dilihat?(opsional) ')
                    if descinput == '':
                        print(f'Ini hasilnya: {caritingkat(nextinput)}')
                        continue
                    elif descinput not in nextchoice['TINGKAT'][1]:
                        print(f'Tidak ada deskripsi {descinput} di sini.')
                        continue
                    else:
                        print(f'Ini adalah {descinput}nya: {caritingkat(nextinput, descinput)}')
                        continue