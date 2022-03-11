from main import minmax
class opponent():
    def __init__(self):
        self.char='O'
    
    def move(self,b):
        maxscore=-99
        for i in range(3):
            for j in range(3):
                if b.checkEmptypos(i, j):
                    b.update(i, j, self.char)
                    score=minmax(b,False)
                    b.update(i, j, '_')
                    if score>maxscore:
                        maxscore=score
                        best_i=i
                        best_j=j
                    
        b.update(best_i,best_j,self.char)
