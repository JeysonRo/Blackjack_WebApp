from flask import Flask, request
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def home():
    # return render_template('index.html')
    return "whats up 4head"

@app.route("/api/game", methods = ["GET"])
def get_game():
    return {
        "message": "This came from Flask"
    }

# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"

# @app.route("/user/<username>")
# def profile(username):
#     return f"you are, {escape(username)}"

# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('hello'))
#     print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    app.run(debug=True)