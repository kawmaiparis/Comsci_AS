def combinations():
    amount = int(input("Amount: "))
    deno = []
    top = []
    print("*type 'stop' to end*")
    while True:
        deno_temp = input("Denominations: ")
        if deno_temp == "stop":
            break
        else:
            deno_temp = int(deno_temp)
            deno.append(deno_temp)
            print(deno)
    #check if division has no remainder
    #add up to taht number
    before = 0
    after = 0
    count = len(deno)
    for unit in deno:
        division = amount%deno[before]
        if division == 0:
            while count > before:
                hold = []
                same = amount / deno[before]
                same = int(same)
                print(same)

                if same == amount:
                    hold.append(same)
                else:
                    for line in range(same):
                        hold.append(same)
                top.append(hold)
                before += 1
    for lines in top:
        print(lines)
            
            
            
    before += 1
        


combinations()        
    
    
