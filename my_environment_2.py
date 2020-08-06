import numpy as np

class environment:
    def __init__(self,dimension = [20,20],character = [1,1],goal = [15,15],border = True,obstacle = []):
        self.dimension = np.array(dimension)
        self.character = np.array(character)
        self.goal = np.array(goal)
        
        obstacle_list = []
        if border:
            #the right and left borders
            for i in range(self.dimension[0]):
                obstacle_list.append([0,i])
                obstacle_list.append([self.dimension[1]-1,i])
            #the up and down
            for i in range(self.dimension[1]):
                if [i,0] not in obstacle_list:
                    obstacle_list.append([i,0])
                if [i,self.dimension[0]-1] not in obstacle_list:
                    obstacle_list.append([i,self.dimension[0] - 1])
            for i in obstacle:
                if i not in obstacle_list:
                    obstacle_list.append(i)
        self.obstacle_list = obstacle_list
        self.obstacle = np.array(obstacle_list)

    def render(self):
        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                if(np.array_equal([i,j],self.character)):
                    print('x ',end = '')
                elif(np.array_equal([i,j],self.goal)):
                    print('. ',end = '')
                elif([i,j] in self.obstacle_list):
                    print('# ',end = '')
                else:
                    print('  ',end = '')
            print()

    def step(self,action):
        if(action == 0):
            self.character[0]-=1
        elif(action == 1):
            self.character[1]-=1
        elif(action == 2):
            self.character[0]+=1
        elif(action == 3):
            self.character[1]+=1

            