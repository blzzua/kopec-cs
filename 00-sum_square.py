#!/usr/bin/python3
""" 1) реализовать функцию возведения в квадрат натуральных чисел без умножения и возведения в степень """

def sq(x):
    row_len = 1
    square = 0
    for i in range(x):
        square += row_len
        row_len +=2
    return square

if __name__ == '__main__':
    for i in range(1,10+1):
        print(sq(i))
    
    
