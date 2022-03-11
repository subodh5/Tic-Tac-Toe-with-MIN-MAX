class board():
    def __init__(self):
        self.b_arr=[['_','_','_'],
                    ['_','_','_'],
                    ['_','_','_']]

        self.fullempty=True

    def checkEmptypos(self,i,j):
        if self.b_arr[i][j] == '_':
            return True
        return False

    def isfull(self):
        for rows in self.b_arr:
            if '_' in rows:
                return False
        return True

    def getwinner(self):
        #horizontal
        if self.fullempty:
            return False

        for i in range(3):
            if self.b_arr[i][0]==self.b_arr[i][1]==self.b_arr[i][2] !='_':
                return self.b_arr[i][0]

        #vertical
        for i in range(3):
            if self.b_arr[0][i]==self.b_arr[1][i]==self.b_arr[2][i] !='_':
                return self.b_arr[0][i]
        
        #diagonal
        if self.b_arr[0][0]==self.b_arr[1][1]==self.b_arr[2][2] !='_':
            return self.b_arr[0][0]
        if self.b_arr[0][2]==self.b_arr[1][1]==self.b_arr[2][0] !='_':
            return self.b_arr[0][2]
        
        return False


    def update(self,i,j,char):
        self.b_arr[i][j]=char 
        self.fullempty=False               

    def display(self):
        for line in self.b_arr:
            print (' '.join(map(str, line)))