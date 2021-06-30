import time
import winsound
numofsec = int(input("What is the length in seconds of your desired timer?  "))


while numofsec > 0:
    start_time = time.clock()
    print(numofsec)
    winsound.Beep(3000,150)
    time.sleep(1-(time.clock() - start_time))
    numofsec = numofsec - 1
winsound.Beep(3000,3000)
        


