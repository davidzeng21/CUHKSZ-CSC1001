while True:
    N = input("Enter a positive integer:")
    if N.isdigit():
        N=int(N)
        print('%-8s%-8s%-8s'%('m', 'm+1', 'm**(m+1)'))
        for i in range(1,N+1):
            print ("%-8d%-8d%-8d"%(i, i+1, i**(i+1)))
        break
    else:
        print("Please enter a positive integer")
