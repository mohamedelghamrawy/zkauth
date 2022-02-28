import requests

from prover import Prover

if __name__ == '__main__':
    # specify shared parameters
    params = requests.get("http://127.0.0.1:5000/auth/parameters")
    p = params.json()["P"]
    g = params.json()["G"]

    username = "mo"
    password = "hello"
    fake_password = "fake"

    # create and register fake prover
    fake_prover = Prover(p, g, fake_password)

    # create and register true prover
    prover = Prover(p, g, password)
    mydata = {"username": "mo", "y": prover.register()}
    reg = requests.post("http://127.0.0.1:5000/auth/registration", json=mydata)
    print(reg.text)

    # authenticate true prover
    t = prover.authenticateInit()
    auth1 = requests.get(
        f"http://127.0.0.1:5000/auth/user/mo/{t}")
    r = prover.authenticateChallenge(int(auth1.text))
    auth2 = requests.post("http://127.0.0.1:5000/auth/user",
                          json={"username": "mo", "r": r})
    print(f"Server Response: {auth2.text}")

    # authenticate true prover
    auth1 = requests.get(
        f"http://127.0.0.1:5000/auth/user/mo/{fake_prover.authenticateInit()}")
    r = fake_prover.authenticateChallenge(int(auth1.text))
    auth2 = requests.post("http://127.0.0.1:5000/auth/user",
                          json={"username": "mo", "r": r})
    print(f"Server Response: {auth2.text}")
