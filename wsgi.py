from application import create_app
from flask import jsonify


app = create_app()
@app.route("/tree", methods=["GET"])
def tree():
    return jsonify(
        myFavouriteTree="cypress"
    )


if __name__ == "__main__":
    app.run()