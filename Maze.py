from random import shuffle, randrange
from graphics import *
class MyStack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def size(self):
         return len(self.items)

class Maze:
    def __init__(self,n):
         #Initializations for the grids/lists used later on in the code
        self.N=n
        self.path=[]
        self.vforexp=[[0 for i in range(n+2)] for j in range(n+2)]
        self.vforexp2=[[0 for i in range(n+2)] for j in range(n+2)]
        self.visited=[[0 for i in range(n+2)] for j in range(n+2)]
        self.north=[[1 for i in range(n+2)] for j in range(n+2)]
        self.south=[[1 for i in range(n+2)] for j in range(n+2)]
        self.east=[[1 for i in range(n+2)] for j in range(n+2)]
        self.west=[[1 for i in range(n+2)] for j in range(n+2)]
        self.startx,self.starty=1,1
        self.endx,self.endy=self.N,self.N
        valid=0
        while valid==0:
             self.keyx,self.keyy=randrange(1,n+1),randrange(1,n+1)
             if self.keyx==n and self.keyy==n:
                  valid=0
             else:
                  valid=1
                  
        changelist(self.vforexp)
        changelist(self.vforexp2)
        changelist(self.visited)
##        changelist(self.north)
##        changelist(self.south)
##        changelist(self.east)
##        changelist(self.west)
        v,n,s,e,w,startx,starty=self.visited,self.north,self.south,self.east,self.west,self.N,1
        a=0
        tracker=[]
        x=startx
        y=starty
        v[x][y]=1
        tracker.append((x,y))
        while a==0:
            #print(x,y)
            if v[x-1][y]==1 and v[x+1][y]==1 and v[x][y-1]==1 and v[x][y+1]==1:
                x,y=previousspot(x,y,tracker)
            else:
                count=0
                while count==0:
                    r=randrange(1,5)
                    if (r==1 and v[x-1][y]==1) or (r==2 and v[x+1][y]==1) or (r==3 and v[x][y-1]==1) or (r==4 and v[x][y+1]==1):
                        count=0
                    else:
                        count=1
                if r==1:#north
                    n[x][y]=0
                    s[x-1][y]=0
                    x=x-1
                    y=y
                if r==2:#south
                    n[x+1][y]=0
                    s[x][y]=0
                    x=x+1
                    y=y
                if r==3:#west
                    e[x][y-1]=0
                    w[x][y]=0
                    x=x
                    y=y-1
                if r==4:#east
                    e[x][y]=0
                    w[x][y+1]=0
                    x=x
                    y=y+1
                    
                    
                v[x][y]=1
                tracker.append((x,y))
                    
            p=0
            for i in range(len(v)):
                for j in range(len(v[i])):
                    if v[i][j]==1 and p==0:
                        a=1
                    else:
                        p=1
                        a=0
        self.visted,self.north,self.south,self.east,self.west=v,n,s,e,w
        #print(self.visited,"\nNORTH:",self.north,"\nSOUTH:",self.south,"\nEAST:",self.east,"\nWEST:",self.west,"\nTRACKER",tracker)
    def draw(self):
#Key-Green(randomized location),Start of maze-red(always bottom left),end of maze-red(always n,n which is bottom right),path-cyan/lightblue(path for explore to key/end),Start of explore-DarkBlue(for convenience)
        width=800/self.N
        y=-width
        win=GraphWin("Maze",800,800)#size is always 800x800, the size of the cubes change as maze gets bigger
        #win=GraphWin(Maze,800,800)
        Rectangle(Point(2,2),Point(800-1,800-1)).draw(win)
        for i in range(len(self.north)):
            x=-width
            
            for m in range(len(self.north[i])):
                if self.north[i][m]==1:
                    
                    
                    Line(Point(x,y),Point(x+width,y)).draw(win)
                x=x+width
            y=y+width
        y=-width
        
        for i in range(len(self.east)):
            x=0
            
            for m in range(len(self.east[i])):
                if self.east[i][m]==1:
                    
                    
                    Line(Point(x,y),Point(x,y+width)).draw(win)
                x=x+width
            y=y+width
        
        startrec=Rectangle(Point((1*width)-(width-5),(self.N*width)-(width-5)),Point((1*width)-5,(self.N*width)-5))
        startrec.setFill('red')
        startrec.draw(win)
        endrec=Rectangle(Point((self.endy*width)-(width-5),(self.endx*width)-(width-5)),Point((self.endy*width)-5,(self.endx*width)-5))
        endrec.setFill('red')
        endrec.draw(win)
        keyrec=Rectangle(Point((self.keyy*width)-(width-5),(self.keyx*width)-(width-5)),Point((self.keyy*width)-5,(self.keyx*width)-5))
        keyrec.setFill('green')
        keyrec.draw(win)

        
        for i in range(len(self.path)):#The starting point is blue
             if i==0:
                  pathrec=Rectangle(Point((self.path[i][1]*width)-(width-5),(self.path[i][0]*width)-(width-5)),Point((self.path[i][1]*width)-5,(self.path[i][0]*width)-5))
                  pathrec.setFill('blue')
                  pathrec.setOutline("white")
                  pathrec.draw(win)
             if self.path[i]!=(self.endx,self.endy) and self.path[i]!=(self.path[0][0],self.path[0][1]):
                  
                  pathrec=Rectangle(Point((self.path[i][1]*width)-(width-5),(self.path[i][0]*width)-(width-5)),Point((self.path[i][1]*width)-5,(self.path[i][0]*width)-5))
                  pathrec.setFill('cyan')
                  pathrec.setOutline("white")
                  pathrec.draw(win)
        
    def Explore(self,x,y):
         self.startx=x
         self.starty=y
