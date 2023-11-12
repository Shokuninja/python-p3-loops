#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        print(i)
        i -= 1
    
    if i == 0:
        print('Happy New Year!')

def square_integers(int_list):
    int_list = [li_item ** 2 for li_item in int_list]
    return(int_list)

def fizzbuzz():
    for i in range(100):
        lazy_i = i + 1
        if (lazy_i % 3 == 0) and (lazy_i % 5 == 0):
            print('FizzBuzz')
        elif lazy_i % 3 == 0:
            print('Fizz')
        elif lazy_i % 5 == 0:
            print('Buzz')
        else: 
            print(lazy_i)
        