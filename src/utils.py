class BlackjackStrategy:
    def __init__(self):
        self.HI_LO_COUNT = 0

    def count_cards(self, card):
        """Update HI_LO_COUNT based on dealt card"""
        if card in ['2','3','4','5','6']:
            self.HI_LO_COUNT += 1
        elif card in ['10','J','Q','K','A']:
            self.HI_LO_COUNT -= 1

    def calculate_bet(self, current_bet):
        """Adjust bet based on count"""
        if self.HI_LO_COUNT > 2:
            return current_bet * 2
        elif self.HI_LO_COUNT < -2:
            return max(current_bet // 2, 1)
        return current_bet

    def get_optimal_move(self, current_bet, dealer_card, player_total, usable_ace=False):
        """Determine best move (hit/stand)"""
        dealer_card = str(dealer_card)
        if dealer_card in ['J','Q','K']:
            dealer_card = '10'
        
        # Basic strategy implementation
        if not usable_ace:  # Hard hand
            if player_total < 12:
                return "hit", self.calculate_bet(current_bet)
            elif player_total < 17:
                if dealer_card in ['7','8','9','10','A']:
                    return "hit", self.calculate_bet(current_bet)
                else:
                    return "stand", self.calculate_bet(current_bet)
            else:
                return "stand", self.calculate_bet(current_bet)
        else:  # Soft hand
            if player_total < 18:
                return "hit", self.calculate_bet(current_bet)
            elif player_total == 18 and dealer_card in ['9','10','A']:
                return "hit", self.calculate_bet(current_bet)
            else:
                return "stand", self.calculate_bet(current_bet)
