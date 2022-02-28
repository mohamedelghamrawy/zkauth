import random

import flask
import libnum
from flask import request, jsonify

from AuthenticationEvent import AuthenticationEvent

app = flask.Flask(__name__)
app.config["DEBUG"] = False

P = 15485867
G = 2

registered_users = {}
authentication_events = {}

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/auth/parameters', methods=['GET'])
def parameters():
    params = {"P": P, "G": G}
    return jsonify(params)

@app.route('/auth/registration', methods=['POST'])
def registration():

    username = request.json["username"]
    y = request.json['y']

    if(username in registered_users.keys()):
        return ("The username is already registered", 400)
    else:
        registered_users[username] = y
        return "The username has been successfully registered"

@app.route('/auth/user/<username>/<t>', methods=['GET'])
def authentication1(username, t):
    if not (username in registered_users.keys()):
        return ("The username is not registered", 400)

    c = random.randint(1, P)
    authentication_events[username] = AuthenticationEvent(t, c)

    return jsonify(c)


@app.route('/auth/user', methods=['POST'])
def authentication2():
    username = request.json["username"]
    r = request.json["r"]

    if not (username in registered_users.keys()):
        return ("The username is not registered", 400)

    y = registered_users[username]
    c = authentication_events[username].c
    t = authentication_events[username].t

    if r < 0:
        result = (libnum.invmod(pow(G, -r, P), P) * pow(y, c, P)) % P
    else:
        result = (pow(G, r, P) * pow(y, c, P)) % P

    if (result == int(t)):
        return f"Hello {username}!"
    else:
        return ("The password is incorrect", 400)

if __name__ == '__main__':
    app.run()
