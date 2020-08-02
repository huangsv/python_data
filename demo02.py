#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@project : Projcet
@License : (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@author  : huangsv
@Contact : huangsv@outlook.com
#@file   : demo02.py
#@ide    : PyCharm
#@time   : 2020-08-02 19:31:50

'''
import os
from multiprocessing import Pool
import time


def get_data_dict(txt_file):
    '''读取数据，组合成字典形式'''
    items = {}
    with open(txt_file, 'r') as f:
        data_list = list()
        data_list.append(txt_file)
        str_list = f.readlines()
        for str in str_list:
            items[str] = data_list  # key = 字符串   value = 文件名
    return items


def finishing(data_list):
    '''处理字典数据，相同key合并值为列表'''
    item = {}
    for data_dict in data_list:
        for key, value in data_dict.items():
            if key in item.keys():
                item[key] += value
            else:
                item[key] = value
    return {k: list(set(v)) for k, v in item.items()}


def save_data(data_dict):
    '''将数据写入txt文件中'''
    print(len(data_dict.keys()))
    import json
    with open('合并.txt', 'a', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    star = time.time()
    os.chdir('./demo02')
    txt_file = os.listdir()
    pool = Pool(4)
    data_list = []
    # 将所有txt文件放入进程池中
    for i in range(len(txt_file)):
        print('Read File .txt :', txt_file[i])
        data_list.append(pool.apply_async(get_data_dict, args=(txt_file[i],)).get())
    pool.close()
    pool.join()
    data_dict = finishing(data_list)
    save_data(data_dict)
    end = time.time()
    print(end-star)
