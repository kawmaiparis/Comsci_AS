top = [4,1,9,3,2]

for c in range(len(top)):
        posi = 0
        for z in range(len(top)-1):
                if top[posi] > top[posi+1]:
                        value = top[posi]
                        top.remove(value)
                        top.insert(posi+1,value)
                posi = posi + 1

print(top)
