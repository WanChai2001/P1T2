Brand = []
Gan = []
Color = []
Price = []
n = int(input("จำนวนข้อมูล = "))
while n <= 0:
    n =int(input('จำนวนรถยนต์ = '))
for i in range(n):
    Brand.append(str(input('ยีห้อรถยนต์ = ')))
    Gan.append(str(input('รุ่นของรถยนต์ = ')))
    Color.append(str(input('สีของรถยนต์ = ')))
    Price.append(str(input('ราคารถยนต์ = ')))
    car = {
        'Brand': Brand,
        'Gen': Gan,
        'Color': Color,
        'Price': Price,
    }
print('ยีห้อรถยนต์ =',car['Brand'])
print('รุ่นของรถยนต์ =',car['Gen'])
print('สีของรถยนต์',car['Color'])
print('ราคารถยนต์ =',car['Price'])
