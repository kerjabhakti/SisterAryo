# Membuat dictionary kosong untuk menyimpan waktu pengerjaan tugas
waktu_pengerjaan = {}

# Membuat list kosong untuk menyimpan tugas
daftar_tugas = []

# Menginputkan jumlah tugas
jumlah_tugas = int(input("Masukkan jumlah tugas: "))

# Menginputkan nama tugas dan menyimpannya ke dalam list
for i in range(jumlah_tugas):
    tugas = input("Masukkan nama tugas ke-{}: ".format(i + 1))
    daftar_tugas.append(tugas)

# Menampilkan daftar tugas
print("Daftar tugas:")
for tugas in daftar_tugas:
    print(tugas)

# Menginputkan waktu pengerjaan tugas
for tugas in daftar_tugas:
    waktu = float(input("Masukkan waktu pengerjaan untuk tugas {}: ".format(tugas)))
    waktu_pengerjaan[tugas] = waktu

# Menampilkan waktu pengerjaan tugas
print("Waktu pengerjaan tugas:")
for tugas, waktu in waktu_pengerjaan.items():
    print("{}: {} jam".format(tugas, waktu))

# Menghitung total waktu pengerjaan
total_waktu = sum(waktu_pengerjaan.values())
print("Total waktu pengerjaan: {} jam".format(total_waktu))