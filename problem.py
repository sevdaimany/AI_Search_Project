class Problem:
    def __init__(self , walls , goals):
        self.walls = walls
        self.goals = goals
        

    def isDeadlock(self ,butters):
        for coordinate in butters:
            row = int(coordinate[0:1])
            col = int(coordinate[-1:])
            if not self.isContain(goals , row ,col):
            # check corners #
                if  self.isContain(walls , row -1 ,col) and  self.isContain(walls , row ,col -1):
                    return True
                if  self.isContain(walls , row -1 ,col) and  self.isContain(walls , row ,col +1):
                    return True
                if  self.isContain(walls , row +1 ,col) and  self.isContain(walls , row ,col -1):
                    return True
                if  self.isContain(walls , row +1 ,col) and  self.isContain(walls , row ,col +1):
                    return True

                ## sides ##
                if self.isContain(walls , row-1 , col -1) and self.isContain(walls , row-1 , col ) and self.isContain(walls , row-1 , col +1) and self.isContain(walls , row , col -2) and self.isContain(walls , row , col +2) and (not self.isContain(goals , row , col -1)) and (not self.isContain(goals , row , col +1)):
                    return True
                if self.isContain(walls , row+1 , col -1) and self.isContain(walls , row+1 , col ) and self.isContain(walls , row+1 , col +1) and self.isContain(walls , row , col -2) and self.isContain(walls , row , col +2) and (not self.isContain(goals , row , col -1)) and (not self.isContain(goals , row , col +1)):
                    return True
                if self.isContain(walls , row-1 , col -1) and self.isContain(walls , row , col- 1 ) and self.isContain(walls , row+1 , col -1) and self.isContain(walls , row-2 , col) and self.isContain(walls , row+2 , col ) and (not self.isContain(goals , row-1 , col)) and (not self.isContain(goals , row+1 , col)):
                    return True
                if self.isContain(walls , row-1 , col +1) and self.isContain(walls , row , col +1 ) and self.isContain(walls , row+1 , col +1) and self.isContain(walls , row -2 , col) and self.isContain(walls , row +2  , col) and (not self.isContain(goals , row-1 , col)) and (not self.isContain(goals , row +1, col)):
                    return True
                    
        return False

    def isContain(self ,set , row , col):
        if str(row)+str(col) in set :
            return True
        return False
