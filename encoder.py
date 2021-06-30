offset = int(input("What is the offset for the encryption? "))
caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while True:
    in_message = input("What is your message? ")
    message = in_message
    output = ""
    exist = False
    for i in range(len(message)):
        exist = False
        for j in range(len(alpha)):
            if alpha[j] == message[i]:
                output = output+alpha[(j+offset)%26]
                exist = True
            elif (alpha[j].upper()) == message[i]:
                output = output+(alpha[(j+offset)%26].upper())
                exist = True
        if exist == False:
            output = output+message[i]
            

    print(output).reverse()
            
    