#-------------------START XY TO KEY----------------         
         self.vforexp[x][y]=1
         vforexp=self.vforexp
         vforexp[x][y]=1
         a=0
         exp=MyStack()
         exp.push((x,y))
         repeat=0
         while a==0:
              if (self.north[x][y]==1 or vforexp[x-1][y]==1) and (self.south[x][y]==1 or vforexp[x+1][y]==1) and (self.west[x][y]==1 or vforexp[x][y-1]==1) and (self.east[x][y]==1 or vforexp[x][y+1]==1):
##                if exp.isEmpty()==True:
##                     exp.push((self.startx,self.starty))
                z=exp.pop()
                
                x,y=z[0],z[1]
                repeat=1
                
              else:
                   if repeat==1:
                        exp.push((x,y))
                        repeat=0 
                   count=0
                   while count==0:
                       r=randrange(1,5)
                       if (r==1 and (self.north[x][y]==1 or vforexp[x-1][y]==1))or (r==2 and (self.south[x][y]==1 or vforexp[x+1][y]==1)) or (r==3 and (self.west[x][y]==1 or vforexp[x][y-1]==1)) or (r==4 and (self.east[x][y]==1 or vforexp[x][y+1]==1)):
                           count=0
                       else:
                           count=1
                   if r==1:#north
                       
                       x=x-1
                       y=y
                   if r==2:#south
                       
                       x=x+1
                       y=y
                   if r==3:#west
                       
                       x=x
                       y=y-1
                   if r==4:#east
                       
                       x=x
                       y=y+1
                    
                   vforexp[x][y]=1 
                   
                   exp.push((x,y))
              if x==self.keyx and y==self.keyy:
                   a=1
         route1=[] 
         for i in range(exp.size()):
              route1.append(exp.pop())
              
         route1.reverse() 
#----------------FROM KEY TO END-----------------              
         x=self.keyx
         y=self.keyy
         self.vforexp2[x][y]=1
         vforexp2=self.vforexp2
         vforexp2[x][y]=1
         a=0
         exp2=MyStack()
         exp2.push((x,y))
         repeat=0
         while a==0:
              if (self.north[x][y]==1 or vforexp2[x-1][y]==1) and (self.south[x][y]==1 or vforexp2[x+1][y]==1) and (self.west[x][y]==1 or vforexp2[x][y-1]==1) and (self.east[x][y]==1 or vforexp2[x][y+1]==1):
##                if exp.isEmpty()==True:
##                     exp.push((self.startx,self.starty))
                z=exp2.pop()
                
                x,y=z[0],z[1]
                repeat=1
                
              else:
                   if repeat==1:
                        exp2.push((x,y))
                        repeat=0 
                   count=0
                   while count==0:
                       r=randrange(1,5)
                       if (r==1 and (self.north[x][y]==1 or vforexp2[x-1][y]==1))or (r==2 and (self.south[x][y]==1 or vforexp2[x+1][y]==1)) or (r==3 and (self.west[x][y]==1 or vforexp2[x][y-1]==1)) or (r==4 and (self.east[x][y]==1 or vforexp2[x][y+1]==1)):
                           count=0
                       else:
                           count=1
                   if r==1:#north
                       
                       x=x-1
                       y=y
                   if r==2:#south
                       
                       x=x+1
                       y=y
                   if r==3:#west
                       
                       x=x
                       y=y-1
                   if r==4:#east
                       
                       x=x
                       y=y+1
                    
                   vforexp2[x][y]=1 
                   
                   exp2.push((x,y))
              if x==self.endx and y==self.endy:
                   a=1 
              
         #print("Route found:=","Start point",(self.startx,self.starty),"End point",(self.endx,self.endy))     
         route=[] 
         for i in range(exp2.size()):
              route.append(exp2.pop())
         route.reverse()
         routefinal=[]
         route.pop(0)
         for i in range(len(route1)):
              routefinal.append(route1[i])
         for i in range(len(route)):
              routefinal.append(route[i])
              
         
         
         for i in range(len(routefinal)):
              print(routefinal[i],end=" ")
              if routefinal[i]!=(self.keyx,self.keyy):
                   self.path.append(routefinal[i])
            
            

def changelist(x):#makes borders around the initial grid to avoid special cases
    for i in range(len(x[0])):
        x[0][i]=1
        x[len(x)-1][i]=1
        x[i][len(x)-1]=1
        x[i][0]=1

    return x

def previousspot(x,y,tracker):#To backtrack for maze
    newx=0
    newy=0
    k=1
    for i in range(len(tracker)):
        if x==tracker[i][0] and y==tracker[i][1] and k==1:
            k=0
            newx=tracker[i-1][0]
            newy=tracker[i-1][1]
    return newx,newy


 
            

    
    
    

        
        
    

