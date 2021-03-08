ipt = (input("Enter an integer:"))

itg = str(ipt)
if ipt < 0:
    print("The number you input is not appropriate.")  
else:
    for i in range(len(itg)):
        print(itg[i])
