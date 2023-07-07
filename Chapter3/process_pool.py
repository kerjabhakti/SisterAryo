# Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing


def antri(data):
    result = data+1
    return result


if __name__ == '__main__':
    inputs = list(range(30))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(antri, inputs)

    pool.close()
    pool.join()
    print('Jumlah antrian:',
          "\n", pool_outputs)
    print('Total Antrian Hari ini :',
          sum(pool_outputs))
