class player():
    def __init__(self):
        self.char='X'

    def move(self,b):
        valid=True
        while valid:
            self.pos=int(input("Enter the position(1-9):"))
            i=int((self.pos-1)/3)
            j=(self.pos-1)%3
            if b.checkEmptypos(i,j):
                valid=False
            else:
                print("Position already occupied")
        b.update(i,j,self.char)