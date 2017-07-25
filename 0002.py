# -*- coding:utf-8 -*-

import random
import pymysql


def generate(count, length):
    coupon_list = []
    for i in range(count):
        re = ''
        for y in range(length):
            re += str(random.randint(1,9))
        coupon_list.append(re)

    return coupon_list

def AddtoDB(coupon_list):
    db_ip = 'localhost'
    db_port = 3306
    db_sock = '/tmp/mysql.sock'
    db_user = 'coupon'
    db_pass = 'coupon'
    db_use = 'coupon'
    db = pymysql.connect(db_ip, db_user, db_pass, db_use)
    cursor = db.cursor()
    for coupon_no in coupon_list:
        cursor.execute('''INSERT INTO coupon (ID) VALUES (''' + coupon_no + ''');''')
    cursor.execute('''COMMIT;''')
    cursor.execute('''SELECT * FROM coupon;''')
    for data in cursor.fetchall():
        print(data)
    db.close()

if __name__ == '__main__':
    coupon_list = generate(10,10)
    AddtoDB(coupon_list)
