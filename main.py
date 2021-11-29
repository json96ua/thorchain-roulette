from model.classes import User

if __name__ == '__main__':
    user_one = User(1, 'jsonua')
    print(user_one.get_assets())
    user_one.top_up_assets(100)
    print(user_one.get_assets())

    user_two = User(2, 'random')
    user_two.increase_wins()
    print(user_two.get_num_of_wins())
