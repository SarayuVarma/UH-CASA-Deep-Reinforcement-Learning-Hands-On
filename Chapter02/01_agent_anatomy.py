import random


class Environment:
    def __init__(self):
        self.steps_left = 10 # agent moves 10 steps and stops

    def get_observation(self):
        return [0.0, 0.0, 0.0] # dummy env so no states to move in, just return a dummy observation

    def get_actions(self):
        return [0, 1] # left, right

    def is_done(self):
        return self.steps_left == 0

    def action(self, action):
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random() # choose a random reward for each action


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env):
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        print(reward)
        self.total_reward += reward # sum of random rewards for 10 steps


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward) 
