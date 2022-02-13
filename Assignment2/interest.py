#Write a program to calculate simple interest.Accept values from user.(si=pnr/100)
p = float(input("Enter value of principle  : "))
 
n = float(input("Enter the years : "))
 
r = float(input("Enter rate of interest : "))
si = (p *n*r)/100
print("Simple interest is :",si)