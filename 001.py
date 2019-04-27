# -*- coding: utf-8 -*-
'''
第一种方法直接调用函数
第二种方法创建了实例，再调用其中的方法
'''
import random

'''def random_code(filename,count=4,num=200):
    f = open(filename, mode='r+')
    s0 = ''
    s1 = '_'
    for i in range(num):
        text = []
        for j in range(count):
            current = random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',4)
            text.append(s0.join(current))

        tupl = tuple(text)
        checkcode = s1.join(tupl)
        
        f.write(checkcode+'\n')
            
if __name__ == '__main__':
    filename = 'C:/Users/m1521/Desktop/1.txt'
random_code(filename)'''
class c:
    def random_code(filename,count=4,num=200):
        f = open(filename, mode='r+')
        s0 = ''
        s1 = '_'
        for i in range(num):
            text = []
            for j in range(count):
                current = random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',4)
                text.append(s0.join(current))
    
            tupl = tuple(text)
            checkcode = s1.join(tupl)
            
            f.write(checkcode+'\n')
            
if __name__ == '__main__':
    filename = 'C:/Users/m1521/Desktop/2.txt'
    cc = c()
    c.random_code(filename)