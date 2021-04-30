# Exercise 9.1

import sys

# Mendifinisakn array konstan
HARI = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')

def main():
    # Meminta user memasukan nomor hari
    nonhari = int(input("Masukan nomor hari [1..7]: "))

    if (nonhari < 1) or (nonhari > 7):
        print("Tidak ada hari ke-%s" % nonhari)
        sys.exit(1)

    print("Hari ke-%d adalah %s" % (nonhari, HARI[nonhari-1]))

if __name__ == "__main__":
    main()
