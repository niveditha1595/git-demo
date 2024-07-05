'''import datetime

#to get current date:
x= datetime.datetime.now()
print("the current date time: ", x)
print(x.strftime("%A, %B %d, %Y %I:%M:%S %p %Z"))     # to print in specific time format
print(x.strptime("02/12/1996 5:53","%m/%d/%Y %H:%M"))

# to fine area of circle
import math

def areaofcircle(radius):
    area = math.pi*radius*radius
    return area
area = areaofcircle(1.1)
print(area)

# program to accept input from keyboard and print the user first & last name in reverse order:
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
x=first_name[::-1]
y=last_name[::-1]
print(first_name,last_name)
print(x, y)
print(x+y)
print(last_name+ " "+ first_name)

# a number is accepted from the user and print them in list and tuple
num=input("Enter a number: ")
print(num)
list=num.split(",")
print('List:', list)
Tuple=tuple(list)
print('Tuple:', Tuple)

# print first and last data from the list:
colorlist=['red','green','blue','yellow']
print(colorlist[0])
print(colorlist[3])
print(colorlist[0]+ " " + colorlist[3])

# to print the month of a calendar:
import calendar
y=int(input("Enter year: "))
x=int(input("Enter month: "))
print(calendar.month(y,x))

# to find the sum and average of list numbers
sum=0
l1=[1,2,3,4,5]
print(len(l1))
for i in l1:
    sum=sum+i
    avg=sum/len(l1)
print(sum)
print(avg)

# to find whether given string is a palindrome or not

x="madam"
y=x[::-1]
if x==y:
    print("the given string is a palindrome")

else:
    print("the given string is not a palindrome")

# to find a factorial of a number:
import math

num=int(input("Enter a number: "))
res=math.factorial(num)
print(res)

# to find the maximum number in a given list:
l1=[1,2,3,4,5,8,9]
num=l1[0]
for x in l1:
    if x>num:
        num=x
print(x)

# to find the common elements between the lists:
l1=[1,2,3,4,5]
l2=[2,3,5,6,7]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print(l3)

# to find whether given number is prime number or not:

l1=[5,2,8,1,9]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

# to find second largest number in a list:
l1=[1,2,3,4,5]
large=l1[0]
seclarge=0
for i in l1:
    if i>large:
        seclarge=large
        large=i

    elif i>seclarge and i!=large:
        seclarge=i

print(seclarge)

# to print same and different numbers in a list:
l1=[1,2,2,3,4,4,5,6,5]
print(l1)
l2=set(l1)
print(l2)

l3=[]
l4=[]
for i in l1:
    if i not in l3:
        l3.append(i)
    elif i not in l4:
        l4.append(i)

print(l3)
print(l4)'''















