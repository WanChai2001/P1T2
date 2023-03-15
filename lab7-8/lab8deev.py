def Bubblesort_Front_to_Back(num1):
    size, count = len(num1), 0
    for i in range(0,size):
        for j in range (0,size-i-1):
            if num1[j]>num1[j+1]:
                num1[j], num1[j+1] = num1[j+1], num1[j]
                count+=1
                print(num1)
    return num1,count

def Bubblesort_Back_to_Front(num2):
    size, count2 = len(num2), 0
    for i in range(size,-1,-1):
        for j in range (size-1,size-i-1,-1):
            if num2[j]<num2[j-1]:
                num2[j], num2[j-1] = num2[j-1], num2[j]
                count2+=1
                print(num2)
    return num2,count2

def linear_search(num1,s):
    size, s_count = len(num1), 0
    for i in range(size):
        if num1[i]==s:
            print("[ data founded! ]")
            return s_count
        if num1[i]>s:
            print("[ data not found! ]")
            return s_count
        if num1[i]<s:
            s_count+=1
        if num1[i]<s and s_count==size:
            print("[ data not found! ]")
            return s_count   

numin = []
n = int(input("Enter list size : "))
for k in range(n):
    numin.append(int(input("Enter data : ")))  
print("\nlist -> ",numin)

num1= []
num1 = numin.copy()
num1,count = Bubblesort_Front_to_Back(num1)
print("list front to back sorted -> ",num1)
print("sort count -> ",count,"\n")

num2 = []
num2 = numin.copy()
num2,count2 = Bubblesort_Back_to_Front(num2)
print("list back to front sorted -> ",num2)
print("sort count -> ",count2,"\n")

while True:
    ans =str(input("Do you want to search [y/n] : "))
    if ans == 'y':
        s = int(input("Enter searching number : "))
        s_count = linear_search(num1,s)
        print("search count - >",s_count)
    if ans == 'n':
        exit()

    