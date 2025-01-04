#This file is for the Tyler Series question.
a=float(input("Enter the value of x:"))
b=int(input("Enter the value of terms:"))
def factorial(a):
    mult=1
    for n in range(2,a+1):
        mult *= n
    return mult
def cos(x,n):
    sumx=0
    for n in range(1,n+1):
        sumx +=((-1)**(n+1))*x**((n-1)*2)/factorial(2*(n-1))
    return sumx    

print(cos(a,b))

















