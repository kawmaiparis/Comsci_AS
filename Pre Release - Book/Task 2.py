while True:
    print("1. display the file contents")
    print("2. search the array for a particular book")
    print("3. end the program")
    choice = input("") #DECLARE choice : string
    if choice == "1":
        myfile = open('BOOK-FILE.txt','r') #DECLARE myfile : file
        top = [line.replace("\n","") for line in myfile] #DECLARE top : string
        print(top)
        myfile.close()
    elif choice == "2":
        filebook = open('BOOK-FILE.txt','r') #DECLARE filebook : file
        title = [line.replace("\n","") for line in filebook] #DECLARE title : string
        print("Enter book")
        thisbook = input("") #DECLARE thisbook : string
        n = 0 #DECLARE n = integer
        isfound = False #DECLARE isfound : boolean
        for i in range(len(title)):
            if thisbook == title[n]:
                print("BOOK FOUND!")
                isfound = True
            n += 1
        if isfound == False:
            print("BOOK NOT FOUND!")
            
    elif choice == "3":
        break
