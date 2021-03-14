from math import sin
from math import cos
from math import tan

while True:
    a = input("Enter the left end point of the interval:")
    if a.lstrip('-').replace('.','',1).isdigit():
        a= eval(a)
        break
    else:
        print("Please Enter a real number!")

while True:
    b = input("Enter the right end point of the interval:")
    if b.lstrip('-').replace('.','',1).isdigit():
        b= eval(b)
        break
    else:
        print("Please Enter a real number!")

a = min(a, b)
b = max(a, b)

while True:
    n = input("Enter the number of sub-intervals you want to divide:")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Please enter a positive integer!")

while True:
    func = input("Please enter the function name(sin, cos, or tan):")
    if func in ('sin', 'cos', 'tan'):
        if func == 'sin':
            i1 = 1
            integration = 0
            while i1 <= n:
                integration += (b-a)/n*sin(a+(b-a)/n*(i1-0.5))
                i1 += 1
            print("The numerical integration of sin(x) over interval [",a,',',b,"] is", integration)
        if func == 'cos':
            i2 = 1
            integration = 0
            while i2 <= n:
                integration += (b-a)/n*cos(a+(b-a)/n*(i2-0.5))
                i2 += 1
            print("The numerical integration of cos(x) over interval [",a,',',b,"] is", integration)
        if func == 'tan':
            i3 = 1
            integration = 0
            while i3 <= n:
                integration += (b-a)/n*tan(a+(b-a)/n*(i3-0.5))
                i3 += 1
            print("The numerical integration of tan(x) over interval [",a,',',b,"] is", integration)
        break
    else:
        print("Plase enter the correct function name!")
