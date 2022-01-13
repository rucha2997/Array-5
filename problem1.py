#Time , space O(n)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dir = [[0,1],[-1,0],[0,-1],[1,0]] #NWSE
        
        idx=0
        x=0
        y=0
        
        for i in range(len(instructions)):
            cur = instructions[i]
          
        #For left
            if cur == "L":
                idx=(idx+1)%4
        #Right
            elif cur == "R":
                idx = (idx+3)%4
        #For G
            else:
                x=x+dir[idx][0]
                y=y+dir[idx][1]
                
        return (x==0 and y==0) or idx!=0
        
