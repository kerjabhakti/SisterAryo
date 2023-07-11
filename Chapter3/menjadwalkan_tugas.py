# Membuat list kosong untuk menyimpan jadwal dan daftar tugas
jadwal_tugas = []
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

# Menjadwalkan tugas
jumlah_tugas = len(daftar_tugas)
jumlah_hari = int(input("Masukkan jumlah hari: "))
tugas_per_hari = jumlah_tugas // jumlah_hari

# Menyusun jadwal tugas
for i in range(jumlah_hari):
    jadwal = daftar_tugas[i*tugas_per_hari:(i+1)*tugas_per_hari]
    jadwal_tugas.append(jadwal)

# Menampilkan jadwal tugas
for i, jadwal in enumerate(jadwal_tugas):
    print("Hari {}: {}".format(i+1, jadwal))