Node = []
def Insert():
    n = int(input("ป้อนตัวเลขของคุณ = "))
    i = 0
    if n not in Node:
        Node.append(n)
        Node.sort()
    elif n in Node:
        print("======================")
        print("ได้รับข้อมูลแล้ว")
        print("======================")
        n = int(input("ป้อนตัวเลขของคุณ = "))
        Node.append(n)
        Node.sort()
def Print(Node):
    print("ตัวเลขของคุณของคุณ  = ",Node)
def Delete(Node):
    print("====================================")
    delete = int(input("ตัวเลขที่ต้องการจะลบ = "))
    Node.remove(delete)
def Search(Node):
    i = 0
    print("=================================")
    a = int(input("ป้อนจำนวนที่จำค้นหา = "))
    if a in Node:
        while a != Node[i]:
            i = i + 1
    print("===========================================")
    print("found at position %d,number of compare %d"%(i+1,i+1))
    print("===========================================")
    i = 0
    if a not in Node and a != -5:
        while a > Node[i]:
            i = i + 1
            if i == len(number):
                break
        print("not found,numder of compare = %d"%(i+1,i+1))
menu = 0
while menu != 5:
    print("[1] Insert ตัวเลขของคุณ")
    print("[2] Print ตัวเลขของคุณ")
    print("[3] Delete ตัวเลขที่ต้องการ")
    print("[4] Search ตัวเลขที่ต้องการ")
    print("[5] จบการทำงาน")
    print("================================")
    menu = int(input("ป้อนทางเลือกของคุณ = "))
    if menu == 1:
        Insert()
    elif menu == 2:
        Print(Node)
    elif menu == 3:
        Delete(Node)
    elif menu == 4:
        Search(Node)
    elif menu == 5:
        print("จบการทำงาน")

