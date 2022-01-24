#from flask import Flask, jsonify
from application import create_app

app = create_app()
app.run()

#myapp = Flask(__name__)
#@myapp.route("/tree", methods=["GET"])
#def tree():
#    return jsonify(
#        myFavouriteTree="cypress"
#    )


#if __name__ == "__main__":
#    myapp.run()