#!/bin/bash

size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for row in range(size):
        print("*", end="")
    print()
    row = row + 1

