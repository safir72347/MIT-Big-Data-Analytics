#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:31:47 2020

@author: safir
"""

from models import Blog

def blog():
    b = Blog()
    print("1. Write a new blog \n2. View a blog \n3. Edit a blog \n4.Delete a blog")
    ch = int(input())
    if ch==1:
        print("Write a blog")
    elif ch==2:
        print("View a blog")
    elif ch==3:
        print("Edit a blog")
    elif ch==4:
        print("Delete a blog")
    else:
        print("Invalid input")

if __name__ == "__main__":
    blog()