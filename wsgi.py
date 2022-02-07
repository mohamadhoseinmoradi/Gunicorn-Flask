from flask import jsonify

from application import create_app

app = create_app()


@app.route("/tree", methods=["GET"])
def tree():
    return jsonify(myFavouriteTree="cypress")


if __name__ == "__main__":
    app.run()
