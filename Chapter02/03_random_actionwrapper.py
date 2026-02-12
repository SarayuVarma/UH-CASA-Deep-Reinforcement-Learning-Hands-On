import gym
import random

# wrapper used to modify environment behavior without touching original environment code
class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.8):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self, action): # change the action taken by the agent with some probability
        if random.random() < self.epsilon: # with epsilon probability, take a random action instead of the one given by the agent
            print("Random!")
            return self.env.action_space.sample()
        return action


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1")) # change version to v1

    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, done, _, info = env.step(0) # add info since step function returns 5 values
        total_reward += reward
        if done:
            break

    print("Reward got: %.2f" % total_reward)
