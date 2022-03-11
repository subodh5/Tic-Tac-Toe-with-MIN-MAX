from board import board
from player import player
import cpu
#minmax algorithm
def minmax(b, maximizing):
    #base case:
    if b.getwinner()=="X":
        return -10
    if b.getwinner()=="O":
        return 10
    if b.isfull() and not b.getwinner():
        return 0


    
    if maximizing:
        maxscore = -99    
        for i in range(3):
            for j in range(3):
                if b.checkEmptypos(i,j):
                    b.update(i,j,'O')
                    score=minmax(b,False)
                    b.update(i,j,'_')
                    if score>maxscore:
                        maxscore=score
        return maxscore
    
    else :                         
        minscore = 99    
        for i in range(3):
            for j in range(3):
                if b.checkEmptypos(i,j):
                    b.update(i,j,'X')
                    score=minmax(b,True)
                    b.update(i,j,'_')
                    if score<minscore:
                        minscore=score
        return minscore


if __name__=="__main__":
    b1=board()
    print("Player1: X   CPU: O")
    print("Initial position:")
    b1.display()
    p1=player()
    cpu=cpu.opponent()

    #game loop
    while True:
        p1.move(b1)
        print("Player:")
        b1.display()
        winner=b1.getwinner()
        if winner:
            print("The winner is :",winner)
            break

        if b1.isfull():
            print("Draw")
            break

        cpu.move(b1)
        print("CPU: ")
        b1.display()
        winner=b1.getwinner()
        if winner:
            print("The winner is :",winner)
            break
        
        if b1.isfull():
            print("Draw")
            break


    
