import gymnasium as gym
import pytest
from src.utils import BlackjackStrategy

@pytest.fixture
def env():
    return gym.make('Blackjack-v1', natural=True, sab=False)

def test_full_episode(env):
    strategy = BlackjackStrategy()
    observation, _ = env.reset()
    done = False
    
    while not done:
        player_total, dealer_card, usable_ace = observation
        action, _ = strategy.get_optimal_move(10, dealer_card, player_total, usable_ace)
        
        # Convert to gym action (0=stand, 1=hit)
        gym_action = 1 if action == 'hit' else 0
        observation, reward, done, _, _ = env.step(gym_action)
    
    assert isinstance(reward, (float, int))
    env.close()