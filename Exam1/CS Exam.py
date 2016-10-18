while True:
    print(" 1. Set username \n 2. Set password \n 3. Login \n 4. Quit \nEnter your choice")
    choice = input("")
    wrong = 0
    if choice == "1":
        username = input("Please input your username:\n").lower()
    while choice == "2":
        password1 = input("Please input your password:\n")
        if len(password1) < 5:
            password1 = input("Password has to be at least 5 characters. Please input again:\n")
        password2 = input("Please input your password again:\n")
        if password1 == password2:
            choice = ""
        else:
            print("Passwords don't match. Please try again.")
            choice = "2"
    while choice == "3":
        name = input("Username: ")
        pas = input("Password: ")
        if name == username and pas ==  password1:
            print("You're logged in")
            choice = ""
        else:
            wrong = wrong + 1
            if wrong == 3:
                choice = ""
            else:
                print("Invalid username or password. Please retry")
                choice = "3"
    if choice == "4":
        break
    if wrong == 3:
        break
