import json

from flask import Flask, request

from model.result import ResultContainer, WinnerEncoder
from model.user import User, UserEncoder
from service.lottery_service import LotteryService

app = Flask(__name__)


@app.route('/result', methods=['GET'])
def get_result():
    return json.dumps(ResultContainer.get_winner(), cls=WinnerEncoder)


@app.route('/add/player', methods=['POST'])
def add_player():
    request_data = request.get_json(force=True)
    address = request_data['address']
    nickname = request_data['nickname']

    user = User(address, nickname)

    LotteryService().add_player_to_lottery(user)
    return str(LotteryService().amount_of_players)


@app.route('/get/players')
def get_players():
    lottery_service = LotteryService()
    return json.dumps(lottery_service.players, cls=UserEncoder)


if __name__ == '__main__':
    app.run(debug=True)
