import sys

from proofer import Proofer
from verifier import Verifier


def pickg(p):
    for x in range(1, p):
        rand = x
        exp = 1
        next = rand % p

        while (next != 1):
            next = (next * rand) % p
            exp = exp + 1

        if (exp == p - 1):
            return rand


if __name__ == '__main__':
    # specify shared parameters
    p = 997
    g = pickg(p)
    # password = str(sys.argv[1])
    password = "hello"
    fake_password = "fake hello"

    verifier = Verifier(p, g)

    # create and register true proofer
    proofer = Proofer(p, g, password)
    proofer.register(verifier)

    # Real Proofer attempts verification
    proofer.authenticate(verifier)

    # Create fake proofer and atttempt verification
    fake_proofer = Proofer(p,g, fake_password)
    fake_proofer.authenticate(verifier)
