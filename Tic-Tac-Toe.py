import numpy as np
class Board:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        self.board = np.array([["-", "-", "-"],
                                                ["-", "-", "-"],
                                                ["-", "-", "-"]])
    def cell_update_1(self, x, y):
        self.board[x-1,y-1] = self.char1
        
    def cell_update_2(self, x, y):
        self.board[x-1,y-1] = self.char2

    def display(self):
        for i in self.board:
            print((i[0]+"  "+i[1]+"  "+i[2]))

    def check(self):
        if self.board[0,0] == self.board[0,1] and self.board[0,1] == self.board[0,2] and self.board[0,0] != '-':
            print(self.board[0,0]+" has won the game!")
            return True
        elif self.board[1,0] == self.board[1,1] and self.board[1,1] == self.board[1,2] and self.board[1,0] != '-':
            print(self.board[1,0]+" has won the game!")
            return True
        elif self.board[2,0] == self.board[2,1] and self.board[2,1] == self.board[2,2] and self.board[2,0] != '-':
            print(self.board[2,0]+" has won the game!")
            return True
        elif self.board[0,0] == self.board[1,0] and self.board[1,0] == self.board[2,0] and self.board[0,0] != '-':
            print(self.board[0,0]+" has won the game!")
            return True
        elif self.board[0,1] == self.board[1,1] and self.board[1,1] == self.board[2,1] and self.board[0,1] != '-':
            print(self.board[0,1]+" has won the game!")
            return True
        elif self.board[0,2] == self.board[1,2] and self.board[1,2] == self.board[2,2] and self.board[0,2] != '-':
            print(self.board[0,2]+" has won the game!")
            return True
        elif self.board[0,0] == self.board[1,1] and self.board[1,1] == self.board[2,2] and self.board[0,0] != '-':
            print(self.board[0,0]+" has won the game!")
            return True
        elif self.board[2,0] == self.board[1,1] and self.board[1,1] == self.board[0,2] and self.board[1,1] != '-':
            print(self.board[1,1]+" has won the game!")
            return True
        else:
            return False

t = Board('X','O')
z=0
won = False
while z<10 and won == False:
    x = int(input("x-coord: "))
    y = int(input("y-coord: "))
    while t.board[y-1,x-1] != "-":
        print("Taken! Retry! ")
        t.display()
        x = int(input("x-coord: "))
        y = int(input("y-coord: "))
    if z%2 ==0:
        t.cell_update_1(y,x)
    else:
        t.cell_update_2(y,x)
    t.display()
    if t.check():
        won = True
    else:
        z+=1
if won == False :
    print("Draw...")



