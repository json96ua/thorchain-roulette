from model.result import Winner, ResultContainer
from model.lottery import Lottery


class LotteryService:
    amount_of_players = 0
    players = []

    @classmethod
    def add_player_to_lottery(cls, user):
        cls.amount_of_players += 1
        cls.players.append(user)
        if cls.amount_of_players == 10:
            lottery_result = cls.__start_lottery()
            cls.__create_winner(lottery_result)
            cls.__reset_values()

    @classmethod
    def __start_lottery(cls):
        return Lottery().start_lottery(cls.players)

    @classmethod
    def __create_winner(cls, lottery_result):
        winner = Winner(lottery_result.user_id)
        ResultContainer.set_winner(winner)

    @classmethod
    def __reset_values(cls):
        cls.amount_of_players = 0
        cls.players = []
