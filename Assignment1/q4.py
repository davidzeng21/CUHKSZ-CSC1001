N = int(input("Enter an integer:"))
while N < 0:
    print("Please enter a positive integer")
    N = int(input("Enter an integer:"))
print('%-8s%-8s%-8s'%('m', 'm+1', 'm**(m+1)'))
for i in range(0,N):
    print ("%-8d%-8d%-8d"%(i, i+1, i**(i+1)))