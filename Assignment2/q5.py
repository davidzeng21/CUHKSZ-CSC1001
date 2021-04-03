resultOfLockers={}
for a in range(1,101):
    resultOfLockers[a] = False
    for b in range (1,101):
        if a%b == 0:
            resultOfLockers[a]= not resultOfLockers[a]
    if resultOfLockers[a]:
        print("L{}".format(a), end = " "),
print("are open.")