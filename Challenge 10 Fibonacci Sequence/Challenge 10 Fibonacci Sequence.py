seq = []
n = 0
unit = int(input("Number of places generated: "))
if unit == 1:
    seq.append(n)
    print(seq)
elif unit == 2:
    for start in range(2):
        seq.append(n)
        n += 1
        print(seq)
else:
    for start in range(2):
        seq.append(n)
        n += 1
        print(seq)
    posi = 0
    count = 2
    while True:
        n = seq[posi] + seq[posi + 1]
        seq.append(n)
        print(seq)
        posi+= 1
        count += 1
        if count == unit:
            break
            
