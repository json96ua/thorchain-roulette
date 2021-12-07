import random


class Lottery:

    @classmethod
    def start_lottery(cls, players):
        all_tickets = []
        map = {}
        for player in players:
            player.calculate_amount_of_tickets()
            player.generate_tickets()
            for ticket in player.get_tickets():
                map[ticket] = player
            all_tickets.extend(player.get_tickets())

        random.shuffle(all_tickets)
        random_number = random.randint(0, len(all_tickets))
        winner_ticket = all_tickets[random_number]
        winner_player = map[winner_ticket]
        winner_player.increase_wins()
        return winner_player
