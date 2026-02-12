import gym

if __name__ == "__main__":
    env = gym.make("CartPole-v1") # change version to v1

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, done, _, info = env.step(action) # add info since step function returns 5 values
        # reward is 1 for every step taken, including the termination step
        total_reward += reward
        total_steps += 1
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
