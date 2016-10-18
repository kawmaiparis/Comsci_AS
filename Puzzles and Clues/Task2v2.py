#version2
# call for file name
def clues(filename):
# open file
    fi= open(filename,"r")
# read filen and store it as variable data1 
    data1=fi.readlines()
# close file
    fi.close()
# print all the line in data1
# end="" to print line to line as text file already have /n at the end
    for line in data1:
        print(line)
# make data1 store it in ans
    return data1
ans = clues("clues.txt")
