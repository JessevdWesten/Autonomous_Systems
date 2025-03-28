import gymnasium as gym
from utils import BlackjackStrategy

def play_blackjack(num_episodes=10):
    env = gym.make("Blackjack-v1", natural=True, sab=False)
    strategy = BlackjackStrategy()
    
    for episode in range(num_episodes):
        observation, info = env.reset()
        done = False
        
        while not done:
            player_total, dealer_card, usable_ace = observation
            
            # Bepaal actie
            action = strategy.get_optimal_move(dealer_card, player_total, usable_ace)
            
            # Vertaal naar Gymnasium's acties (0=stand, 1=hit)
            gym_action = 1 if action == "hit" else 0
            
            observation, reward, done, truncated, info = env.step(gym_action)
        
        print(f"Episode {episode+1}: Reward = {reward}")

if __name__ == "__main__":
    play_blackjack(num_episodes=100)


def test_strategy():
    strategy = BlackjackStrategy()
    
    # Test 1: Basis hit/stand beslissingen
    print("\n=== Test 1: Basis strategie ===")
    test_cases = [
        ("5", 16, False, "hit"),      # Hard 16 vs 5 → hit
        ("A", 12, True, "hit"),       # Soft 12 (A+2) vs A → hit
        ("6", 18, False, "stand"),    # Hard 18 vs 6 → stand
    ]
    
    for dealer_card, player_total, usable_ace, expected_action in test_cases:
        action = strategy.get_optimal_move(dealer_card, player_total, usable_ace)
        print(f"Player {player_total} (Ace: {usable_ace}) vs Dealer {dealer_card}:")
        print(f"  Verwachte: {expected_action}, Kreeg: {action} → {'✅' if action == expected_action else '❌'}")

def simulate_episodes(num_episodes=100):
    env = gym.make("Blackjack-v1", natural=True, sab=False)
    strategy = BlackjackStrategy()
    total_reward = 0

    for episode in range(num_episodes):
        observation, _ = env.reset()
        done = False
        
        while not done:
            player_total, dealer_card, usable_ace = observation
            action = strategy.get_optimal_move(dealer_card, player_total, usable_ace)
            gym_action = 1 if action == "hit" else 0
            observation, reward, done, _, _ = env.step(gym_action)
        
        total_reward += reward
        if (episode + 1) % 10 == 0:
            print(f"Episode {episode + 1}: Reward = {reward}, Running Total = {total_reward}")

    print(f"\nGemiddelde reward per episode: {total_reward / num_episodes:.2f}")
    env.close()

if __name__ == "__main__":
    test_strategy()       # Unit tests
    simulate_episodes(100)  # Simulatie met Gymnasium
