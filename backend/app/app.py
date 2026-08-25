from flask import Flask, request, url_for
from markupsafe import escape
from services.Blackjack_player import Blackjack_game
from services.Hand import Hand

app = Flask(__name__)

@app.route("/")
def home():
    # return render_template('index.html')
    return "whats up 4head"

@app.route("/api/game", methods = ["GET"])
def get_game():
    return {"message": "This came from Flask"}
    
@app.route("/api/game", methods=["POST"])
def start_game():
    game = Blackjack_game(1000)
    game.play([100])
    game_info = {
        "dealer_hand": game.dealer.card_list[1].value,
        "player_hand": game.players[0].get_hand_values(),
        "valid_actions": game.players[0].get_valid_actions(),
    }
    return game_info

@app.route("/api/game", methods=["POST"])
def Hit():
    return {"message": "Card Hit!"}

# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"

# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('hello'))
#     print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    app.run(debug=True)