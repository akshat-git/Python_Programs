root = int(input("Coefficient: "))
linear=int(input("Linear term: "))
factors=[]
done = False
for i in range(linear,linear*(-1)+1):
    if i != 0 and i != 1 and i != -1 and linear%i==0:
        factors.append(i)
for i in factors:
    if i+(linear/i) == root:
        done = True
        print("(x + ( ",i," )) (x + ( ",int(linear/i)," ))",sep = "")
    else:
        pass
if done == False:
    print("No factors")
    
