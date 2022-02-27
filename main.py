import sys

from prover import Prover
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
    prover = Prover(p, g, password)
    prover.register(verifier)

    # Real prover attempts verification
    prover.authenticate(verifier)

    # Create fake prover and attempt verification
    fake_prover = Prover(p, g, fake_password)
    fake_prover.authenticate(verifier)
