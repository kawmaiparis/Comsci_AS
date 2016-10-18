import time
import random

top = [0]
player = []
while True:
    #option
    print("1. Show Highscore")
    print("2. Play game")
    choice = input("")
    if choice == "1":
            #open text and read highscore
            myfile = open('text.txt','r+')
            top = [line.replace("\n","") for line in myfile]
            #reject if text file is empty
            if len(top) == 0:
                print("")
                print("No highscore recorded!!!")
                print("")
            #put highscore in list
            else:
                top.pop(0)
                print("")
                num = 0
                for i in range(len(top)):
                        num = num + 1
                        print("        " + str(num) + "." + " " + str(top[i]))
                print("")
                myfile.close()
                top = [0]
                player = []
        
    if choice == "2":
            pause = random.randint(0,4)
            #user type anything to signal the start
            start = input("Press enter to start! ")
            start = 'a'
            if start == 'a':
                    time.sleep(pause)
                    #get random words from text file
                    mywords = open('word_list.txt','r+')
                    words = [line.replace("\n","") for line in mywords]
                    start = time.time()
                    #repeat 5 times
                    for go in range(5):
                        A = random.choice(words)
                        print(A)
                        answer = 0
                        #check whether user's answer matches the given word
                        while answer != A:
                            answer = input("")
                            if answer == A:
                                break
                            #reject if user misspells
                            else:
                                print("Spelling is important in life. Please Do take your time to try again.")
                    end =time.time()
                    #store time as 'score' variable
                    score = round(end-start,2)
                    print(str(score) + "\n")
                    if 0 in top:
                        top.remove(0)

            #Get HIGHSCORES from textfile
            myfile = open('text.txt','r+')
            top = [line.replace("\n","") for line in myfile]
            if len(top) != 0:
                top.pop(0)
                #remove everything else other than the numbers and store in 'top'
                for i in range(len(top)):
                    temp1 = list(top[i-1])
                    for p in range(len(temp1)-5):
                        temp1.pop(5)
                    if "-" in temp1:
                        temp1.remove("-")
                    paris = "".join(temp1)
                    top[i-1] = float(paris)
            #add score to 'top'
            top.append(score)
            myfile.close()

            player = []

            #Get players' names from textfile
            myfile = open('text.txt','r+')
            player = [line.replace("\n","") for line in myfile]
            #remove everything else other than the names and store in 'player'
            if len(player) != 0:
                player.pop(0)
                for i in range(len(player)):
                    temp2 = list(player[i-1])
                    if temp2[5] == "-":
                        for p in range(7):
                            temp2.pop(0)
                    elif temp2[6] == "-":
                        for p in range(8):
                            temp2.pop(0)
                    elif temp2[4] == "-":
                        for p in range(6):
                            temp2.pop(0)
                    else:
                        for p in range(9):
                            temp2.pop(0)
                    nut = "".join(temp2)
                    player[i-1] = nut
            myfile.close()

            #BUBBLE SORT!
            for c in range(len(top)):
                posi = 0
                for z in range(len(top)-1):
                        if top[posi] > top[posi+1]:
                                value = top[posi]
                                top.remove(value)
                                top.insert(posi+1,value)
                        posi = posi + 1
            #remove last number if total > 10
            if len(top) > 10:
                top.pop(10)

            #ask for user's name if they made it to the top ten
            if score in top:
                for i in range(len(top)):
                    if top[i] == score:
                        rank = i
                name = input("You made it to the top ten! Name: ")
                player.insert(rank,name)
                #remove last player's name from 'player'
                if len(player) == 11:
                    player.pop(10)
            
            #open textfile and clear everything and store new highscores + names instead
            myfile = open('text.txt','r+')
            myfile.truncate()
            myfile.write("HIGHSCORE!")
            myfile.write("\n")
            for a in range(len(top)):
                myfile.write(str(top[a]))
                myfile.write(" - ")
                myfile.write(str(player[a]))
                myfile.write("\n")
            myfile.close()
