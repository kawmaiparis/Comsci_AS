user = input("User id: ")

if user[0].isupper() and user[1:3].islower() and user[3:].isdigit() and len(user) == 6:
    print("Correct!")
else:
    print("Wrong!")

#Extension
if user[0:3].isalpha() and user[3:].isdigit() and len(user) == 6:
    print("Correct!")
else:
    print("Wrong!")

def ValidateUserId(user):
    if user[0].isupper() and user[1:3].islower() and user[3:].isdigit() and len(user) == 6:
        return True
    else:
        return False

ValidateUserId("Hal123")
