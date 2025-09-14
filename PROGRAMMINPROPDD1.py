
print("Nama        : Kardila Varani Barutu")
print("NIM         : 2509116009")
print("Kelas       : Sistem Informasi A")
print("Tema        : Pendataan Pekerja Perkebunan kelapa sawit")
print("Mini Project 1 Dasar Dasar Pemograman")

data_pekerja = [
    ("Asep", 670108050007, "Askep"),
    ("Hakim", 6472061123812, "Pemanen"),
    ("Attar", 6472061903070005, "Manajer")
]

data_visual = """
1. Asep, 670108050007, Askep
2. Hakim, 6472061123812, Pemanen
3. Attar, 6472061903070005, Manajer
"""

# Pendataan Pekerja Perkebunan Kelapa Sawit
# Tampilkan menu
print("menu Pekerja Perkebunan kelapa Sawit")
print("1. Tambah data Pekerja")
print("2. Tampilkan data Pekerja")
print("3. Menghapus data Pekerja")
print("4. Program dimatikan")

#input pilihan
pilihan = int(input("pilihan (1-4) : "))

# Tambah data Pekerja
if pilihan == 1:
    nama = input("masukkan nama")
    nik = int(input("masukkan nik"))
    jabatan = input("masukkan jabatan")
    pekerja = (nama, nik, jabatan)
    data_pekerja.append(pekerja)
    print("data masuk")

# Tampilkan data Pekerja
elif pilihan == 2:

    if not data_pekerja:
        print("Data tidak ditemukan")

    else:
        print("List data pekerja")
        nama, nik, jabatan = data_pekerja[0]
        print(f"1. Nama : {nama}, NIK : {nik}, Jabatan : {jabatan}")

        nama, nik, jabatan = data_pekerja[1]
        print(f"2. Nama : {nama}, NIK : {nik}, Jabatan : {jabatan}")

        nama, nik, jabatan = data_pekerja[2]
        print(f"3. Nama : {nama}, NIK : {nik}, Jabatan : {jabatan}")

# Menghapus data pekerja
elif pilihan == 3:
    print(data_visual)
    hapus = int(input("Masukkan NIK pekerja yang ingin dihapus: "))

    if hapus == 1 :
        data = data_pekerja.pop(0)
        print(f"data {data[0]} berhasil dihapus")

    elif  hapus == 2 :
        data = data_pekerja.pop(1)
        print(f"data {data[0]} berhasil dihapus")
    
    elif hapus == 3 :
        data = data_pekerja.pop(2)
        print(f"data {data[0]} berhasil dihapus")



elif pilihan == 4:  # Exit
        print("Program selesai. Terima kasih!")

else: 
    print("Input tidak valid")