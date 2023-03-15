
def serach(s,c,a):
    i = 0
    j = 1
    while i < c:
        if a[i] == s:
            print("======>> Found at %d position <<======" % i)
            print("======>> number of compare %d <<======" % j)
            break
        i += 1
        j += 1
    if i == c:
            print("======>>      Not Found       <<======")
            print("======>> number of compare %d <<======" % j)
size = int(input("Enter your size of array : "))
N = []
i = 0
while i < size:
    N.append(int(input("Enter your number : ")))
    i += 1
i = 1
print(N)
while i < size:
    temp = N[i]
    j = i
    while(temp < N[j-1]) and j>0:
        N[j] = N[j-1]
        j -= 1
    N[j] = temp
    i+=1
a = list(dict.fromkeys(N))
c = len(a)
print("len(a) = ",c)
print(a)
while True:
    print("=====================")
    print("[1] Want to search")
    print("[2] Exit")
    print("=====================")
    n = int(input("select number : "))
    print("=====================")
    if n == 2:
        print("=========={ End the search }==========")
        break
    if n == 1:
        s = int(input("Enter number for search: "))
        serach(s, c, a)


