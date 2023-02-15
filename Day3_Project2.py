list = {"Darshan": '4444', "Kartik": '2222', "Yajur": '3333', "Krishna": '5555'}

while (True):

    username = str(input("For login,Enter a Username:"))

    if username in list:
        password = str(int(input("Now,Enter a password:")))

        if (list[username] == password):
            print("You are login is succssesful")
            break
        else:
            for i in range(2):

                print("Fail To login,try again")
                password = str(int(input("Enter a password:")))  

                if (list[username] == password):
                    print("You are login is succssesful")
                    break
                else:
                    continue

            ans = input("Fail To login,You want to create a password:")

            if ans == 'y' or ans == "Y":
                password = str(int(input("Creat your password:")))
                list[username] = password

    else:

        print("invalid username!")
        ch = input("You Want to creat a account(y/n):")

        if ch == "y" or ch == "Y":
            username = str(input("create a Username:"))
            password = str(input("Creat your password:"))
            list[username] = password
            print("Registerd!")
        else:
            print("Thank You! for visiting")
            break