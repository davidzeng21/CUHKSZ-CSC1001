while True:
    N = input("Enter a positive integer:")
    if N.isdigit():
        N=int(N)
        prime_list = list()
        for digit in range(2, N):
            flag = True
            for i in range (2, int(digit**0.5 + 1)):
                if digit % i == 0:
                    flag = False
                    break
            if flag:
                prime_list.append(digit)
        print("The prime numbers smaller than",  N, "include:")
        order = 0
        for prime in prime_list:
            print(prime, end =" ")
            order += 1
            if order % 8 == 0:
                print()
        break
    else:
        print("Please enter a positive integer")