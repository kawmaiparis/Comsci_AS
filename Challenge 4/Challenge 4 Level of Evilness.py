#the level of evil starts at 0
evil = 0

#ask the two names, first and last
name1 = input("Gimme your first name please: ")
name2 = input("How about your last name: ")


"""go through each character in the first name and see
if it has the same letters as the words 'devil' and 'satan'"""

for char in name1:
    if char in ['d','e','v','i','l','s','a','t','n']:
        #level of evilness increases by 1 for each matching letter
        evil += 1

#it's turn to look at the last name
for char in name2:
    if char in ['d','e','v','i','l','s','a','t','n']:
        #level of evilness increases by 2 for each matching letter this time
        evil += 2

#tell the user how evil they are
print ("Your evil level is " + str(evil))
