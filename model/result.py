import json


class ResultContainer:
    __winner = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ResultContainer, cls).__new__(cls)
        return cls.instance

    @classmethod
    def set_winner(cls, winner):
        cls.__winner = winner

    @classmethod
    def get_winner(cls):
        return cls.__winner


class Winner:

    def __init__(self, address):
        self.address = address


class WinnerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Winner):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
