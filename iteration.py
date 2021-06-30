counter=0
for i in range(1000,2000):
    j = str(i)
    if j[0] == j[1] or j[0] == j[2] or j[0] == j[3] or j[1] == j[2] or j[1] == j[3]  or j[2] == j[3] :
            counter += 1
print(str(counter),"different integers")
