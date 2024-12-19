import torch
import numpy as np
import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode = "human")
episode_over = False
score = 0
observation, something = env.reset()
kp1 = 0.9
kd1 = 0.9
kp2 = 0.2
kd2 = 0.1
while not episode_over:
    f = kp1 * observation[2] + kd1 * observation[3] + kp2 * observation[0] + kd2 * observation[1]
    action = 1 if f > 0 else 0
    observation, reward, truncated, terminated, info = env.step(action)
    episode_over = True if terminated or truncated else False

time.sleep(1)
env.close()
