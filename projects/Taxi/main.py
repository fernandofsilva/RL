from agent import Agent
from monitor import interact
import gym


if __name__ == '__main__':

    # Create environment
    env = gym.make('Taxi-v3')

    # Instantiate agent
    agent = Agent()

    # Interact with environment
    avg_rewards, best_avg_reward = interact(env, agent)
