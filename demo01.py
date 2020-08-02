#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@project : Projcet
@License : (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@author  : huangsv
@Contact : huangsv@outlook.com
#@file   : demo01.py
#@ide    : PyCharm
#@time   : 2020-08-02 16:30:00

'''
import time
import os

def verify_name(name, data_list):
    '''验证重复姓名的数据'''
    if len(data_list) <= 1:
        return False
    name_list = list()
    for data_dict in data_list:
        name_list.append(data_dict['Name'])
    if name in name_list:
        return True
    else:
        return False


def get_data_dict(txt_files):
    '''读入txt数据到内存'''
    data_list = list()
    for txt_file in txt_files:
        with open(txt_file, 'r') as f:
            temp_list = f.readlines()
            for temp in temp_list:
                item = {}
                name = temp.split(',')[0]
                date = temp.split(',')[1]
                results = temp.split(',')[-1].strip()
                # 取重复姓名的最高分
                if verify_name(name, data_list):
                    for data in data_list:
                        if name == data['Name']:
                            if data['Results'] < results:
                                data['Date'] = date
                                data['Results'] = results
                        else:
                            continue
                else:
                    item['Name'] = name
                    item['Date'] = date
                    item['Results'] = results
                    data_list.append(item)
    return data_list


def set_sort_data(data_list):
    '''字典排序，先按 results，再按 Date排序'''
    from operator import itemgetter
    return sorted(data_list, key=itemgetter('Results', 'Date'), reverse=True)


def save_data(data_list):
    '''保存数据'''
    i = 1
    for data_dict in data_list:
        with open('finaly_data.txt', 'a') as f:
            f.write(str(i) + ',' + data_dict['Name'] + ',' + data_dict['Date'] + ',' + data_dict['Results'])
            f.write('\n')
            i += 1

if __name__ == '__main__':
    star = time.time()
    os.chdir('./demo01')
    txt_file = os.listdir()
    print('Read Files .txt :', txt_file)
    data_list = get_data_dict(txt_file)
    data_list = set_sort_data(data_list)
    save_data(data_list)
    end = time.time()
    print(end - star)
