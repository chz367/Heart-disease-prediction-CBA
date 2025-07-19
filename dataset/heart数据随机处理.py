import random

import numpy as np


def load_dataset(filename):
    fp = open(filename,encoding='utf-8')
    # 存放数据
    dataset = []
    # 存放标签
    labelset = []
    for i in fp.readlines():
        print(i)
        dataset.append(i)
    random.shuffle(dataset)

    file = open('heart_heart异常数据分析2.txt', mode='a')
    for i in range(len(dataset)):
        # for j in str(i):
        file.write(dataset[i])
    file.close()
    # return dataset


if __name__ == '__main__':
    load_dataset('heart_heart异常数据分析1.txt')
    # train_seg = int(0.6 * len(dataset))
    # validate_seg = int(0.8 * len(dataset))
    # test_seg = len(dataset)
    # nodes = 5

    # file = open('heart_heart异常数据分析2.txt', mode='a')
    # file.write(dataset)
    # file.close()