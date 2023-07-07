from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

j_panggilan = 6 # jumlah panggilan
finish_line = Barrier(j_panggilan)
panggilan = ['Bapak', 'Ibu', 'Ade', 'Kakak', 'Kakek', 'Nenek'] # nama panggilan

def func():
    name = panggilan.pop() # mengambil nama panggilan dari antrian
    sleep(randrange(5, 10)) # menunda waktu panggilan
    print('%s Panggilan tidak terjawab pada waktu: %s \n' % (name, ctime()))
    finish_line.wait() # menunggu semua panggilan berada waktu yg berbeda

def main():
    threads = []
    print('Panggilan Masuk')
    for i in range(j_panggilan):
        threads.append(Thread(target=func))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Kamu menerima panggilan masuk tak terjawab ')

if __name__ == "__main__":
    main()
    
    
        