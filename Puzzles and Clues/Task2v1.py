#Paris & Ruj
# open file name ()
def clues(filename):
    fi = open(filename,"r")
    # read lines in the file and store it in data1 
    data1=fi.readlines()
    # close the file
    fi.close()
    # use n variable to count line
    n = 0
    # for loops to run throught everyline in data1 
    for line in data1:
    # for every lines in data1 stripe off "\n"
        data1[n]=line.strip("\n")
    # n will increase by one everytime it runs through
        n += 1
    # check if it works by running 2 comments below
    #for line2 in data1:
        #print(line2)
    # now we return the data to data1
    return data1

