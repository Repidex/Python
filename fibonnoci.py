# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:54:35 2020

@author: Jitendra Parmar
"""
def fibonnoci(a):
    if a<0:
        print("Invalid")
    elif a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fibonnoci(a-1)+fibonnoci(a-2)
print(fibonnoci(7))