# -*- coding:utf-8 -*-

import random

def generate(count, length):
    coupon_list = []
    for i in range(count):
        re = ''
        for y in range(length):
            re += str(random.randint(1,9))
        coupon_list.append(re)

    return coupon_list

if __name__ == '__main__':
    print(generate(10,10))

