#!/bin/bash

X = number
Y = num
Z = product

number = int(input("Enter a number to see its multiplication table: "))

for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}")

