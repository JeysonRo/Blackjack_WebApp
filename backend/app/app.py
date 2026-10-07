from flask import Flask, request, session
import uuid
from markupsafe import escape
from services.Blackjack_player import Blackjack_game
from services.Hand import Hand

app = Flask(__name__)
app.secret_key = "dev-secret-key"
games = {}

def format_game_info(game: Blackjack_game):
    if len(game.players) > 0:
        game_info = {
                    "dealer_hand": ["hidden"] + game.dealer.get_hand_values()[1:],
                    "player_hands": [
                        card_list.get_hand_values() for card_list in game.players
                    ],
                    "finished_hands": [
                        card_list.get_hand_values() for card_list in game.final_hands
                    ],
                    "valid_actions": game.players[0].get_valid_actions(),
                }
    else:
        game_info = {
                    "dealer_hand": game.dealer.get_hand_values(),
                    "player_hands": [
                        card_list.get_hand_values() for card_list in game.players
                    ],
                    "finished_hands": [
                        card_list.get_hand_values() for card_list in game.final_hands
                    ],
                    "valid_actions": ["continue"],
                }
    return game_info

@app.route("/api/game", methods = ["GET"])
def get_game():
    session_id = session.get("session_id")
    if not session_id or session_id not in games:
            return {"message": "No game in progess"}, 404
        
    game = games[session_id]
    
    game_info = format_game_info(game)
    return game_info
    
@app.route("/api/game", methods=["POST"])
def start_game():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    
    session_id = session["session_id"]
    
    settings = request.get_json()["settings"]
    print("received json:")
    print(settings)
    dealer_behavior = settings["dealer_behavior"]
    
    game = Blackjack_game(bankroll=1000, dealer_behavior=dealer_behavior)
    games[session_id] = game
    
    game.play([100, 100])
    
    game_info = format_game_info(game)

    return game_info

@app.route("/api/game/action", methods=["POST"])
def Action():
    session_id = session.get("session_id")
    if not session_id or session_id not in games:
            return {"message": "No game in progess"}, 404
    
    game = games[session_id]
        
    data = request.get_json()
    action = data["action"]
    if action == "continue":
        game.play([100, 100])
    if action == "hit":   
        game.hit(game.players[0])
    if action == "stand":
        game.stand(game.players[0])
    if action == "double":
        game.double(game.players[0])
    if action == "split":
        game.split(game.players[0])
    
    game_info = format_game_info(game)

    return game_info

if __name__ == "__main__":
    app.run(debug=True)