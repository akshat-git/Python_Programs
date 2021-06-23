def Knapsack(maxWeight, items):
    matrix = [[0 for col in range(maxWeight+1)] for row in range(len(items[0]))]
    for row in range(len(items[0])):
        for col in range(maxWeight+1):
            if items[0][row] > col:
                matrix[row][col] = matrix[row-1][col]
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row-1][col-items[0][row]]+items[1][row])
    for i in range(len(items[0])):
        print(matrix[i])
    packed = []
    col = maxWeight
    for row in range(len(items[0])-1,-1,-1):
        if row == 0 and matrix[row][col] != 0:
            packed.insert(0,row)
        if matrix[row][col] != matrix[row-1][col]:
            packed.insert(0,row)
            col-= items[0][row]
    print(packed)
    print("Maximum Total Value of Knapsack is",matrix[len(items[0])-1][maxWeight])
itemdict = {
#    weight :   value
        3   :   7,
        1   :   2,
        2   :   4,
        4   :   5
}
itemWeights = []
itemValues = []
for k,v in itemdict.items():
    itemWeights.append(k)
    itemValues.append(v)
items = [itemWeights,itemValues]
inputMaxWeight = int(input("Max Knapsack Weight: "))
Knapsack(inputMaxWeight,items)