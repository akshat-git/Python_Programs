import random
import time
numer = int(input("What number of chances? "))
denom = int(input("What is total num of chances? "))
while True:
    randnum = random.randint(1,denom)
    if randnum > numer:
        dots = (".")
        print(dots)
    else:
        print(">>>")
    time.sleep(0.1)
