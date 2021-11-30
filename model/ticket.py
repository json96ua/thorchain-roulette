import uuid


class Ticket:

    def __init__(self, user):
        self.__code = user.nickname + str(uuid.uuid4())
        self.__ticker_owner_nickname = user.nickname
        self.__code = ''
        self.__ticker_owner_nickname = ''

    def get_ticket_code(self):
        return self.__code

    def __str__(self):
        return self.__code
