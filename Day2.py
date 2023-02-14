import math

# movies=["Pushpa","RRR","Patahn","KGF"]
# stars=["Allu Arjun","Ram Charan","SRK","Yash"]
# for i in range(len(movies)):
#     print("The {} movie is {}".format(i+1,movies[i]))

# for i in range(len(movies)):
#    print("The",int(i+1),"is the",movies[i])

# for i in range(0,len(stars)):
#     print("{} is stars {}.".format(stars[i],movies[i]))

# for i in range(3):
#     str=input("Enter a movie name:")
#     movies.append(str)
# print(movies)

# subject=() #tuple syntax

# taking input and appending into the list

# subject=[]

# for i in range(5):
#     subject.append(input("Enter a subject name:"))
# print(subject)

#=============================================================================================
#1
# otp=[]
# for i in range(1,10):
#     otp.append(int(input("Enter a number:"))**2)
# print(otp)    

#==============================================================================================
#tuple
 
#Tuple is not muttable and it have () by default
#tup=(1,2,3)
# tup[2]=4 it is not possible
#tup1=tup,5,6,7  #Nested tuple
#print(tup[2]) #3

# name=input("What your name:")
# age=int(input("What is your age:"))
# department=input("What your department:")

# print("Hi %s,how are you? I see that you are from %s department. You are %i year old" %(name,department,age))
# print("Hi {name},how are you? I see that you are from {department} department. You are {age} year old" )

#=========================================================================================================================

# seq=[]
#seq=[(1,2,3),(4,5,6),(7,8,9)]

# for i in range(0,9,3):
#     seq.append((i+1,i+2,i+3))
# print(seq)

#========================================================================

# x=input().split()
# print(x)

# for i in range(len(x)):
#     x[i]=int(x[i])
# print("New:",x)

#==========================================================================

r=int(input("Enter a radius:"))
if r>0:
    Area=(4/3)*(math.pi)*(r**3)
    print("Area of volume is:",Area)
else:
    print("Not possible")

