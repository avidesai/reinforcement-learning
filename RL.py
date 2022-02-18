'''
Proximal Policy Optimization RL algorithm applied to the cart-pole control theory problem.
Avi Desai

The goal is to move a cart so that it can balance a beam which is standing upright on top of it.
The cart moves along a frictionless horizontal track and is controlled by applying a force of +1 or -1.
For every time step that the pole remains upright, a reward of +1 is provided.
The episode will end if the pole moves more than 15 degrees from its upright position
or if the cart moves more than 2.5 units from the center.

'''
import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy


