import threading


def panggilan(reject):
    print('Panggilan tak terjawab sudah mencapai x{}'.format(reject))


def main():
    threads = []
    for i in range(1, 7):
        t = threading.Thread(target=panggilan, args=(i,))
        threads.append(t)
        t.start()
        t.join()

    # Menunggu semua thread selesai sebelum melanjutkan eksekusi
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
    
    