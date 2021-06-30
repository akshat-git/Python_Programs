

#calculates the bianry value of any number input
done = False
while done == False:
        numinputorig= input("What is the number you want? ")
        if numinputorig == "leave":
           done = True 
        else:
                numinput = int(numinputorig)
                numoutput = ""
                x = 0

                while 2**(x+1) <= numinput:
                    x = x+1
                while x >= 0:
                    if 2 ** x > numinput:
                        numoutput = numoutput + "0"
                    elif 2 ** x <= numinput:
                        numoutput = numoutput + "1"
                        numinput = numinput - 2**x
                    x = x-1

                print(numoutput)
            
