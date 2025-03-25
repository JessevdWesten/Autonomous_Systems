import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.utils import BlackjackStrategy
import pytest

class TestBlackjackStrategy:
    @pytest.fixture
    def strategy(self):
        return BlackjackStrategy()

    def test_card_counting(self, strategy):
        strategy.count_cards('5')
        strategy.count_cards('K')
        assert strategy.HI_LO_COUNT == 0

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
            action, _ = strategy.get_optimal_move(10, dealer_card, player_total, usable_ace)
            assert action == expected

    def test_bet_calculation(self, strategy):
        strategy.HI_LO_COUNT = 3
        assert strategy.calculate_bet(10) == 20
        
        strategy.HI_LO_COUNT = -3
        assert strategy.calculate_bet(10) == 5