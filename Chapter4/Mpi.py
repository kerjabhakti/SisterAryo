from mpi4py import MPI

# Data tiket konser
tickets = {
    'Coldplay': 100,
}

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def buy_tickets(name, quantity):
    if name in tickets:
        available_tickets = tickets[name]
        if quantity <= available_tickets:
            tickets[name] -= quantity
            return True
    return False

# Proses 0 menerima permintaan pembelian tiket dari proses-proses lain
if rank == 0:
    # Menampilkan jumlah tiket yang tersedia
    print(f"Available tickets: {tickets}")

    # Menerima permintaan pembelian tiket dari proses-proses lain
    for i in range(1, size):
        data = comm.recv(source=i, tag=0)
        name = data['name']
        quantity = data['quantity']

        success = buy_tickets(name, quantity)

        # Mengirim balasan ke proses yang meminta pembelian tiket
        response = {'success': success}
        comm.send(response, dest=i, tag=1)

# Proses-proses lain mengirim permintaan pembelian tiket ke proses 0
else:
    # Mengirim permintaan pembelian tiket
    request = {'name': 'Coldplay', 'quantity': 2}
    comm.send(request, dest=0, tag=0)

    # Menerima balasan dari proses 0
    response = comm.recv(source=0, tag=1)
    success = response['success']

    if success:
        print(f"Process {rank} successfully bought tickets!")
    else:
        print(f"Process {rank} failed to buy tickets.")
