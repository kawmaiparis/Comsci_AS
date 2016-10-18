import statistics
import math
import time

mark = []
run = "yesh"
while "y" in run:
    try:
                print("1.For\n2.While")
                option = input("")
                print("")
                if option == "1":
                        position = 1
                        n = input("Number of scores you want to add: ")
                        n = int(n)
                        pos = 0
                        for o in range(0,n,1):
                                score = input(str(position) + ". " )
                                mark.append(int(score))
                                position += 1
                if option == "2":
                        position = 1
                        print("Type 'done' or press enter to stop")
                        while True:
                                score = input(str(position) + ". ")
                                position += 1
                                if score == "done" or score == "":
                                    break
                                else:
                                    mark.append(int(score))
                                

                mean = statistics.mean(mark)
                median = statistics.median(mark)
                total = sum(mark)
                time.sleep(1)
                print("Mean: " + str(mean))
                print("Median: " + str(median))
                print("Total: " + str(total))
                run = input("Again? ")
                mark = []
    except:
        print("Invalid command. Please try again")

        
