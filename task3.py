#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
import math


print("\n\n\n\nEnter the first price")
price1 = input ()
price1 = float (price1)


print("\nEnter the second price")
price2 = input ()
price2 = float (price2)

print("\nEnter the third price")
price3 = input ()
price3 = float (price3)


print("\nEnter the fourth price")
price4 = input ()
price4 = float (price4)

p = (price1+price2+price3+price4)

t = p*0.12
t = float (t)
round(t,2)


tt = t + p
tt = float (tt)
round(tt,2)


print(f"Your subtotal is {p} and your taxes total {t} for a total of ${tt}")