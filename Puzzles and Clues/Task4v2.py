#Task4 v2
# Paris & Ruj
# when input= addClues running def function 
def addClues(puzzle):
# print what's in puzzle
    print(puzzle)
# ask user to input letter to pair
        letter = input("choose letter for pairing: ")
# check if letter have any pair or not
        if letter in puzzle:
            print("letter's already been paired")
# if not ask user to input symbol to pair with
        else:
            symbol= input("Choose symbol to pair with a letter: ")
# run to check is the symbol available to pair
            if symbol in puzzle:
                print("symbol's already been paired")
# if it can be paired then letter+ symbol
# add the pairing in to newclue list
# return puzzle 
            else:
                newClue = letter+symbol
                print(newClue)
                puzzle.append(newClue)
                return puzzle

    
                  

    
