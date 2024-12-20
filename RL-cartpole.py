import numpy as np
import gymnasium as gym # type: ignore
import time

env = gym.make("CartPole-v1", render_mode = "human")
episode_over = False
observation, something = env.reset()
while not episode_over:
    action = env.action_space.sample()
    observation, reward, truncated, terminated, info = env.step(action)
    episode_over = True if terminated or truncated else False

time.sleep(1)
env.close()
