# Reinforcement Learning

Reinforcement learning: agents learn through through trial and error.
* Agents are actors operating within an environment. 
They can be ML models, people, players in video games, etc.
* Environments are the worlds in which agents operate in. 
* Actions are what the agent performs within the environment.
* Agents may receive a reward after performing an action.
* The agent observes its environment when it gets a reward and remembers it.


**Ideally, over time agents will learn what action to take in response to the environment in order to maximize reward.**


![Alt text](rl.png?raw=true "RL")

## How to do Reinforcement Learning
1. Import dependencies

### Proximal Policy Optimization
```
!pip install stable-baselines3[extra]
import os
import gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
```
2. **Load the environment**
3. **Train a RL model**
When using reinforcement learning to train robots in their movements, it often saves time and cost
to train the model in simulation first. Taking this simulation trained model and applying it to hardware
for testing can be a much more safe and efficient method. 
4. Save and reload the model
5. Evaluate the model
6. **Test the model**
7. View Logs in Tensorboard
8. **Add a callback to training stage**
9. Change policies
10. Using an alternate algorithm


Keep in mind that RL can be overkill for simple problems. Additionally,
environments must be Markovian. RL training can also take a long time and
it is not always stable.

# Links
https://stable-baselines3.readthedocs.io/en/master/
https://gym.openai.com/
