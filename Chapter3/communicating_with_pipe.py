# Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing


def create_items(pipe):
    output_pipe, _ = pipe
    for antrian in range(100):
        # tambahkan
        print('Antrian Pembelian Tiket ColdPlay : '+str(antrian))
        output_pipe.send(antrian)
    output_pipe.close()


def tiket_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            jumlah_antrian = input_pipe.recv()
            print('Nomor tiket antrian yang anda dapat : ' +
                  str(jumlah_antrian + jumlah_antrian))
            output_pipe.send(jumlah_antrian + jumlah_antrian)
    except EOFError:
        output_pipe.close()


if __name__ == '__main__':

    # First process pipe with numbers from 0 to 9
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = \
        multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()

# second pipe,
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = \
        multiprocessing.Process(target=tiket_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:

            print(
                f"Kode Tiket : {pipe_2[1].recv()}")
    except EOFError:
        print("End")
