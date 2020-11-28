import datetime    
d = datetime.datetime.now()
date = float(str(d.strftime("%m"))+"."+str(d.strftime("%d")))
for x in items:
    if items[x] <= date + limit and (items[x] - date) > 0:
        print(x,", ",floor((items[x]-date)*100)," days left", sep = "")
        
