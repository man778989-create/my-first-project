print('============')
print('Elbek')
print('============')
print('17 years old')
print('============')
print('Engineer')
print('============')
print('Python')
print('============')

#Huh my is going to be the thing which will can safe my tens years.

#1.
name = 'Elbek'
age = 17
height = 1.70
is_student = True 

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#Close to Physics 
distance = 150
time = 3

speed = distance/time

print(speed)

#Might be challange 
temperature = 25.5
print(type(temperature))

#2. Second day
name = input('Enter your name:')
print('Hello',name)

age = int(input('Enter your Age:'))
print('your age after 10 years',age+10)

first = int(input('Enter your 1 number:'))
second = int(input('Enter your 2 number:'))

total = first+second

print('Total:',total)

#Speed
distance = float(input('Enter distance:'))
time = float(input('Enter time:'))

speed = distance / time

print("Speed: ",speed,'km/s')

#Surface
Length = int(input('Enter length(sm):'))
Width = int(input('Enter width(sm):'))

S = Length*Width

print('S =', S, 'sm')

#Day 3
product_price = int(input('Enter price of the product:'))
product_quantity = int(input('Enter quantity:'))
customer_money = int(input('Enter the amount of money you have:'))

price = int(product_price*product_quantity)
change = int(customer_money-price)

print('Total:', price)
print('Change:', change)

#3 day
a = 15
b = 7

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b) 

seconds = int(input('Enter seconds:'))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
left_seconds = seconds % 60
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds left:', left_seconds)

#day 4 
area = int(input('Enter area in rectangle:'))
perimeter = int(input('Enter perimeter in rectangle:'))

diagonal = (area**2 + perimeter**2)**0.5

print(int(diagonal), 'is the diagonal of rectangle')

#Distance Between Two Points
x = int(input('Enter first point x:'))
y = int(input('Enter first point y:'))
x2 = int(input('Enter second point x:'))
y2 = int(input('Enter second point y:'))

d = ((x2**2-x**2)+(y2**2-y**2))**0.5

print('Distance between two points:',int(d))

