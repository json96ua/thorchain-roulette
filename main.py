from model.user import User

if __name__ == '__main__':
    user_one = User('tthor1eu3sa69jvudksdt5qv43s8qwdrqq2ukkkjlvc4', 'jsonua')

    user_one.calculate_amount_of_tickets()
    user_one.generate_tickets()
    for ticket in user_one.get_tickets():
        print(ticket)
