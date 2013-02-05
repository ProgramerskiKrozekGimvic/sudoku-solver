# "2456.......32.......4"

class Sudoku:
    def __init__(self):
        self.s = []
        self.p = [[1, None, 7, None, None, 3, None, 2, 9],
                  [None, None, 8, 5, 2, None, None, None, None],
                  [2, None, None, None, 7, 1, 6, None, None],
                  [None, 8, None, 3, None, None, 9, None, None],
                  [None, 3, 6, 4, 8, 7, None, None, None],
                  [None, None, 4, 6, None, None, 8, 7, 3],
                  [None, None, None, None, None, 4, None, 5, 8],
                  [None, None, None, None, 3, None, None, None, 2],
                  [6, 4, None, 2, 5, None, None, None, None]]
    def draw(self):
        for i in self.p:
            print(i)
        print()
        


    def validmovesV(self,x,a):  #x= vrstica, y = stolpc
        
        
        for i in range(len(self.p[x])):        
        #for i in self.p[x]:
            if self.p[x][i] == a:
                
                return False
        
        return True
    
    def validmovesS(self,y, a):
            
        for i in range(len(self.p)):
            if self.p[i][y] == a:
                
                return False
        
            
        return True
    
    def validmovesK(self,x,y,a):
        z = x // 3
        o = y //3
        for i in range(3):
            #self.p[z*3][o*i]
            for j in range(3):
                #print(self.p[z*3 + i][o*3 + j])
                if self.p[z*3 + i][o*3 + j] ==a:
                    
                    return False
        
        return True
    def validN(self,x,y):
        if self.p[x][y] !=None:
            return False
        return True
    def valid(self,x,y,a):
        if self.validmovesV(x,a) and self.validmovesS(y,a) and self.validmovesK(x,y,a)and self.validN(x,y):
            
            return True
        
        return False
    

    def makemove(self):
        
        
        for i in range(9):
            for j in range(9):
                
                for g in range(1,10):
                
                    if self.valid(i,j,g):
                        self.p[i][j] = g
            self.draw()
                    
    
                
                




a = Sudoku()

a.makemove()


