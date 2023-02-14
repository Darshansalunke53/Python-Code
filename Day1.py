#we do not use datatypes for storing value in variable
#a=10  datatype automaticaly assigne by PVM

# a=10;
# b=3.6;
# c='$';
# d="Darshan"
# print("value a:",a)
# print("value b:",b)
# print("value c:",c)
# print("value d:",d)

# print("a:",type(a)) #type() is used to see the datatype of variable
# print("b:",type(b))
# print("c:",type(c))
# print("d:",type(d))

# print("a:",id(a))  #id() used to see the addres of variable
# print("b:",id(b))
# print("c:",id(c))
# print("d:",id(d))

# a=2
# b=3
# print("Addition=",a+b)
# print("Substraction=",a-b)
# print("MUltiplication=",a*b)

#1
# a=2
# b=3
# c=a+b
# print("addition=",c)

#2
# num1=10
# num2=30
# print("Befor swapping num1=",num1,"and num2=",num2)
# temp=num1
# num1=num2
# num2=temp
# print("After swapping num1=",num1,"and num2=",num2)

#3
# a=100
# b=300
# print("Befor swapping a=",a,"and b=",b)
# a=a+b
# b=a-b
# a=a-b
# print("After swapping a=",a,"and b=",b)

#4
# p1=65
# p2=89
# p3=99

# total=p1+p2+p3
# percentage=total/3.0

# print("Total=",total)
# print("Percentage=",percentage)

#5
# p=1000000
# r=9.5
# t=1.5
# si=p*r*t/100
# p=si/r*t
# print("Simple Interest=",si)
# print('Principle amount=',p)

#6
# pi=3.14
# r=5
# A=pi*r*r
# C=2*pi*r
# print("Area of Circle=",A)
# print("Circumfarence=",C)

#7
# height=5
# inch=height*12
# cm=inch*2.54
# print("inch=",inch)
# print("cm=",cm)

#8
# ct=20
# f=1.8*ct+240
# print("Feranite tem=",f)

#9 Slicing
# Name="Darshan"

# print(Name[0])
# print(Name[2])
# print(Name[-1])
# #print(Name[8])
# print(Name[0:8:2]) # [start:end-1:step]
# print(Name[0:])
# print(Name[:4])
# print(Name[::2])
# print(Name[::])
 
#10 Memory Managment
# math=50
# chem=50
# phy=50
# print(id(math))
# print(id(chem))
# print(id(phy))
# math=55
# print(id(math))

#Type Casting
#11  
# a='2'
# b='3'
# print(a+b)
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print(a+b)

#12
print(int(3.24))
#print(int(10+3i))

print(int(True))
print(int(False))
#print(int("3.22"))
print(int("4"))
#print(int("Darshan"))

#12

# print(float(3.24))
# #print(int(10+3i))
# print(float(True))
# print(float(False))
# print(float("3.22"))
# print(float("4"))
# print(float("Darshan"))

#13

# print(complex(3.24))
# print(complex(10))
# print(complex(True))
# print(complex(False))
# print(complex("3.22"))
# print(complex("4"))
# #print(complex("Darshan"))

#14

print(bool(3.24))
print(bool(10))
print(bool(True))
print(bool(False))
print(bool("3.22"))
print(bool("4"))
print(bool("Darshan"))
print(bool(-1))

#15 List are muttable
mylist=['darshan','kartik','krishna',45,89.90]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[-2])
print(mylist[2:5])
print(mylist[:6])
print(mylist[1:6:1])

# mylist[3]="abcd"
# print(mylist)

# #list are growable

# mylist.append("xyz")
# mylist.append(89)

# print(mylist)

# #to add a value in specified position use insert in list
# mylist.insert(2,"narte")
# print(mylist)

# #to delete a value on list use remove
# mylist.remove("narte")
# print(mylist)

# #to copy list into anothe list use copy
# newlist=mylist.copy()
# print(newlist)

#Multi-dimentional list
mylist=[['darshan','kartik'],['krishna',45],[89.90]]
print(mylist[0][0])
print(mylist[1][1])
print(mylist[2][0])





