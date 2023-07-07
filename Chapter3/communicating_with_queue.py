import multiprocessing
import random
import time


class room(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        # pembeli adalah nama akun pelanggan
        pembeli = ["Ayunasya", "Amara", "Nanda", "Rudy", "Lina"]
        for i in range(6):
            pembelian = random.choice(pembeli)
            self.queue.put(pembelian)
            print(
                f"Process room: Akun '{pembelian}' telah ditambahkan ke dalam antrian oleh {self.name}")
            time.sleep(2)
            print(f"Nomor Antriannya adalah {self.queue.qsize()}")


class teller(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Antrian Selesai")
                break
            else:
                time.sleep(2)
                pembelian = self.queue.get()
                print(
                    f"Process Teller: Akun '{pembelian}' telah diberikan oleh {self.name}\n")
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_room = room(queue)
    process_teller = teller(queue)
    process_room.start()
    process_teller.start()
    process_room.join()
    process_teller.join()
