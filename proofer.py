import random
import hashlib


class Proofer:
    def __init__(self, p, g, password):
        self.p = p
        self.g = g

        self.__password = password
        self.__x = int(hashlib.md5(self.__password.encode()).hexdigest()[:8], 16) % self.p

        self.v = None
        self.t = None
        self.c = None
        self.r = None

    def register(self, verifier):
        y = pow(self.g, self.__x, self.p)
        verifier.register(y)

    def authenticate(self, verifier):
        self.v = random.randint(1, self.p)
        self.t = pow(self.g, self.v, self.p)

        self.c = verifier.challenge(self.t)

        self.r = self.v - self.c * self.__x
        result = verifier.verify(self.r)

        if result:
            print(f'{self} with password {self.__password} has proven they know the registered password')
            return True
        else:
            print(f'{self} with password {self.__password} has proven they do not know the registered password')
            return False

        return result