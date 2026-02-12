import gym

if __name__ == "__main__":
    env = gym.make("CartPole-v1", render_mode="rgb_array") # change version to v1 and add render mode to rgb_array

    # Change Monitor to RecordVideo since Monitor was removed in latest version of gym
    env = gym.wrappers.RecordVideo(
        env,
        video_folder="recording",
        episode_trigger=lambda episode_id: True
    )

    total_reward = 0.0
    total_steps = 0
    obs, info = env.reset() # add info since reset function returns 2 values

    done = False # add this line since done is not returned by reset function anymore

    while not done: # change to while not done since done is not returned by reset function anymore

        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action) # change this line since step function returns 5 values now

        done = terminated or truncated # add this line to determine if episode is done since step function returns terminated and truncated instead of done

        total_reward += reward
        total_steps += 1

        # remove if done loop

    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
    env.close()

    # remove env.env.close()
