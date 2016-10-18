import random
import time

#starting stats
start = 15
healthx = 0
doublex = 0
counterx = 0
missx = 0
bonusx = 0
        
#original hp
health = 100

#items stats
tango = 30
salve = 100
dagon = 50

#intro
user = input("What is your name?\n")
pokemon = input("Please name your pokemon.\n")
print("Please carefully spend skill points on " + pokemon + "'s attributes")

#let user choose their pokemon attribute
while True:
    #user has 15 skill points to start with
    print("\nYou now have " + str(start) + " skill points to spend\n")
    print("     1. Health - your total hp and regeneration rate\n     2. Double - Chances of you attacking twice in a role\n     3. Counter - Chances of you counterattacking\n     4. Miss - Chances that your enemy will miss their attack\n     5. Bonus - Chances of you finding an extra item\n     6. Reset skill points")
    skill = input("\n")
    #let user to input skill points
    if skill == "1":
        healthxx = input("How many points do you want to use: ")
        if healthxx.isnumeric() == False:
            print("invalid command. Try again.")
        else:
            healthxx = int(healthxx)
            healthx += healthxx
            healthxx = 0
            start -= int(healthx)
    elif skill == "2":
        doublexx = input("How many points do you want to use: ")
        if doublexx.isnumeric() == False:
            print("invalid command. Try again.")
        else:
            doublexx = int(doublexx)
            doublex += doublexx
            doublexx = 0
            start -= int(doublex)
    elif skill == "3":
        counterxx = input("How many points do you want to use: ")
        if counterxx.isnumeric() == False:
            print("invalid command. Try again.")
        else:
            counterxx = int(counterxx)
            counterx += counterxx
            counterxx = 0
            start -= int(counterx)
    elif skill == "4":
        missxx = input("How many points do you want to use: ")
        if missxx.isnumeric() == False:
            print("invalid command. Try again.")
        else:
            
            missxx = int(missxx)
            missx += missxx
            missxx = 0
            start -= int(missx)
    elif skill == "5":
        bonusxx = input("How many points do you want to use: ")
        if bonusxx.isnumeric() == False:
            print("invalid command. Try again.")
        else:
            bonusxx = int(bonusxx)
            bonusx += bonusxx
            bonusxx = 0
            start -= int(bonusx)
    elif skill == "6":
        healthx = 0
        manax = 0
        countrx = 0
        missx = 0
        bonusx = 0
        start = 15
    else:
        print("invalid command, please select skill set by typing '1','2','3','4','5' or '6'")

    if healthx > 10 or doublex > 10 or counterx > 10 or missx >10 or bonusx > 10:
        print("maximum skill points for each attribute is 10. Spent skill points will be reset. Please try again")
        healthx = 0
        doublex = 0
        counterx = 0
        missx = 0
        bonusx = 0
        start = 15

    #skill points will be reset if they overspend them, more than 20
    if healthx + doublex + counterx + missx + bonusx > 20:
        print("skill points have been overspent. All points will be reset. Please try again.")
        healthx = 0
        doublex = 0
        counterx = 0
        missx = 0
        bonusx = 0
        start = 15
    #ask whether they want to proceed or to go back when all the 20 points are spent
    if healthx + doublex + counterx + missx + bonusx == 20:
        print("All skill points have been spent. Do you want to make any changes?")
        reset = int(input("     1.Continue\n     2.Make Changes\n"))
        #reset skillpoints
        if reset == 2:
            healthx = 0
            doublex = 0
            counterx = 0
            missx = 0
            bonusx = 0
            start = 15
        #continue
        elif reset == 1:
            health = health + (int(healthx) * 10)
            double = random.randint(1,15-doublex)
            counter = random.randint(1,15-counterx)
            miss = random.randint(1,15-missx)
            break

#more intro
print("")
print("Welcome to the world of pokemon, " + user)
print("As you travel across the land, you will find items which can aid you along the journey")

#starting items
inventory = ["tango","amplifier"]

#starting kill count
kill = 0

