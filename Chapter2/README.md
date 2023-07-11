# Studi Kasus : Penjadwalan Tugas - Menginputkan Tugas
* Barrier

# Membuat list kosong untuk menyimpan tugass
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

![Barrier](https://github.com/kerjabhakti/SisterAryo/assets/56922640/aafcf016-54f2-44fe-86f4-fd45552d3738)

* Thread Definition

![Thread_definition](https://github.com/kerjabhakti/SisterAryo/assets/56922640/98624efd-424e-4b6a-89bc-db72c6beae7f)

* Thread name and processes

![Thread_name_and_processes](https://github.com/kerjabhakti/SisterAryo/assets/56922640/59c3f768-1e53-4ef6-bc64-6651fde3ff0b)

# Deskripsi
Pada kode program barrier.py dengan studi kasus panggilan akan menampilkan nama panggilan tidak terjawab dengan nama acak menggunakan random dan waktu tunda yg akan menunggu semua panggilan berada pada waktu yg berbeda menggunakan time, kode program thread_definition.py dan thread_name_and_processes.py 
