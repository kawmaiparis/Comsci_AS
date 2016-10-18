words = "Tom Marvolo Riddle"
print(words)
words2 = words[9].upper() + words[10] + words[12].lower() + words[14] + " " + words[7].upper() + words[10]+ words[9]+ words[14] + words[17]+ words[2]+ words[1]+ words[6] + words[0].lower()
print(words2)

print("")
burger = "Burger king is the best. Mcdonalds suck!"
print(burger)
burger2 = burger[0] + burger[8:11] + burger[28] + burger[39]
print(burger2)

shopping = ['apples','bananas','oranges','peaches','strawberries','kiwi']
#print every other fruits starting from 0
print(shopping[0::2])
#print fruits 0 to 3
print(shopping[0:3])
print('apples' in shopping)
