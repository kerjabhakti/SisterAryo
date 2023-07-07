from mpi4py import MPI
import random

# Inisialisasi MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Jumlah tiket Coldplay yang tersedia
total_tickets = 100

def sell_tickets(agent_id):
    global total_tickets

    # Menghitung jumlah tiket yang akan dijual oleh agen ini
    tickets_to_sell = random.randint(1, 10)
    
    # Mengurangi jumlah tiket yang tersedia
    total_tickets -= tickets_to_sell
    
    # Menampilkan informasi penjualan tiket oleh agen ini
    print("Agen", agent_id, "telah menjual", tickets_to_sell, "tiket.")
    print("Jumlah tiket tersisa:", total_tickets)

# Proses utama
if rank == 0:
    print("Penjualan tiket Coldplay dimulai!")

    # Memproses penjualan tiket oleh agen-agen lain
    for agent in range(1, size):
        comm.send(agent, dest=agent)

    # Memproses penjualan tiket oleh agen 0 (proses ini)
    sell_tickets(0)

    # Menerima laporan penjualan tiket dari agen-agen lain
    for agent in range(1, size):
        comm.recv(source=agent)

    print("Penjualan tiket Coldplay selesai!")
else:
    agent_id = comm.recv(source=0)
    sell_tickets(agent_id)
    comm.send("Laporan penjualan dari agen " + str(agent_id), dest=0)