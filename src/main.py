import gymnasium as gym
from utils import BlackjackStrategy

def play_blackjack(num_episodes=10, initial_bet=10):
    env = gym.make("Blackjack-v1", natural=True, sab=False)
    strategy = BlackjackStrategy()
    
    for episode in range(num_episodes):
        observation, info = env.reset()
        done = False
        current_bet = initial_bet
        
        while not done:
            player_total, dealer_card, usable_ace = observation
            
            # Update card count (alleen dealer's zichtbare kaart)
            strategy.count_cards(str(dealer_card) if dealer_card != 10 else "10")
            
            # Bepaal actie
            action, next_bet = strategy.get_optimal_move(
                current_bet,
                dealer_card,
                player_total,
                usable_ace
            )
            current_bet = next_bet
            
            # Vertaal naar Gymnasium's acties (0=stand, 1=hit)
            gym_action = 1 if action == "hit" else 0
            
            observation, reward, done, truncated, info = env.step(gym_action)
            
            # Update count voor getrokken kaart (als we hit deden en niet bust)
            if action == "hit" and not done and observation[0] > player_total:
                # Schat de nieuwe kaart (onzeker, maar nodig voor counting)
                new_card_value = observation[0] - player_total
                strategy.count_cards(str(new_card_value) if new_card_value != 10 else "10")
        
        print(f"Episode {episode+1}: Reward = {reward}, Final Count = {strategy.HI_LO_COUNT}")

if __name__ == "__main__":
    play_blackjack(num_episodes=100)



def test_strategy():
    strategy = BlackjackStrategy()
    
    # Test 1: Basis hit/stand beslissingen
    print("\n=== Test 1: Basis strategie ===")
    test_cases = [
        (10, "5", 16, False, "hit"),      # Hard 16 vs 5 → hit
        (10, "A", 12, True, "hit"),       # Soft 12 (A+2) vs A → hit
        (10, "6", 18, False, "stand"),    # Hard 18 vs 6 → stand
    ]
    
    for bet, dealer_card, player_total, usable_ace, expected_action in test_cases:
        action, _ = strategy.get_optimal_move(bet, dealer_card, player_total, usable_ace)
        print(f"Player {player_total} (Ace: {usable_ace}) vs Dealer {dealer_card}:")
        print(f"  Verwachte: {expected_action}, Kreeg: {action} → {'✅' if action == expected_action else '❌'}")

    # Test 2: Card counting
    print("\n=== Test 2: Card counting ===")
    strategy.HI_LO_COUNT = 0
    strategy.count_cards("5")  # +1 (low card)
    strategy.count_cards("K")  # -1 (high card)
    print(f"Na 5 en K: Count = {strategy.HI_LO_COUNT} (verwacht: 0) → {'✅' if strategy.HI_LO_COUNT == 0 else '❌'}")

def simulate_episodes(num_episodes=100):
    env = gym.make("Blackjack-v1", natural=True, sab=False)
    strategy = BlackjackStrategy()
    total_reward = 0

    for episode in range(num_episodes):
        observation, _ = env.reset()
        done = False
        
        while not done:
            player_total, dealer_card, usable_ace = observation
            action, _ = strategy.get_optimal_move(10, dealer_card, player_total, usable_ace)
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