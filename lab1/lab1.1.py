N = int(input("Enter amount number = "))
V=[]
Z = 0
while Z < N :
    Y = int(input("Enter number = "))
    V.append(Y)
    Z = Z + 1
X = int(input("searching  = "))
i = 0
U = 0
Found = False
while i < N and not Found :
    if X == V[i]:
        Found = True
        U = U + 1
        location = i
        print("found")
        print("Count = ",U)
        print("location = ",location)
        exit()
    else:
        i = i + 1
        U = U + 1
    print("Not Found")
print("Count = ",U)









