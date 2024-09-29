import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while data := file.readline():
            all_data.append(data)


if __name__ == '__main__':
    filenames = [f"./file {i}.txt" for i in range(1, 4 + 1)]
    st1 = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end1 = datetime.datetime.now()
    print(end1 - st1)

    st2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=32) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.datetime.now()
    print(end2 - st2)
