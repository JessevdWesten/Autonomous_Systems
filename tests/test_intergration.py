import sys
import os
import pytest
import gymnasium as gym

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.utils import BlackjackStrategy

@pytest.fixture
def env():
    """Creates a new Blackjack environment."""
    env = gym.make("Blackjack-v1", natural=True, sab=False)
    yield env
    env.close()

@pytest.fixture
def strategy():
    """Creates a new instance of BlackjackStrategy."""
    return BlackjackStrategy()

def test_integration(env, strategy):
    """Runs multiple episodes to ensure the strategy functions correctly."""
    num_episodes = 10
    total_reward = 0

    for episode in range(num_episodes):
        observation, _ = env.reset()
        done = False

        while not done:
            player_total, dealer_card, usable_ace = observation
            action = strategy.get_optimal_move(dealer_card, player_total, usable_ace)

            # Convert action to Gymnasium format (0=stand, 1=hit)
            gym_action = 1 if action == "hit" else 0
            observation, reward, done, _, _ = env.step(gym_action)

        total_reward += reward

    assert isinstance(total_reward, (int, float)), "Total reward should be a number."
    assert -num_episodes <= total_reward <= num_episodes, "Rewards should be within expected bounds."
