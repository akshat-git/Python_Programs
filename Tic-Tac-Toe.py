import time
box1 = '_'
box2 = '_'
box3 = '_'
box4 = '_'
box5 = '_'
box6 = '_'
box7 = '_'
box8 = '_'
box9 = '_'

done = False
numtaken = []
turns = ["X","O"]
turnnum = 0
turn = turns[turnnum]
Line1 = [box1,box2,box3]
Line2 = [box4,box5,box6]
Line3 = [box7,box8,box9]

while done != True:
    boxinput = input("What box number should be filled? ")
    turn = turns[turnnum]
    taken = False
    for i in numtaken:
        if i == boxinput:
            taken = True
    if taken == False:
        turn = turns[turnnum]
        turnnum = (turnnum+1)%2
        if boxinput == "1":
            box1 = turn
        if boxinput == "2":
            box2 = turn
        if boxinput == "3":
            box3 = turn
        if boxinput == "4":
            box4 = turn
        if boxinput == "5":
            box5 = turn
        if boxinput == "6":
            box6 = turn
        if boxinput == "7":
            box7 = turn
        if boxinput == "8":
            box8 = turn
        if boxinput == "9":
            box9 = turn
        numtaken.append(boxinput)
        Line1 = [box1,box2,box3]
        Line2 = [box4,box5,box6]
        Line3 = [box7,box8,box9]
        print(box1,box2,box3)
        print(box4,box5,box6)
        print(box7,box8,box9)
        if box1 == box2 and box2 == box3 and box1 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box4 == box5 and box5 == box6 and box4 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box7 == box8 and box8 == box9 and box7 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box1 == box4 and box4 == box7 and box1 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box2 == box5 and box5 == box8 and box2 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box3 == box6 and box6 == box9 and box3 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box1 == box5 and box5 == box9 and box1 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True

        elif box3 == box5 and box5 == box7 and box3 != '_':
            print("THE PLAYER",turn,"HAS WON!!")
            done = True
            
        elif box1 != '_' and box2 != '_' and box3 != '_' and box4 != '_' and box5 != '_' and box6 != '_' and box7 != '_' and box8 != '_' and box9 != '_':
            print("Draw")
            done = True

    else:
        print("Taken! Try again! ")
time.sleep(1)
print("GOODBYE") 
