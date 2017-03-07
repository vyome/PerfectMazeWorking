"""To find a solution for a randomly generated maze where you have a starting point, a key and an ending point. The path would first find the path to reach the key from the starting point and then find the path from the key to the ending point. The path will be found by using an implemented stack. Finally, it will display the path it took to complete the maze using graphics."""

from random import shuffle, randrange#imports libraries used to random numbers
from graphics import *#imports libraries used to display graphics

class MyStack:#implements a stack structure which will be used in the process of path finding
     def __init__(self):#initialization of class constructor 
         self.items = []#initializes the stack as empty 

     def isEmpty(self):#to check if a stack is empty 
         return self.items == []#returns true if the stack is empty

     def push(self, item):#to push an item on to the stack where item is the item to be added to the list
         self.items.append(item)#adds the item to the end of the list

     def pop(self):#to pop an item off the stack 
         return self.items.pop()#returns the last item added to the stack and removes it from the stack

     def size(self):#to find the size of the stack
         return len(self.items)#returns the length of the stack as an integer 

class Maze:#The main program to create the maze and find the solution to it
    def __init__(self,n):#initializes the maze with a nxn grid
        #Initializations for the grids/lists used later on in the code
        self.N=n#size of the grid(nxn)
        self.path=[]#empty list for the path of the solution
		#the following variables have n+2 range as it changed later to account for special edge cases where the edges will end up being 0 which implies the path cant visit it
        self.vforexp=[[0 for i in range(n+2)] for j in range(n+2)]#list for visited cells in the draw method for starting to key path initialized to 0, 0 means not visited and 1 means visited
        self.vforexp2=[[0 for i in range(n+2)] for j in range(n+2)]#list for visited cells in the draw method for key to ending path initialized to 0, 0 means not visited and 1 means visited
        self.visited=[[0 for i in range(n+2)] for j in range(n+2)]#list for visited cells while creating the maze initialized to 0, 0 means not visited and 1 means visited
        self.north=[[1 for i in range(n+2)] for j in range(n+2)]#list for making the maze and breaking north walls for every cell so a move upwards is possible from that cell
        self.south=[[1 for i in range(n+2)] for j in range(n+2)]#list for making the maze and breaking south walls for every cell so a move downwards is possible from that cell
        self.east=[[1 for i in range(n+2)] for j in range(n+2)]#list for making the maze and breaking east walls for every cell so a move right is possible from that cell
        self.west=[[1 for i in range(n+2)] for j in range(n+2)]#list for making the maze and breaking west walls for every cell so a move left is possible from that cell
        self.startx,self.starty=1,1#the starting point is placed on the top-left corner cell of the grid
        self.endx,self.endy=self.N,self.N#the ending point is placed on the bottom-right corner cell of the grid
        valid=0#variable to check if the key's location is allowed and valid on the grid
        while valid==0:#to set a random key location and check if its a valid location
             self.keyx,self.keyy=randrange(1,n+1),randrange(1,n+1)#sets the key's position to a random x and y from 1 to n+1
             if self.keyx==n and self.keyy==n:#checks if the key is at the same spot as the end point
                  valid=0#this condition is not valid as the key cannot be at the same cell as the end point
             else:
                  valid=1#if the key has any other location, the key's position is valid
        #This needs to be done so that north,south,east,west for every cell doesnt go out of range for special edge cases
        changelist(self.vforexp)#changes the edge cells for the visited cells list to 1 so the path recognizes the edges as visited and does not go off the grid to find the path
        changelist(self.vforexp2)#changes the edge cells for the visited cells list to 1 so the path recognizes the edges as visited and does not go off the grid to find the path
        changelist(self.visited)#changes the edge cells for the visited cells list to 1 when creating maze, recognizes the edges as visited and does not go off the grid to find the path

        v,n,s,e,w,startx,starty=self.visited,self.north,self.south,self.east,self.west,self.N,1#sets all the variables to the corresponding variables defined above to use in the maze creation process
        a=0#this variable is used for main loop that creates the maze to make sure that all the cells have been visited
        tracker=[]#to track every previous visited cell so that backtracking is possible
        x=startx#x is set to the x value of the starting point to start breaking walls
        y=starty#y is set to the y value of the starting point for breaking walls
        v[x][y]=1#set v[x][y] to 1 since starting point is already visited
        tracker.append((x,y))#append the starting point to the tracker list since it the first cell
        while a==0:#while all the cells have not been visited
            
            if v[x-1][y]==1 and v[x+1][y]==1 and v[x][y-1]==1 and v[x][y+1]==1:#if all the sides are blocked and there is no way to get to this cell
                x,y=previousspot(x,y,tracker)#then go back to previous cell and break more walls so that this cell can have a path to it
            else:
                count=0#variable to make sure that the next cell we go into has not been visited
                while count==0:#this is true when the cell we are trying to move into has already been visited
                    r=randrange(1,5)#randomly generate a number to move into a new cell where 1=up 2=down 3=left 4=right
                    if (r==1 and v[x-1][y]==1) or (r==2 and v[x+1][y]==1) or (r==3 and v[x][y-1]==1) or (r==4 and v[x][y+1]==1):#if the way we are trying to move has already been visited 
                        count=0#if its already visited, we try again
                    else:
                        count=1#else we move into the cell 
                if r==1:#we break the north wall from which means the south wall of the north cell is also open
                    n[x][y]=0#we set the north of the cell to open 
                    s[x-1][y]=0#we set the south of the north cell to open
                    x=x-1#set the new x to north cell's value
                    y=y#set the new y to north cell's value
                if r==2:#we break the south wall from which means the north wall of the south cell is also open
                    n[x+1][y]=0#we set the south of the cell to open
                    s[x][y]=0#we set the north of the south cell to open
                    x=x+1#set the new x to south cell's value
                    y=y#set the new y to south cell's value
                if r==3:#we break the west wall from which means the east wall of the west cell is also open
                    e[x][y-1]=0#we set the west of the cell to open
                    w[x][y]=0#we set the east of the west cell to open
                    x=x#set the new x to west cell's value
                    y=y-1#set the new y to west cell's value
                if r==4:#we break the east wall from which means the west wall of the east cell is also open
                    e[x][y]=0#we set the east of the cell to open
                    w[x][y+1]=0#we set the west of the east cell to open
                    x=x#set the new x to east cell's value
                    y=y+1#set the new y to east cell's value
                    
                    
                v[x][y]=1#set the current cell as visited
                tracker.append((x,y))#add the current cell to the tracker for backtracking
                    
            p=0#variable which helps us break out the for loop the first time we hit an univisted cell
            for i in range(len(v)):#loop through the grid to check if all the cells have been visited
                for j in range(len(v[i])):
                    if v[i][j]==1 and p==0:#if we find that all cells have been visited, as this runs till the end and the else statement never happens, we end the creating the maze
                        a=1#end the while loop to create the maze
                    else:#if we find a cell that has not been visited
                        p=1#we break out of the for loop
                        a=0#continue to create the maze
        self.visted,self.north,self.south,self.east,self.west=v,n,s,e,w# once the maze is created we set the maze values to the updated variables so we can find a path through it
        
    def draw(self):
		#Key-Green(randomized location),Start of maze-red(always bottom left),end of maze-red(always n,n which is bottom right),path-cyan/lightblue(path for explore to key/end),Start of explore-DarkBlue(for convenience)
        width=800/self.N#width of the window for nxn grid to fit perfectly
        y=-width#since x and y in the window screen is different from the way we defined it for the maze, y starts from the other side
        win=GraphWin("Maze",800,800)#size is always 800x800, the size of the cubes change as maze gets bigger
        #-------------drawing the maze-------------------
		Rectangle(Point(2,2),Point(800-1,800-1)).draw(win)#the border for the maze is drawn
        for i in range(len(self.north)):#loop through all north wall coords to draw horizontal lines accrodingly
            x=-width#since x and y in the window screen is different from the way we defined it for the maze, x starts from the other side
            
            for m in range(len(self.north[i])):#check coordinates inside north wall list to see if they are open 
                if self.north[i][m]==1:#if north wall is not open    
                    Line(Point(x,y),Point(x+width,y)).draw(win)#draw a line indicating that the north wall from that cell is closed
                x=x+width#add cell width to x so that the next line is after a certain width
            y=y+width#add cell height to x so that the next line is after a certain width
        y=-width#set y back to do the iterations for vertical lines
        
        for i in range(len(self.east)):#loop through all north wall coords to draw horizontal lines accrodingly
            x=0#sets the beginning to the left
            
            for m in range(len(self.east[i])):#check coordinates inside the east wall list to see if they are open
                if self.east[i][m]==1:#if east wall is not open
                    Line(Point(x,y),Point(x,y+width)).draw(win)#draw a line indicating that the east wall from that cell is closed
                x=x+width#add cell width to x so that the next line is after a certain height
            y=y+width#add cell height to y so that the next iteration is on the next cell line
        
        startrec=Rectangle(Point((1*width)-(width-5),(self.N*width)-(width-5)),Point((1*width)-5,(self.N*width)-5))#this creates the start rectangle at bottom left 
        startrec.setFill('red')#this colors the start rectangle to red
        startrec.draw(win)#this draws the created rectangle to the window
        endrec=Rectangle(Point((self.endy*width)-(width-5),(self.endx*width)-(width-5)),Point((self.endy*width)-5,(self.endx*width)-5))#this creates the end rectangle at the bottom right
        endrec.setFill('red')#this colors the end rectangle red
        endrec.draw(win)#this draws the created rectange to the window
        keyrec=Rectangle(Point((self.keyy*width)-(width-5),(self.keyx*width)-(width-5)),Point((self.keyy*width)-5,(self.keyx*width)-5))#this creates thekey rectange at a random location set earlier
        keyrec.setFill('green')#this colors the key rectangle green
        keyrec.draw(win)#this draws the created rectangle to the window

        
        for i in range(len(self.path)):#this loops through the path to display it with colors on the maze
             if i==0:#the starting point of the path
                  pathrec=Rectangle(Point((self.path[i][1]*width)-(width-5),(self.path[i][0]*width)-(width-5)),Point((self.path[i][1]*width)-5,(self.path[i][0]*width)-5))#creates a rectangle at the cells location
                  pathrec.setFill('blue')#this sets the color of the rectangle to blue
                  pathrec.setOutline("white")#this sets the outline of the rectangle to white
                  pathrec.draw(win)#this draws the created rectangle to the window
	
             if self.path[i]!=(self.endx,self.endy) and self.path[i]!=(self.path[0][0],self.path[0][1]):#this where the whole path is colored and shown on the maze except for starting and end point being colored
                  pathrec=Rectangle(Point((self.path[i][1]*width)-(width-5),(self.path[i][0]*width)-(width-5)),Point((self.path[i][1]*width)-5,(self.path[i][0]*width)-5))#creates a rectangle at the path's cells
                  pathrec.setFill('cyan')#the rectangle the path is shown with is colored cyan
                  pathrec.setOutline("white")#the outline of the rectangle is white
                  pathrec.draw(win)#this draws the created rectangle to the window
        
    def Explore(self,x,y):#this essentially finds the path from a starting point x,y to the key and then to the end point
         self.startx=x#sets the starting x point to the given x of the cell from where the maze is to be explored
         self.starty=y#sets the starting y point to the given y of the cell from where the maze is to be explored
