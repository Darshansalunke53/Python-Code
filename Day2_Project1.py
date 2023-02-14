import random
#1===============================================================================
# qualities=["MCC","BCL","LL","AZ"]
# greetings=["Good Morning","Hello,welcome","I like this","Good night"]
# print(random.choice(greetings))
# print("kartik",random.choice(qualities))

# comp=[1,2,3,4,5,6,7,8,9]
# for i in comp:
#  player=int(input("Enter a player number(1-9):"))
#  if(player==random.choice(comp)):
#     print("You win")
#  else:
#     print("You Loose")    


# greetings=["Good Morning%s","Hello,welcome%s","I like this%s","Good night%s"]

# message=random.choice(greetings) %(" Darshan")
# print(message)

#2==================================================================================
# name=input("Enter your name:")
# grettings=["Good morning","Hey","Hello","hi"]
# jokes=("My wife told me to stop impersonating a flamingo. I had to put my foot down","I failed math so many times at school, I can’t even count",
#        "I used to have a handle on life, but then it broke")
# print(random.choice(grettings),name,", How are you")
# x=input()
# if x=="i am fine":
#     print("Do you want to hear a joke?")
#     a=input()
#     if(a=="yes"):
#         print("Here it is",random.choice(jokes))
#     else:
#         print("bay bay",name)

#3=================================================================================

#Dictionary
score=0
a={
    "What is the capital of india?":"Delhi",
    "Who is the Pm of india?":"Narendra Modi",
    "When did india gain independance?":'1947',
    "When did chhattrapati shivaji maharaj born":'1630'
}
for i in a:
    print(i)
    ans=input("Your answer:")
    if ans == a[i]:
        score +=1
print("Your score is:",score)

