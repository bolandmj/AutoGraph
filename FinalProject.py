# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:57:22 2022

@author: maxwe
"""
import numpy as np
import pandas as pd

print("Welcome to an auto grapher.")
print("This program will take to sets of data and plot this with a trend line for each set of data.")

X1 = np.array([])
Y1 = np.array([])
X2 = np.array([])
Y2 = np.array([])

Title = input("Enter the title of your graph: ")
XAxis = input("Enter the X Axis name: ")
YAxis = input("Enter the Y Axis name: ")

FirstLabel = input("Enter the name of your first set of data: ")
n = int(input("Enter number of elements for your first set of data: "))

for i in range(0, n):
    while True:
        Xnum = input("Input your " + str(i + 1) + " data for X: ")
        Check = Xnum.isnumeric()
        if Check == False:
            print('Invalid number.')
            continue
        else:
            X1 = np.append(X1, int(Xnum))
            break
    while True:
        Ynum = input("Input your " + str(i + 1) + " data for Y: ")   
        Check = Ynum.isnumeric()
        if Check == False:
            print('Invalid number.')
            continue
        else:
            Y1 = np.append(Y1, int(Ynum))
            break
          
    
SecondLabel = input("Enter the name of your second set of data: ")
n = int(input("Enter number of elements for your second set of data: "))

for i in range(0, n):
    while True:
        Xnum = input("Input your " + str(i + 1) + " data for X: ")
        Check = Xnum.isnumeric()
        if Check == False:
            print('Invalid number.')
            continue
        else:
            X2 = np.append(X2, int(Xnum))
            break
    while True:
        Ynum = input("Input your " + str(i + 1) + " data for Y: ")   
        Check = Ynum.isnumeric()
        if Check == False:
            print('Invalid number.')
            continue
        else:
            Y2 = np.append(Y2, int(Ynum))
            break


from matplotlib import pyplot as plt

plt.title(Title)
plt.xlabel(XAxis)
plt.ylabel(YAxis)

plt.scatter(X1,Y1,color='red',label=FirstLabel)
z = np.polyfit(X1, Y1, 1)
p = np.poly1d(z)
plt.plot(X1, p(X1),color='red')

plt.scatter(X2,Y2,color='blue',label=SecondLabel)
z = np.polyfit(X2, Y2, 1)
p = np.poly1d(z)
plt.plot(X2, p(X2),color='blue')

plt.legend(loc="upper left")
plt.show()

print("")
print("The lines are a trend line through each set of data.")



