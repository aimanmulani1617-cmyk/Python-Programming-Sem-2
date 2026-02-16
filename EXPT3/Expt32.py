# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 14:58:16 2026

@author: User
"""

def simple_interest(principle,rate,time):
    si=(principle*rate*time)/100
    return si

p=float(input("Enter principle amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time (in years):"))

interest = simple_interest(p,r,t)
print("Simple interest is:",interest)
