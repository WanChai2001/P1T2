def serach(s,c,a):
    i = 0
    j = 1
    while i < c:
        if a[i] == s:
            print("  จำนวนเปรียบเทียบ %d  " % j)
            break
        i += 1
        j += 1
    if i == c:
            print("//////  ไม่พบ  ///////")
size = int(input("ป้อนขนาดอาร์เรย์ของคุณ = "))
N = []
i = 0
while i < size:
    N.append(int(input("ป้อนหมายเลขของคุณ = ")))
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
print(a)
while True:
    print("//////////////////////")
    print("[1] ต้องการค้นหาอีกครั้ง")
    print("[2] Exit")
    print("//////////////////////")
    n = int(input("เลือกหมายเลข = "))
    print("//////////////////////")
    if n == 1:
        s = int(input("ป้อนหมายเลขสำหรับการค้นหา = "))
        serach(s, c, a)
    if n == 2:
        print("//////End//////")
        break



