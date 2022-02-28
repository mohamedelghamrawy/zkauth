import random
import hashlib


class Prover:
    def __init__(self, p, g, password):
        self.p = p
        self.g = g

        self.__password = password
        self.x = int(hashlib.md5(self.__password.encode()
                                 ).hexdigest()[:8], 16) % self.p

    def register(self):
        self.y = pow(self.g, self.x, self.p)
        return self.y

    def authenticateInit(self):
        self.v = random.randint(1, self.p)
        self.t = pow(self.g, self.v, self.p)
        return self.t

    def authenticateChallenge(self, c):
        self.c = c
        self.r = self.v - self.c * self.x

        return self.r
