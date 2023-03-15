filename = str(input('Enter filename '))
f = open("personal.dat",'a')
ID = []
name = []
age = []
salary = []
position = []
employee_information = {
    'ID': ID,
    'name': name,
    'age': age,
    'salary': salary,
    'position': position,
}
i = 0
while True:
    ID.append(int(input('ID พนักงาน = ')))
    if ID[i] == 0:
        print("=====================End===================")
        break
    else:
        name.append(str(input("ชื่อพนักงาน = ")))
        age.append(int(input("อายุของพนักงาน = ")))
        salary.append(int(input("เงินเดือนของพนักงาน = ")))
        position.append(str(input("แผนกที่ทำงาน = ")))
        f.write(str(employee_information['ID'][i]) + "/" + employee_information['name'][i] + "/"
        + str(employee_information['age'][i]) + "/" + str(employee_information['salary'][i]) + "/" + employee_information['position'][i]+ '\n')
    i = i + 1
f.close()
f = open("personal.dat",'g')
u = 1
k = 0
h = f.readable()
while True:
    h = f.readline()
    if h == '':
        break
    while k < i:
        print("=========================================================" % k)
        print("ID = ",employee_information['ID'][k])
        print("name = ", employee_information['name'][k])
        print("age = ", employee_information['age'][k])
        print("salary = ", employee_information['salary'][k])
        print("position = ", employee_information['position'][k])
        k += 1
        u += 1
f.close()