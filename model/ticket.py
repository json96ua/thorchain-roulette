import uuid


class Ticket:
    __code = ''
    __ticker_owner_nickname = ''

    def __init__(self, user):
        self.__code = user.nickname + str(uuid.uuid4())
        self.__ticker_owner_nickname = user.nickname

    def get_ticket_code(self):
        return self.__code

    def __str__(self):
        return self.__code
