import pytest
from src.utils import BlackjackStrategy

@pytest.fixture
def strategy():
    """Creates a new instance of BlackjackStrategy."""
    return BlackjackStrategy()

def test_basic_strategy(strategy):
    """Test basic strategy decisions without card counting or betting logic."""
    
    test_cases = [
        # (dealer_card, player_total, usable_ace, expected_action)
        ('5', 16, False, 'stand'),  # Hard 16 vs 5 → hit
        ('7', 16, False, 'hit'),  # Hard 16 vs 7 → hit
        ('6', 17, False, 'stand'),  # Hard 17 vs 6 → stand
        ('A', 17, True, 'hit'),   # Soft 17 (A+6) vs A → hit

    ]
    
    for dealer_card, player_total, usable_ace, expected in test_cases:
        action = strategy.get_optimal_move(dealer_card, player_total, usable_ace)
        assert action == expected, f"Failed for player_total={player_total}, dealer_card={dealer_card}, usable_ace={usable_ace}. Expected {expected}, got {action}"
