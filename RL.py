'''
Proximal Policy Optimization RL algorithm applied to the cart-pole control theory problem.
Avi Desai

The goal is to move a cart so that it can balance a beam which is standing upright on top of it.
The cart moves along a frictionless horizontal track and is controlled by applying a force of +1 or -1.
For every time step that the pole remains upright, a reward of +1 is provided.
The episode will end if the pole moves more than 15 degrees from its upright position
or if the cart moves more than 2.5 units from the center.

https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
'''
# 1. Import dependencies
import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

# 2. Load environment
environment_name = 'CartPole-v0'
env = gym.make(environment_name)

# Loop through environment 5 times (episodes) to see how agent can can operate within it.
episodes = 5
for episode in range (1, episodes+1):

    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        # Generate random action for the cart [0,1]
        action = env.action_space.sample()
        # Apply the random cart action to the environment
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode: {} Score: {}'.format(episode, score))
env.close()

env.reset()