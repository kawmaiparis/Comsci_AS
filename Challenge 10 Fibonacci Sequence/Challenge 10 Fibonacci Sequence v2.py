#normal function
def normal():
    seq = []
    n = 0
    #ask user for number of places they want
    unit = int(input("Number of places generated: "))
    if unit <= 0:
        print("ARGGHH! YOU BROKE THE PROGRAM!")
    #if user only want 1 place
    if unit == 1:
        seq.append(n)
        print(seq)
    #if user wants 2 places
    elif unit == 2:
        for start in range(2):
            seq.append(n)
            n += 1
            print(seq)
    #if they want more than 2 places
    else:
        #for loop for the first 2 numbers
        for start in range(2):
            seq.append(n)
            n += 1
            print(seq)
        posi = 0
        #for loop for other numbers, using the sum of the 2 numbers before them
        for start in range(unit-2):
            n = seq[posi] + seq[posi + 1]
            seq.append(n)
            print(seq)
            posi+= 1
        #sum of everything
        total = sum(seq)
        print("Total: " + str(total))

#reverse function        
def reverse():
    seq = []
    n = 0
    #ask user for number of places they want
    unit = int(input("Number of places generated: "))
    #if they input negative numbers
    if unit <= 0:
        print("ARGHHHH! YOU BROKE THE PROGRAM!")
    #if user only want 1 place
    if unit == 1:
        seq.append(n)
        print(seq)
    #if user wants 2 places
    elif unit == 2:
        for start in range(2):
            seq.append(n)
            n += 1
        print("[" + str(seq[1]) + "]")
        seq.reverse()
        print(seq)
    #if user wants more than 2 places
    else:
        #for loop for the first 2 numbers
        for start in range(2):
            seq.append(n)
            n += 1
            #reverse the list
            seq.reverse()
            print(seq)
        #reverse the list back
        seq.reverse
        posi = 0
        #for loop for other numbers
        for start in range(unit-2):
            n = seq[posi] + seq[posi + 1]
            seq.append(n)
            posi+= 1
            #reverse the list
            seq.reverse()
            print(seq)
            #reverse the list back
            seq.reverse()
    #total
    total = sum(seq)
    print("Total: " + str(total))

#ask user if they want normal or reverse series
print("1.Normal\n2.Reverse")
option = input("")
if "1" in option:
    normal()
if "2" in option:
    reverse()
