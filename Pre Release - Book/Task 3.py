import random

while True:
    x = int(input('first integer: ')) #DECLARE x : integer
    y = int(input('second integer: ')) #DECLARE y : integer
    if y-x >= 20:
        break
    print("invalid input")

hold = [] #DECLARE hold : array
while len(hold) != 20:
    gen = random.randint(int(x),int(y)) #DECLARE  gen : integer
    if gen not in hold:
        hold.append(gen)

for line in range(len(hold)):
    print(hold[line])
