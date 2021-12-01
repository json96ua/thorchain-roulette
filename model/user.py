from thorchain import api
from model.ticket import Ticket
from model.pool import PoolItem


class User:

    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname
        self.__tickets_amount = 0
        self.__tickets = []
        self.__num_of_wins = 0

    def increase_wins(self):
        self.__num_of_wins += 1

    def get_num_of_wins(self):
        return self.__num_of_wins

    def get_amount_of_tickets(self):
        return self.__tickets_amount

    def get_tickets(self):
        return self.__tickets

    @staticmethod
    def calculate_pool_share(pool_item):
        pool_json = api.get_pool_info_by_name(pool_item.pool_name)
        user_lpu = pool_item.user_lpu
        pool_lpu = pool_json['liquidityUnits']
        return float(user_lpu) / float(pool_lpu) * 100

    def calculate_amount_of_tickets(self):
        tickets_amount = 0
        member_details = api.get_member_details(self)
        if member_details is not None:
            for pool in member_details['pools']:
                pool_name, liquidity_units = pool['pool'], pool['liquidityUnits']
                pool_item = PoolItem(pool_name, liquidity_units)
                try:
                    pool_share = self.calculate_pool_share(pool_item)
                except ValueError:
                    print(f'The pool {pool_name} cannot be found')
                    continue

                tickets_amount += int(liquidity_units) / 100000000 * pool_share

        if tickets_amount > 100:
            tickets_amount = 100
        elif tickets_amount < 1:
            tickets_amount = 1

        self.__tickets_amount = round(tickets_amount)

    def generate_tickets(self):
        for i in range(0, self.__tickets_amount):
            self.__tickets.append(Ticket(self))

    def erase_tickets(self):
        self.__tickets = []
        self.__tickets_amount = 0
