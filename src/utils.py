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

# Deze klopt niet en moet veranderd worden, de resultaten moeten overeen komen met de tests het kan ook zijn dat de uitkomst van de test niet klopt.

    # def get_optimal_move(self, current_bet, dealer_card, player_total, usable_ace=False):
    #     dealer_card = str(dealer_card)
    #     if dealer_card in ['J','Q','K']:
    #         dealer_card = '10'
        
    #     # Hard hands (no usable ace)
    #     if not usable_ace:
    #         if player_total <= 11:
    #             return "hit", self.calculate_bet(current_bet)
    #         elif 12 <= player_total <= 16:
    #             # ALTIJD hit bij 13-16 tegen dealer 2-6 (behalve specifieke uitzonderingen)
    #             if dealer_card in ['2','3','4','5','6']:
    #                 if player_total == 12 and dealer_card in ['4','5','6']:
    #                     return "stand", self.calculate_bet(current_bet)
    #                 return "hit", self.calculate_bet(current_bet)  # <- Dit is de cruciale wijziging
    #             else:
    #                 return "hit", self.calculate_bet(current_bet)
    #         else:  # 17+
    #             return "stand", self.calculate_bet(current_bet)
        
    #     # Soft hands (usable ace) blijft ongewijzigd
    #     else:
    #         if player_total <= 17:
    #             return "hit", self.calculate_bet(current_bet)
    #         elif player_total == 18:
    #             if dealer_card in ['9','10','A']:
    #                 return "hit", self.calculate_bet(current_bet)
    #             else:
    #                 return "stand", self.calculate_bet(current_bet)
    #         else:
    #             return "stand", self.calculate_bet(current_bet)