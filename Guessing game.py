import random
numtofind = random.randint(1,100)
gotit = False
tries = 0
print("Welcome to the guessing game! You will guess numbers from 1 to 100")
print("We will choose a number and you will try to guess it till you type 'quit' ")
hardness = int(input("How hard do you want it to be? 1 is hardest, 5 is easiest! "))
if hardness < 1 or hardness > 5:
    print("")
    print("***Invalid hardness number***")
    hardness = int(input("How hard do you want it to be? 1 is hardest, 5 is easiest! "))
while gotit == False:
    tries = tries+1
    strnuminput = input("What do you guess? ")
    if strnuminput == "quit":
        print("Bye, hope you play again!")
        gotit = True
        
    else:
        numinput = int(strnuminput)
        if numinput > 100:
            print("Numbers from 1 to 100 would help your score")
        elif numinput <= 0:
            print("Numbers from 1 to 100 would help your score")
        else:
            if numinput > numtofind:
                print("Sorry, too high")
                if (numinput-numtofind)<=hardness:
                    print("You are very close though!")
                print("")
            elif numinput < numtofind:
                print("Sorry, too low")
                if (numtofind-numinput)<=hardness:
                    print("You are very close though!")
                print("")
            elif numinput == numtofind:
                gotit = True
                print("*********************")
                print("GOOD JOB !!!! YOU GOT IT IN",tries,"TRIES")
print("Goodbye!") 
