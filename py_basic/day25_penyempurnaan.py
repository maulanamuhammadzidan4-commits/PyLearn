import argparse
import os
import cowsay
class HitungKata:
    def __init__(self, teks, kata):
        self.teks = teks
        self.kata = kata
        self.hasil = self.teks.lower().count(self.kata.lower())

    def __str__(self):
        return f"Total kata {self.kata} ada: {self.hasil}"
    
    def __repr__(self):
        return f"KataDicari({self.kata}, {self.teks})"
    
parser = argparse.ArgumentParser(description='Mencari kata dari teks.')

parser.add_argument('--sumber', type=str, help='Sumber teks untuk dicari katanya.')
parser.add_argument('--kata', type=str, help='Teks yang ingin dicari.')

args = parser.parse_args()

if os.path.exists(args.sumber):
    with open(args.sumber, 'r', encoding='utf-8') as f:
        sumber_teks = f.read()

    run = HitungKata(sumber_teks, args.kata)
    cowsay.cow(run)
else:
    print(f'{args.sumber} tidak ada!')

# unutk menjalankan program ini, gunakan command line dan ketik:
# python day25_penyempurnaan.py --sumber "nama_file.txt" --kata "kata_yang_dicari"