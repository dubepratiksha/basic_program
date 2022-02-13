#WAP to calculate x raised to the power n (xn). Accept the value of x and n from the user.
import math
x= int(input("Enter the value of x: "))
n= int(input("Enter the value of n: "))
c = math.pow(x, n)
print("The",x,"raised to the power",n,"is:",int(c))