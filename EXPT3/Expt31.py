# Program to print Pattern
"""
Created on Mon Feb 16 14:34:29 2026

@author: Aiman
"""

n=int(input("Enter number of rows:"))
for i in range(1,n + 1):
    for j in range(1,i + 1):
        print(j,end="")
    print()
