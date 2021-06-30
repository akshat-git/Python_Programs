height = int(input("What is the unit of your pyramid? "))
unit = input("What is the character for each block? ")+" "
spaces = ""
for i in range(height):
    spaces = spaces + " "
for i in range(height+1):
    print(spaces,unit*i)
    spaces = spaces-" "
