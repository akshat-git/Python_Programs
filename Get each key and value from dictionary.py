num = "Madeleines : 4.19"
colon = False
first = ""
second = ""
for i in num:
    if colon == False and (i != ":" or i != " " ):
        first = first + i
    elif i == ":":
        colon = True
    elif colon == True and (i != ":" or i != " " ):
        seond = second + i
second = float(second)
