import random


class Lottery:
    players = []

    def __init__(self, players):
        self.players = players

    def start_lottery(self):
        all_tickets = []
        map = {}
        for player in self.players:
            for ticket in player.get_tickets():
                map[ticket] = player
            all_tickets.extend(player.get_tickets())

        random.shuffle(all_tickets)
        random_number = random.randint(0, len(all_tickets))
        winner_ticket = all_tickets[random_number]
        winner_player = map[winner_ticket]
        winner_player.increase_wins()
        return winner_player
