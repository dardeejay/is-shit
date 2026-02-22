from collections import deque

class Agent:
    def __init__(self, environment, start):
        self.environment = environment
        self.state = start
    def perceive(self):
        return self.environment.get_actions(self.state)
    def act(self, action):
        self.state = self.environment.transition(self.state, action)

    def goal_test(self):
        return self.environment.is_goal(self.state)

class Environment:
    def __init__(self, graph, goal):
        self.graph = graph
        self.goal = goal

    def get_actions(self, state):
        return self.graph.get(state, [])
    
    def transition(self, state, action):
        
        if action not in self.graph.get(state, []):
            print("Invalid action. Staying in the same state.")
            return state

        if self.graph.get(action, []) == [] and action != self.goal:
            print("Blocked cell. Staying in the same state.")
            return state

        return action

    def is_goal(self, state):
        return state == self.goal

graph = {
    (0,0): [(0,1), (1,0)],
    (0,1): [],
    (0,2): [(0,1), (1,2)],
    (1,0): [(0,0), (2,0)],
    (1,2): [(0,2), (2,2)],
    (2,0): [(1,0), (2,1)],
    (2,1): [(2,0), (2,2)],
    (2,2): []  # Goal
}

env = Environment(graph, (2,2))
agent = Agent(env, (0,0))
print("Starting at:", agent.state)

while not agent.goal_test():
    actions = agent.perceive()
    print("Available actions:", actions)
    choice = eval(input("Choose next state: "))
    agent.act(choice)
    print("Current state:", agent.state)


print("Goal reached!")

# for neighbor in env.get_actions(agent.state):
#     print("Neighbor:", neighbor)

# def dfs(environment, start):
#     stack = [start]
#     visited = set()

#     while stack:
#         state = stack.pop()

#         if state in visited:
#             continue

#         print("Visiting:", state)
#         visited.add(state)

#         if environment.is_goal(state):
#             print("Goal found!")
#             return True

#         for neighbor in environment.get_actions(state):
#             if neighbor not in visited:
#                 stack.append(neighbor)

#     return False


# def bfs(environment, start): 
#     queue = [start]
#     visited = set()

#     while queue: 
#         state = queue.pop(0)

#         if state in visited:
#             continue
            
#         print("Visiting:", state)
#         visited.add(state)

#         if environment.is_goal(state):
#             print("Goal found!")
#             return True
        
#         for neighbor in environment.get_actions(state):
#             if neighbor not in visited:
#                 queue.append(neighbor)

#     return False




# bfs(env, (0,0))

