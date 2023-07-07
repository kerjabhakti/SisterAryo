import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time, sleep
from datetime import datetime

# mengklaim promo jasa joki akun


def cek_data(user_id, synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    sleep(1)
    now = time()
    with serializer:
        print("Akun %s telah mengklaim promo pada %s. Klaim %s diterima"
              % (user_id, datetime.fromtimestamp(now), name))


if __name__ == '__main__':
    synchronizer = Barrier(5)
    serializer = Lock()
    Process(name='Ayunasya', target=cek_data, args=(
        'Ayunasya', synchronizer, serializer)).start()
    Process(name='Amara', target=cek_data, args=(
        'Amara', synchronizer, serializer)).start()
    Process(name='Nanda', target=cek_data, args=(
        'Nanda', synchronizer, serializer)).start()
    Process(name='Rudy', target=cek_data, args=(
        'rudy', synchronizer, serializer)).start()
    Process(name='Lina', target=cek_data, args=(
        'Lina', synchronizer, serializer)).start()
