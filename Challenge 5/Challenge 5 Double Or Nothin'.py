import random
print("double or nothin'!!! You now have a score of 1")

#player starts with a score of 1!
score = 1
loss = 0
win = 0
#player decides whether to take their chance
play = input("Are you in for this!? [y/n]: ")

while play.lower() == 'y':
    fate = random.randint(0,3)
    #25% of losing, 75% of winning
    if fate == 0:
        print ("...AWW, you just lost all your points")
        loss += 1

    #score is doubled if player wins
    else:
        score = score*2
        print ("...YEAHHH, your score is now: " + str(score))
        win += 1
 

    #ask player to play again
    play = input("Play again? [y/n]: ")
    #stop the game after player lose for the third time
    if loss == 2:
        print ("You Suck. QUIT YOUR LIFE.")
        break

    #triple the points if they win 3 times
    if win == 3:
        score = score*3
        print ("x3 Bonus Points. Your score is now: " + str(score))

    if score == 16:
        score = score*1.5
        print ("your luck is too good, let's triple the score")

if play == 'n':
    print ("BOOOO!")
