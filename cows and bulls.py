from random import *
done = False
randnum = randint(999,9999)
while done == False:
    cows = 0
    bulls = 0
    numinput = input("What number do you chose? ")
    for i in range(len(numinput)):
        for j in range(len(str(randnum))):
            if numinput[i] == str(randnum)[j] and i != j:
                cows = cows + 1
            if numinput[i] == str(randnum)[j] and i == j:
                bulls = bulls + 1
    if bulls == 4:
        done = True
    else:
        print("Cows:",cows)
        print("Bulls:",bulls)
print("You got it !!")
