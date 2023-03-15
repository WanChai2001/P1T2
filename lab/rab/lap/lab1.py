import math
N = int(input("N is positive Number : "))
M = 2
while M <= math.sqrt(N) :
    NUM = N//M*M
    if NUM == N :
        print("N is not prime")
        exit()
    M = M + 1
print("N is prime")



