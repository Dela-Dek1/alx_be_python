#!/bin/bash
number = int(input("Enter a number and see its multiplication table: "))
print(f"Multiplication Table for {number}:")
for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}")

