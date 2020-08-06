import numpy as np
import my_environment_2 as me 

env = me.environment(obstacle = [[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[10,18],[10,17],[10,16],[10,15],[10,14],[10,13],[10,12],[10,11],[10,10],[10,9],[10,8],[10,7],[11,7],[12,7],[13,7],[14,7],[15,7],[16,7],[17,7],[18,10],[17,10],[16,10],[15,10],[14,10],[13,13],[14,13],[15,13],[16,13],[17,13]])

qtable = np.random.uniform(low = -2,high = 0,size = list(env.dimension) + [4])

print(qtable[0])

EPISODES = 70000

#Epsilon decay
epsilon = 1
EPSILON_START = 0
EPSILON_STOP = EPISODES/2
EPSILON_DECAY = epsilon/(EPSILON_STOP - EPSILON_START) 


default = env.character.copy()

for episode in range(EPISODES):
    env.character = default.copy()
    state = env.character.copy()
    for i in range(1000):
        if np.random.rand() >epsilon:
            action = np.argmax(qtable[tuple(state)])
        else:
            action = np.random.randint(4)
        
        print(action,episode,epsilon)
        print(qtable[tuple(state)])
        env.step(action)
        if (episode%1000 == 0):
            env.render()

        #updating the qtable
        #deciding the rewards
        if(np.array_equal(env.character,env.goal)):
            reward = 1
        elif(list(env.character) in env.obstacle_list):
            reward = -20
        else:
            reward = -1

        current_q = qtable[tuple(state)][action]
        max_future_q = np.max(qtable[tuple(env.character)])
        new_q = 0.9*current_q + 0.1*(reward + 0.95*max_future_q)
        qtable[tuple(state)][action] = new_q

        if(np.array_equal(env.character,env.goal) and episode%1000 == 0):
            print("Yaha hua")
            input()

        if(list(env.character) in env.obstacle_list or np.array_equal(env.character,env.goal)):
            break
        state = env.character.copy()

    if EPSILON_STOP > episode >= EPSILON_START:
        epsilon-=EPSILON_DECAY
    if  episode%1000 == 0:
        input()
    print("-------------------")