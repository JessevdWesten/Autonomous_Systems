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
        dealer_card = str(dealer_card)
        if dealer_card in ['J','Q','K']:
            dealer_card = '10'
        elif dealer_card.isdigit():
            dealer_card = int(dealer_card)

        # Hard hands (no usable ace)
        if not usable_ace:
            if player_total <= 11:
                return "hit", self.calculate_bet(current_bet)
            elif player_total == 12:
                if dealer_card in [4, 5, 6]:
                    return "stand", self.calculate_bet(current_bet)
                else:
                    return "hit", self.calculate_bet(current_bet)
            elif 13 <= player_total <= 16:
                if dealer_card in ['2','3','4','5','6']:
                    return "stand", self.calculate_bet(current_bet)
                else:
                    return "hit", self.calculate_bet(current_bet)
            else:  # 17+
                return "stand", self.calculate_bet(current_bet)
        
        # Soft hands (usable ace)
        else:
            if player_total <= 17:
                return "hit", self.calculate_bet(current_bet)
            elif player_total == 18:
                if dealer_card in ['9','10','A']:
                    return "hit", self.calculate_bet(current_bet)
                else:
                    return "stand", self.calculate_bet(current_bet)
            else:  # 19+
                return "stand", self.calculate_bet(current_bet)