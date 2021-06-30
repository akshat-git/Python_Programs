choices1 = [1,2,3,4,5,6]
choices2 = [1,2,3,4,5,6]
totalcase = len(choices1)*len(choices2)
counter = 0
for i in choices1:
    for j in choices2:
        if i >= j:
            counter += 1
print(counter,"/",totalcase)
