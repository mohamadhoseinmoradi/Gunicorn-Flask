from flask import Flask, jsonify


myapp = Flask(__name__)
@myapp.route("/tree", methods=["GET"])
def tree():
    return jsonify(
        myFavouriteTree="cypress"
    )


if __name__ == "__main__":
    myapp.run()