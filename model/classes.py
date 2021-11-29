class User:
    __assets = 0
    __num_of_wins = 0

    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname

    def increase_wins(self):
        self.__num_of_wins += 1

    def get_num_of_wins(self):
        return self.__num_of_wins

    def get_assets(self):
        return self.__assets

    def top_up_assets(self, amount):
        self.__assets += amount

    def write_off_assets(self, amount):
        self.__assets -= amount
