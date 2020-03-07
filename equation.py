import math
def solve(a,b,c):
    d=b*b-4*a*c
    if d>=0 and a!=0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        #print("x1=",x1,"x2=",x2)
        return x1,x2
    elif a==0:
        x1=x2=-c/b
        #print("x1=x2=",x1)
        return x1,x2
    else:
        return("there is no solution!")
a=float(input("please input a="))
b=float(input("please input b="))
c=float(input("please input c="))
print(solve(a,b,c))