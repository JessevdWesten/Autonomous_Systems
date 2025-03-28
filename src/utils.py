class BlackjackStrategy:
    def __init__(self):
        self.HI_LO_COUNT = 0

    def count_cards(self, card):
        """Update HI_LO_COUNT based on dealt card.
        We wanted to experiment with how the strategy would diverge if only one deck was used, there is much information about it
        However for now we wont use it
        Hi-Lo counting system:
        - Low cards (2-6) increase the count (+1), meaning more high cards remain.
        - High cards (10, J, Q, K, A) decrease the count (-1), meaning fewer high cards remain.
        - Neutral cards (7-9) do not affect the count.
        
        In a simulation without card counting, this method can be ignored.
        """
        if card in ['2', '3', '4', '5', '6']:
            self.HI_LO_COUNT += 1
        elif card in ['10', 'J', 'Q', 'K', 'A']:
            self.HI_LO_COUNT -= 1

    def calculate_bet(self, current_bet):
        """Adjust bet size based on the Hi-Lo count.
        Like count cards, we can try adjusting betting size based on the count, but we wont use it for now
        - If the count is significantly positive (>2), increase the bet (good odds).
        - If the count is significantly negative (<-2), decrease the bet (bad odds).
        - Otherwise, keep the bet the same.
        
        In a simulation without betting, this function can be ignored.
        """
        if self.HI_LO_COUNT > 2:
            return current_bet * 2
        elif self.HI_LO_COUNT < -2:
            return max(current_bet // 2, 1)
        return current_bet

    def get_optimal_move(self, dealer_card, player_total, usable_ace=False):
        dealer_card = str(dealer_card)
        if dealer_card in ['J', 'Q', 'K']:
            dealer_card = '10'
        elif dealer_card.isdigit():
            dealer_card = int(dealer_card)

        # Hard hands (no usable ace)
        if not usable_ace:
            if player_total <= 11:
                return "hit"
            elif player_total == 12:
                if dealer_card in [4, 5, 6]:
                    return "stand"
                else:
                    return "hit"
            elif 13 <= player_total <= 16:
                if dealer_card in [2, 3, 4, 5, 6]:
                    return "stand"
                else:
                    return "hit"
            else:  # 17+
                return "stand"

        # Soft hands (usable ace)
        else:
            if player_total <= 17:
                return "hit"
            elif player_total == 18:
                if dealer_card in [9, 10, 'A']:
                    return "hit"
                else:
                    return "stand"
            else:  # 19+
                return "stand"