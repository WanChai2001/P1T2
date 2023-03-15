def input_num():
    n = int(input("enter your amount of number = "))
    number = []
    for i in range(n):
        na = int(input("enter your int number = "))
        number.append(na)
    print("your number is ",number)
    find_odd(n,number)
    find_even(n,number)
def find_odd(n,allna):
    odd = []
    posodd = []
    for i in range(n):
        if allna[i]%2!=0:
            k_num=allna[i]
            odd.append(k_num)
            posodd.append(i)
    output_odd(odd,posodd)
def find_even(n,allna):
    even = []
    poseven = []
    for i in range(n):
        if allna[i]%2==0:
            k_num = allna[i]
            even.append(k_num)
            poseven.append(i)
    output_even(even,poseven)
def output_odd(allodd,posodd):
    print("your odd number is",allodd)
    print("your odd position is",posodd)
    return 0
def output_even(alleven,poseven):
    print("your odd number is",alleven)
    print("your odd position is",poseven)
    return 0
# main
input_num()