#-------------------START XY TO KEY----------------         
         self.vforexp[x][y]=1#the starting cell on the visited list is marked as visited
         vforexp=self.vforexp#assigns the visited list to a temporary variable that will be used to find the path
         vforexp[x][y]=1#sets the starting cell on the visited list to visited
         a=0#used as a boolean for the while loop till a path is found to the key
         exp=MyStack()#a stack is initialized to keep track of the path we are going through
         exp.push((x,y))#push the starting coordinates on the stack as this is where we start our path
         repeat=0#variable to check if we need to push a popped point back onto the stack
         while a==0:#while we havent found a path to the key from the starting point
              if (self.north[x][y]==1 or vforexp[x-1][y]==1) and (self.south[x][y]==1 or vforexp[x+1][y]==1) and (self.west[x][y]==1 or vforexp[x][y-1]==1) and (self.east[x][y]==1 or vforexp[x][y+1]==1):#checks if all moves from a certain cell are blocked, meaning if all sides are either closed or the cells on that side have already been visited

                z=exp.pop()#if the case is true that there is no move from that cell we pop and go back to the previous cell we were on
                
                x,y=z[0],z[1]#sets the x and y values to the previous cells x and y essentially going back to the previous cell
                repeat=1#variable to push the x and y into the stack again on the next iteration 
                
              else:#if there is a move possible from the cell
                   if repeat==1:#this is where the variable gets pushed
                        exp.push((x,y))#pushes the previously popped cell back onto the stack as it is being used again
                        repeat=0#set to 0 so we dont push every cell back onto the stack
                   count=0#sets the variable to 0 to check if the randomly generated move is possible
                   while count==0:#runs until the randomly generated move is acceptable
                       r=randrange(1,5)#randoms a number from 1 to 4 where 1=move north 2=move south 3=move west and 4=move east
                       if (r==1 and (self.north[x][y]==1 or vforexp[x-1][y]==1))or (r==2 and (self.south[x][y]==1 or vforexp[x+1][y]==1)) or (r==3 and (self.west[x][y]==1 or vforexp[x][y-1]==1)) or (r==4 and (self.east[x][y]==1 or vforexp[x][y+1]==1)):#this essentially checks if all the moves are possible in every direction depending on the random number and whether the side we are trying to move to is blocked or has already been visited
                           count=0#we keep trying if this is the case
                       else:
                           count=1#if we find a valid move, we break out of the while loop
                   if r==1:#if we're moving north
                       
                       x=x-1#we set x to the north cell's value
                       y=y#we set y to the north cell's value
                   if r==2:#if we're moving south
                       
                       x=x+1#we set x to the south cell's value
                       y=y#we set y to the south cell's value
                   if r==3:#if we're moving west
                       
                       x=x#we set x to the west cell's value
                       y=y-1#we set y to the west cell's value
                   if r==4:#if we're moving east
                       
                       x=x#we set x to the east cell's value
                       y=y+1#we set y to the east cell's value
                    
                   vforexp[x][y]=1 #we set the cell as visited on the visited cell list
                   
                   exp.push((x,y)) #we push the cell we just moved into onto the stack for the path
              if x==self.keyx and y==self.keyy:#if we have reached the key
                   a=1#we break out of the loop as we have found the path
         route1=[]#this is a variable to store the path from the starting point to the key
         for i in range(exp.size()):#goes through the whole path
              route1.append(exp.pop())#pops the whole path onto the route but since we are popping it, it will be in reverse order
              
         route1.reverse() #reverse the route so its from starting point to key
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
            
            

def changelist(x):#makes borders around the initial grid to avoid special cases by making the border cells=1 for the corresponding list
    for i in range(len(x[0])):#loops through the grid and sets all the edges to 1
        x[0][i]=1#sets top edge cells to 1
        x[len(x)-1][i]=1#sets bottom edge cells to 1
        x[i][len(x)-1]=1#sets the right edge cells to 1
        x[i][0]=1#sets the left edge cells to 1

    return x#returns the list after fixing the edges

def previousspot(x,y,tracker):#To backtrack for maze which returns the previous positions x and y from the list by taking in the tracker list and the current x and y values
    newx=0#initialize x variable to return as previous x
    newy=0#initialize y variable to return as previous y
    k=1#variable to break out of for loop
    for i in range(len(tracker)):#loop through the tracker
        if x==tracker[i][0] and y==tracker[i][1] and k==1:#once we find the current x and y values we take the previous x and y points in the tracker
            k=0#to break out of loop so that we dont run into the points again
            newx=tracker[i-1][0]#previous x is set here
            newy=tracker[i-1][1]#previous y is set here
    return newx,newy#returns previous x and y values in the tracker so that it can go back to the previous cell and break more walls in that cell


 
            

    
    
    

        
        
    