#random enemy and their set of stat
while True:
    faith = random.randint(1,3)
    #Charizard
    if faith == 1:
        enemy = "CHARIZARD"
        rivalhealth = 200
        attack = ["SUPERNOVA","DRAGONBREATHE","SUNSTRIKE"]
        damage = [10,11,12,13,14,15,16,17,18,19,20]

    #Squirtle
    elif faith == 2:
        enemy = "SQUIRTLE"
        rivalhealth = 80
        attack = ["TIDEBRINGER","TORRENT","WAVEFORM"]
        damage = [15,17,19,21,22,23,24,25,30,34,38]

    #Bulbasar
    elif faith == 3:
        enemy = "BULBASAR"
        rivalhealth = 120
        attack = ["OVERGROWTH","ECHOSLAM","BOULDERSMASH"]
        damage = [15,16,17,18,19,20,21,22,24,25,26]
    
    print("\n*An enemy has suddenly appeared*")
    #user press enter to continue
    preBattle = input(enemy + " wants to battle with you. press enter when you're ready")

    print("\n     " + user + " sends out " + pokemon)
    BONUST = 0
    BONUSW = 0
    while True:
        print("")
        print("     " + pokemon + "'s health : " + str(health))
        print("     " + enemy + "'s health : " + str(rivalhealth))
        print("")
        #user's attack stats
        moves = ["tackle","whip"]
        tackle = [21,32,30,24,25]
        whip = [35,16,27,28,19]
        m = "0"
        #user selects what to do
        print("     1.attack \n     2.use items \n     3.surrender")
        option = input("Select your option: ")
        t = random.choice(tackle)
        #critical strike for tackle
        if BONUST == 1:
            t = t*2
        elif BONUST == 2:
            t = t*3
        else:
            pass
        w = random.choice(whip)
        #crical strike for whip
        if BONUSW == 1:
            w = w*2
        elif BONUSW == 2:
            w = w*3
        else:
            pass
        #user chooses attack
        if option == "1":
            while True:
                print("")
                print(moves)
                #user selects move to use
                m = input("Select move to use: ").lower()
                print("")
                if m == "tackle":
                    if double == 1:
                        print(".....")
                        time.sleep(1.5)
                        print("LUCKY CHANCE! Your damage is double this round!")
                        t = t*2
                    print("You have dealt " + str(t) + " damage")
                    rivalhealth -= t
                    print(enemy + "'s health: " + str(rivalhealth))
                    stopattack = 0
                    break
                elif m == "whip":
                    if double == 1:
                        print(".....")
                        time.sleep(1.5)
                        print("LUCKY CHANCE! Your damage is double this round!")
                        w = w*2
                    print("You have dealt " + str(w) + " damage")
                    rivalhealth -= w
                    print(enemy + "'s health: " + str(rivalhealth))
                    stopattack = 0
                    break
                else:
                    print("invalid moves. Please select again.")                   

        #use inventory
        elif option == "2":
            print(inventory)
            print("Select item to use: ")
            item = input("")
            if item not in inventory:
                print("please try again")
            if "tango" in item:
                health = health + tango
                inventory.remove("tango")
                print(pokemon + "'s health : " + str(health))
            elif "salve" in item:
                health = health + salve
                inventory.remove("salve")
                print(pokemon + "'s health : " + str(health))
            elif "amplifier" in item:
                BONUST = 1
                BONUSW = 1
                inventory.remove("amplifier")
                print(pokemon + "'s damage is now X2")
            elif "superamp" in item:
                BONUST = 2
                BONUSW = 2
                inventory.remove("superamp")
                print(pokemon + "'s damage is now X3")
            elif "scepter" in item:
                rivalhealth = rivalhealth - scepter
                inventory.remove("scepter")
                print(enemy + "'s health : " + str(rivalhealth))
            elif "shadow" in item:
                inventory.remove("shadowblade")
                print("You turned invisible and backstabbed " + enemy)
                rivalhealth = 0
            else:
                print("invalid item, please try again")

        #surrender
        elif option == "3":
            print("You Suck")
            break
        else:
            print("invallid command, press select '1', '2', or '3'")

        #rival hp below = 0
        if rivalhealth <= 0:
            print("Well Done! You have slained " + enemy)
            kill += 1
            print("Enemies slained: " + str(kill))
            health += 2*healthx
            print(pokemon + " has regenerated " + str(5*healthx))
            #item drop
            while True:
                    print("\nYou found something...")
                    time.sleep(1.5)
                    #random item from 1 - 15
                    drop = random.randint(1,16+bonusx)
                    if drop == 1 or drop == 2 or drop == 3 or drop == 4:
                        inventory.append("tango")
                        print("You found a TANGO!")
                        break
                    elif drop == 5 or drop == 6 or drop == 7:
                        inventory.append("salve")
                        print("You found a SALVE!")
                        break
                    elif drop == 8 or drop  == 9:
                        inventory.append("amplifier")
                        print("You found an AMPLIFIER!")
                        break
                    elif drop == 10 or drop == 11 :
                        inventory.append("superamp")
                        print("***You found a SUPER AMPLIFIER!!!***")
                        break
                    elif drop == 12 or drop == 13 or drop == 14:
                        inventory.append("scepter")
                        print("You found SCEPTER!")
                        break
                    elif drop == 15:
                        inventory.append("shadowblade")
                        print("**********You found SHADOWBLADE!!!!!!!************")
                        break
                    #if random = 16, user finds 2 items
                    elif drop >= 16:
                        print(".....")
                        time.sleep(1.5)
                        print("LUCKY DROP! You found 2 items.")
                        drop = random.randint(1,15)
                        if drop == 1 or drop == 2 or drop == 3 or drop == 4:
                            inventory.append("tango")
                            print("You found a TANGO!")
                        elif drop == 5 or drop == 6 or drop == 7:
                            inventory.append("salve")
                            print("You found a SALVE!")
                        elif drop == 8 or drop  == 9:
                            inventory.append("amplifier")
                            print("You found an AMPLIFIER!")
                        elif drop == 10 or drop == 11 :
                            inventory.append("superamp")
                            print("***You found a SUPER AMPLIFIER!!!***")
                        elif drop == 12 or drop == 13 or drop == 14:
                            inventory.append("scepter")
                            print("You found SCEPTER!")
                        elif drop == 15:
                            inventory.append("shadowblade")
                            print("**********You found SHADOWBLADE!!!!!!!************")
            
        #Enemy attacking
        print("")
        rivalturn = input(enemy + " is about to attack. Press enter to continue")
        l = random.choice(damage)
        print(miss)
        if counter == 1:
            print(enemy + " uses " + (random.choice(attack)) + ", dealing " + str(l) + " damage")
            print(".....")
            time.sleep(2)
            print("LUCKY COUNTER! " + enemy + "'s attack has reflected.")
            rivalhealth -= l
        if miss == 1:
            print(enemy + " uses " + (random.choice(attack)) + ", dealing " + str(l) + " damage")
            print(".....")
            time.sleep(2)
            print("LUCKY DODGE! " + enemy + " missed their attack")
        else:
            print(enemy + " uses " + (random.choice(attack)) + ", dealing " + str(l) + " damage")
            health -= l
        #Game over
        if health <= 0:
            print(pokemon + " died")
            print("     ***** GAME OVER *****     ")
