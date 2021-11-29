from thorchain import api
from model.ticket import Ticket


class User:
    __tickets_amount = 0
    __tickets = []
    __num_of_wins = 0

    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname

    def increase_wins(self):
        self.__num_of_wins += 1

    def get_num_of_wins(self):
        return self.__num_of_wins

    def get_amount_of_tickets(self):
        return self.__tickets_amount

    def get_tickets(self):
        return self.__tickets

    def calculate_amount_of_tickets(self):
        member_details = api.get_member_details(self)
        if member_details is not None:
            tickets_amount = 0
            for pool in member_details['pools']:
                liquidity_units = pool['liquidityUnits']
                tickets_amount += float(liquidity_units) * 0.00000001
            self.__tickets_amount = round(tickets_amount)

    def generate_tickets(self):
        for i in range(0, self.__tickets_amount):
            self.__tickets.append(Ticket(self))

    def erase_tickets(self):
        self.__tickets = []
        self.__tickets_amount = 0
