#ask for input
print("Input your numbers below (spacebar to stop):")
n = 0
startingstock = []
#let user inputs numbers
while True:
    n += 1
    number = (input(str(n) + "."))
    if number == " ":
        break
    number = int(number)
    startingstock.append(number)
    
print(startingstock)
hold = []
after = 0
#count unit digits of stock
stockrange = len(startingstock)
#for loop for clearing everything other than the selected unit
for n in range(stockrange-1):
    #duplicated stock numbers as fixed values
    stock = list(startingstock)
    #before gets reset
    before = 0
    temp = []
    #after goes up by 1 each time in the big loop
    after += 1
    #delete everything after the second unit
    del stock[after+1:]
    #count remaining unit
    count = len(stock)
    #for loop for calculating the differences between each units
    for t in range(count-1):
        #after variable stays the same while before variable goes up by 1 each time
        differ = stock[after] - stock[before]
        #before goes up by 1 each time in the small loop and get reset
        before+=1
        #store result in temporary list
        temp.append(differ)
    #find max result in the temp list
    maxi = max(temp)\
    #store the max result in hold list
    hold.append(maxi)
#find max result in hold list
finalmaxi = max(hold)
#print the max of max result!
print(finalmaxi)
        



