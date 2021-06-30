reps = {}
product = 1
def factorial(x):
    numsum = 1
    for i in range(1,x+1):
        numsum = numsum*i
    return numsum


while True:
    word = input("Word: ")
    for i in word:
        reps[i] = 0
    for i in word:
        reps[i] +=1
    div = 1
    for i in reps.values():
        div = div*(factorial(i))
    product = factorial(len(word))
    print(str(product/div),"ways")
