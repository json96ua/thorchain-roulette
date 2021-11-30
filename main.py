import requests

from model.lottery import Lottery
from model.user import User

if __name__ == '__main__':
    users = []
    members = requests.get('https://testnet.midgard.thorchain.info/v2/members').json()
    for member in members:
        user = User(member, member)
        user.calculate_amount_of_tickets()
        user.generate_tickets()
        users.append(user)

    for i in range(1, 11):
        print('Lottery: ' + str(i))
        lottery = Lottery(users)
        winner_player = lottery.start_lottery()
        print(f'The winner is: {winner_player.nickname}')
        print(f'Amount of tickets: {winner_player.get_amount_of_tickets()}')
        print(f'Number of wins: {winner_player.get_num_of_wins()}')
        print('--------------------------------')
        print()
