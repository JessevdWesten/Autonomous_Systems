import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.utils import BlackjackStrategy

class TestBlackjackStrategy:
    @pytest.fixture
    def strategy(self):
        return BlackjackStrategy()

    def test_basic_strategy(self, strategy):
        test_cases = [
            # (dealer_card, player_total, usable_ace, expected_action)
            ('5', 16, False, 'hit'),
            ('7', 16, False, 'hit'), 
            ('6', 17, False, 'stand'),
            ('A', 17, True, 'hit'),
            ('10', 18, True, 'stand')
        ]
        
        for dealer_card, player_total, usable_ace, expected in test_cases:
            action = strategy.get_optimal_move(dealer_card, player_total, usable_ace)
            assert action == expected
