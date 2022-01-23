from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/users")
def users():
    return "here is /users"

@app.route("/users/<string:user_id>")
def user(user_id):
    return f"hello user {user_id}"

@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        return "Register Form:"

if __name__ == "__main__":
    app.run()
