n = int(input("number = "))
i = 0
if n > 0:
    print("positive number")
    while i < n:
        i = i + 1
        print(i)
if n < 0:
    print("negative number")
    while   i > n:
        i = i - 1
        print(i)
if n == 0:
    print("it is zero number")
else:
    print("number",n)
