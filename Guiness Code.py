u_input = 277777788888899
def check(n):
    done = False
    steps = 0
    while done == False:
        steps = steps+1
        total = 1
        numset = []
        if len(str(n))>1:
            for i in str(n):
                numset.append(i)
                total = total*int(i)
            n = total
        else:
            done = True
            return steps-1
while True:
    if check(u_input)>=11:
        print(u_input)
        print(check(u_input))
    u_input+=1
