def readfile(filename):
    myfile = open(filename,"r")
    data = myfile.readlines()
    myfile.close()

    return data

def strip(filename):
    myfile = open(filename,"r")
    data = [line.replace("\n","") for line in myfile]
    myfile.close()

    return data

def write(filename, stuff):
    myfile = open(filename, "w")
    myfile.write(stuff)
    myfile.close()


write("gunrukpatty.txt","I love you")
ngo = readfile("textfile.txt")
print(ngo)
