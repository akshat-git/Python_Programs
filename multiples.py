class Gates:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        
class And(Gates):
    def __init__(self, between, mult1, mult2):
        super().__init__(between[0], between[1])
        self.mult1 = mult1
        self.mult2 = mult2
        self.count = self.evaluate(self.mult1, self.mult2)
    def evaluate(self, mult1, mult2):
        for i in range(self.start, self.end+1):
            if (i % mult1 == 0) and (i % mult2 == 0):
                self.count += 1
        return self.count
    def __str__(self):
        return str(self.mult1)+" and " + str(self.mult2) + ": "+str(self.count)
        
class Nand(Gates):
    def __init__(self, between, mult1, mult2):
        super().__init__(between[0], between[1])
        self.mult1 = mult1
        self.mult2 = mult2
        self.count = self.evaluate(self.mult1, self.mult2)
    def evaluate(self, mult1, mult2):
        for i in range(self.start, self.end+1):
            if not((i % mult1 == 0) and (i % mult2 == 0)):
                self.count += 1
        return self.count
    def __str__(self):
        return "not both " + str(self.mult1) + " and " + str(self.mult2) + ": " + str(self.count)
        
class Or(Gates):
    def __init__(self, between, mult1, mult2):
        super().__init__(between[0], between[1])
        self.mult1 = mult1
        self.mult2 = mult2
        self.count = self.evaluate(self.mult1, self.mult2)
    def evaluate(self, mult1, mult2):
        for i in range(self.start, self.end+1):
            if (i % mult1 == 0) or (i % mult2 == 0):
                self.count += 1
        return self.count
    def __str__(self):
        return str(self.mult1)+" or " + str(self.mult2) + ": "+str(self.count)
        
class Nor(Gates):
    def __init__(self, between, mult1, mult2):
        super().__init__(between[0], between[1])
        self.mult1 = mult1
        self.mult2 = mult2
        self.count = self.evaluate(self.mult1, self.mult2)
    def evaluate(self, mult1, mult2):
        for i in range(self.start, self.end+1):
            if not ((i % mult1 == 0) or (i % mult2 == 0)):
                self.count += 1
        return self.count
    def __str__(self):
        return str(self.mult1)+" nor " + str(self.mult2) + ": "+str(self.count)

class Is(Gates):
    def __init__(self, between, mult):
        super().__init__(between[0], between[1])
        self.mult = mult
        self.count = self.evaluate(self.mult)
    def evaluate(self, mult):
        for i in range(self.start, self.end+1):
            if (i % mult == 0):
                self.count += 1
        return self.count
    def __str__(self):
        return str(self.mult)+": "+str(self.count)
        
class Not(Gates):
    def __init__(self, between, mult):
        super().__init__(between[0], between[1])
        self.mult = mult
        self.count = self.evaluate(self.mult)
    def evaluate(self, mult):
        for i in range(self.start, self.end+1):
            if not (i % mult == 0):
                self.count += 1
        return self.count
    def __str__(self):
        return "not " + str(self.mult)+": "+str(self.count)

def ndigitnum(num):
    out1 = int("1"+(num-1)*"0")
    out2 = int(num*"9")
    return (out1,out2)

while True:
    mult = input("Factors: ").replace(" ","").split(",")
    inputrange = input("Range: ").replace(" ","").split("-")
    for i in range(len(inputrange)):
        inputrange[i] = int(inputrange[i])
    for i in range(len(mult)):
        mult[i] = int(mult[i])
    if len(inputrange) == 1:
        inputrange = ndigitnum(inputrange[0])
    if len(mult) == 2:
        a = And(inputrange,mult[0],mult[1])
        b = Nand(inputrange,mult[0],mult[1])
        c = Or(inputrange,mult[0],mult[1])
        d = Nor(inputrange,mult[0],mult[1])
        print(a)
        print(b)
        print(c)
        print(d)
        print()
    if len(mult) == 1:
        a = Is(inputrange,mult[0])
        b = Not(inputrange,mult[0])
        print(a)
        print(b)
        print()
        



        
        
        
