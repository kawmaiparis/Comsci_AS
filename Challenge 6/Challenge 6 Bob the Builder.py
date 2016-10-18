import random
import time
import math

def intro():
    #hi
    print ("Hi. I'm your personal chatbot friend.")
    time.sleep(1.2)
    print ("How are you feeling today?")
    choice = input()
    time.sleep(1)
    if "sad" in choice or "not" in choice or "bad" in choice:
        print ("Aw. What's wrong?")
        wrong = input("")
        time.sleep(0.5)
        print ("I hope you get better soon.")
    else:
        print ("Yay! I'm delighted for you too")

def game():
    #ask whether to play or not to play
    game = input("Wanna play a game? \n")
    if "y" in game or "s" in game or "k" in game:
        print("You get to guess a number between 1 and 4. If your number matches the number in my head, you get one point!")
        time.sleep(3)
        score = 0
        loss = 0
    else:
        time.sleep(1)
        print("Fine then. What a boring life you're living.")

    #if they say yes
    while "y" in game or "s" in game or "ok" in game:
        ans1 = random.randint(1,2)
        if ans1 == 1:
            answer1 = input("Gimme your magic number please \n")
        else:
            answer1 = input("And your lucky number is ?... \n")

        print("...")
        fate1 = random.randint(1,4)
        time.sleep(1)

        #25% of winning
        if fate1 == int(answer1):
            score += 1
            print("Wow. That was some luck. Your score is now " + str(score))
            game = input("Ready for another go? \n")
        else:
            loss += 1
            #ask to play again
            ask = random.randint(1,2)
            if ask == 1:
                game = input("Not quite what I was thinking. Try again? \n")
            else:
                game = input("You missed by only one number. Again? \n")

       

        #change winning percentage to 50 if lose 2 times
        if loss == 2:
            game2 = input("I'll make it easier okay?\n")
            print("How about just the number 1 to 2")
            while "y" in game2 or "s" in game2 or "o" in game2:
                #ask for number
                ans2 = random.randint(1,2)
                if ans2 == 1:
                    answer2 = input("Lucky number please \n")
                else:
                    answer2 = input("And your number is... \n")

                print("...")
                time.sleep(1)
                fate2 = random.randint(1,2)

                #50% of winning
                if fate2 == int(answer2):
                    score += 1
                    print("Yay! Your score is now " + str(score))
                    #print face and stop the loop if score is 3
                    if score == 3:
                        time.sleep(1.5)
                        print ("\n\n                                  O        O\n                                    ______\n\n                             WHY ARE YOU SO GOOD!? \n\n")
                        time.sleep(3)
                        print ("Let's just stop playing, I'm getting bored of you reading my mind")
                        game = "n"
                        game2 = "n"
                    else:
                        game2 = input("Up for winning another round? \n")
                else:
                    loss += 1
                    again = random.randint(1,3)
                    if again == 1:
                        game = input("So close! another guess? \n")
                    elif again == 2:
                        game = input("Still no. How about one more time? \n")
                    elif again == 3:
                        game = input("Aww. Not again. C'mon. play? \n")


                #stop the loop if loses 4 times
                if loss == 3:
                    time.sleep(1.5)
                    print("Actually nah, you really suck at this. Better stop playing before I get cancer")
                    game = "n"
                    game2 = "n"
                    
def questions():
    time.sleep(1)
    identity = input("Please answer a few questions and I'll try to figure out who you are. Alright?\n")
    time.sleep(1.5)
    while "y" in identity or "ok" in identity or "alright" in identity:
        years = input("So how long have you been in Harrow?\n")
        time.sleep(1)
        house = input("What color of tie did you wear last year?\n")
        time.sleep(1)
        subject = input("How about the other AS you're doing? [type 'none' if not any]\n")
        time.sleep(0.5)
        if "2" in years:
            year = "Joined in year 10, "
        elif "3" in years or "4" in years or "5" in years or "6" in years or "7" in years or "8" in years or "9" in years or "10" in years:
            year = "an old student, "
        else:
            year = "Pretty new to Harrow, "

        if "yellow" in house:
            hause = "in keller, "
        elif "blue" in house:
            hause = "in churchill, "
        elif "red" in house:
            hause = "in nehru, "
        else:
            hause = "in an unidentified house, "

        print("hmmmm...")
        time.sleep(0.8)
        if "phy" in subject:
            subjectt = "and wanna be an engineer"
        elif "eco" in subject:
            subjectt = "and wanna run a company"
        elif "media" in subject:
            subjectt = "doing media"
        elif "none" in subject:
            subjectt = "and not a student"
        else:
            subjectt = ""

        print(year + hause + subjectt + " eh?")
        time.sleep(1.5)

        if "none" in subject:
            print("Hey Mr.T")
            name = "Mr.T"
        elif "yellow" in house:
            if "f" in subject:
                print("Hey Aof!")
                name = "Aof"
            else:
                print("Hey Smart!")
                name = "Smart"
        elif "blue" in house:
            if "f" in subject:
                print("It's been my greatest pleasure talking to you, Sia Ruj")
                name = "Sia Ruj"
            else:
                print("*Sigh* fat gunn.")
                name = "fat gunn"
        elif "red" in house:
            print("Hey Allan!")
            name = "Allan"
        elif "months" in years:
            print("Hey Victor!")
            name = "Victor"
        else:
            print("You're not in this class, stranger")
            name = "Stranger"

        time.sleep(1)
        identity = input("I got your name right, didn't I? If not, do you want me to try again? [say 'no' if you want to move on]\n")
        

def chat():
    print("Okay it's your turn. Feel free to ask me anything you like. [say 'bye' or 'stop' to quit]")
    while True:
        question = input("")
        time.sleep(1)
        if "how are you" in question:
            print("I'm fine for a program i guess.")
        elif "hi" in question or "hello" in question:
            print("Hi. Again.")
        elif "robot" in question:
            print("I dont know. Am I? \n Are you?\n you tell me")
        elif "color" in question:
            print("Um...My favorite color is 110001001001000011010")
        elif "am i" in question:
            print("Are you?")
        elif "gay" in question:
            print("No. You are")
        elif "joke" in question:
            print("I went to the zoo the other day.")
            time.sleep(1.5)
            print("there was one animal in it.")
            time.sleep(1.5)
            print("It was a shitzu.")
        elif "hobby" in question or "job" in question or "hobbies" in question :
            print("Hence the name 'chatbot'. Yes, my hobby, my job, and my life is to chat")
        elif question == "why" or question == "y":
            print("Why not?")
        elif "paris" in question:
            print("How dare you speak those filthy lies about my god, peasant.")
        elif "ha" in question:
            print("Funny.")
        elif "com" in question:
            print("please stop mentioning any computer relating terms, I'm sick of 'em")
        elif "bye" in question or "stop" in question:
            print("Byebye hooman.")
            break
        else:
            print("ahhhh... Let's change the topic")

def dance():
    for dance in range(3):
        print("\n\n")
        time.sleep(0.2)
        print("(•_•)             (•_•)            (•_•)\n<)   )╯          <)   )╯          <)   )╯\n /    \           /    \            /    \  \n\n")
        time.sleep(0.2)
        print("  (•_•)             (•_•)             (•_•)\n<(   (>            <(   (>           <(   (> \n/   \              /    \            /    \  ")

intro()
questions()
game()
chat()
dance()
