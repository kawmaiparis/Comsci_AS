bank = input("Bank Code: ")
counter = 0
file = open("codes.txt",'r')
member = [line.strip() for line in file]
print(member)
for i in range(len(member)):
    banknum = member[i][6:]
    if banknum == bank:
        print(member[i])
        counter = counter + 1
print("There are", counter, "dispensers in this bank")
