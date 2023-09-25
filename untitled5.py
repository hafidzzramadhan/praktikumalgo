# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LDMGU0UZY7u2zN7WMh9-TAYQf9V7ZdTt
"""

def create_python_banner():
    banner = """
   @   @ @@@@@  @      @@@@@@ @
   @@  @ @   @  @      @      @
   @ @ @ @@@@@  @      @@@@@  @
   @  @@ @   @  @      @
   @   @ @   @  @@@@@@ @@@@@
    """
    return banner

print(create_python_banner())
import math

def hitung_sisi():
    print("Kalkulator Pythagoras")
    print("Pilih salah satu operasi:")
    print("1. Hitung sisi a")
    print("2. Hitung sisi b")
    print("3. Hitung sisi c")

    pilihan = input("Masukkan nomor operasi yang diinginkan (1/2/3): ")

    if pilihan == "1":
        sisi_b = float(input("Masukkan sisi b: "))
        sisi_c = float(input("Masukkan sisi c: "))

        while sisi_c < sisi_b:
            print("Nilai c tidak boleh lebih kecil dari nilai b.")
            sisi_c = float(input("Masukkan sisi c: "))

        sisi_a = math.sqrt(sisi_c**2 - sisi_b**2)
        print(f"Sisi a = {sisi_a}")
    elif pilihan == "2":
        sisi_a = float(input("Masukkan sisi a: "))
        sisi_c = float(input("Masukkan sisi c: "))

        while sisi_c < sisi_a:
            print("Nilai c tidak boleh lebih kecil dari nilai a.")
            sisi_c = float(input("Masukkan sisi c: "))

        sisi_b = math.sqrt(sisi_c**2 - sisi_a**2)
        print(f"Sisi b = {sisi_b}")
    elif pilihan == "3":
        sisi_a = float(input("Masukkan sisi a: "))
        sisi_b = float(input("Masukkan sisi b: "))
        sisi_c = float(input("Masukkan sisi c: "))

        while sisi_c < sisi_a or sisi_c < sisi_b:
            print("Nilai c tidak boleh lebih kecil dari nilai a atau b.")
            sisi_c = float(input("Masukkan sisi c: "))

        sisi_c = math.sqrt(sisi_a**2 + sisi_b**2)
        print(f"Sisi c = {sisi_c}")
    else:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    hitung_sisi()

def create_python_banner():
    banner = """
   @   @ @@@@@  @      @@@@@@ @
   @@  @ @   @  @      @      @
   @ @ @ @@@@@  @      @@@@@  @
   @  @@ @   @  @      @
   @   @ @   @  @@@@@@ @@@@@
    """
    return banner

print(create_python_banner())
import math

def hitung_sisi():
    print("Kalkulator Pythagoras")
    print("Pilih salah satu operasi:")
    print("1. Hitung sisi a")
    print("2. Hitung sisi b")
    print("3. Hitung sisi c")

    pilihan = input("Masukkan nomor operasi yang diinginkan (1/2/3): ")

    if pilihan == "1":
        sisi_b = float(input("Masukkan sisi b: "))
        sisi_c = float(input("Masukkan sisi c: "))

        while sisi_c < sisi_b:
            print("Nilai c tidak boleh lebih kecil dari nilai b.")
            sisi_c = float(input("Masukkan sisi c: "))

        sisi_a = math.sqrt(sisi_c**2 - sisi_b**2)
        print(f"Sisi a = {sisi_a}")
    elif pilihan == "2":
        sisi_a = float(input("Masukkan sisi a: "))
        sisi_c = float(input("Masukkan sisi c: "))

        while sisi_c < sisi_a:
            print("Nilai c tidak boleh lebih kecil dari nilai a.")
            sisi_c = float(input("Masukkan sisi c: "))

        sisi_b = math.sqrt(sisi_c**2 - sisi_a**2)
        print(f"Sisi b = {sisi_b}")
    elif pilihan == "3":
        sisi_a = float(input("Masukkan sisi a: "))
        sisi_b = float(input("Masukkan sisi b: "))
        sisi_c = float(input("Masukkan sisi c: "))

        while sisi_c < sisi_a or sisi_c < sisi_b:
            print("Nilai c tidak boleh lebih kecil dari nilai a atau b.")
            sisi_c = float(input("Masukkan sisi c: "))

        sisi_c = math.sqrt(sisi_a**2 + sisi_b**2)
        print(f"Sisi c = {sisi_c}")
    else:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    hitung_sisi()

# Membaca tiga angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

# Menemukan angka terbesar
if angka1 >= angka2 and angka1 >= angka3:
    angka_terbesar = angka1
elif angka2 >= angka1 and angka2 >= angka3:
    angka_terbesar = angka2
else:
    angka_terbesar = angka3

# Menampilkan hasil
print("Angka terbesar adalah:", angka_terbesar)