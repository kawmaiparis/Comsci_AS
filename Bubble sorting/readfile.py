def readfile(filename):
    file = open(filename,"r")
    data = file.readlines()
    file.close()

    return data

ngo = readfile("textfile.txt")
print(ngo)
