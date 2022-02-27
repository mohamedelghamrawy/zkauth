import random
import libnum


class Verifier:
    def __init__(self, p, g):
        self.p = p
        self.g = g

        self.__y = None
        self.t = None
        self.c = None
        self.result = None

    def register(self, y):
        """
        Proofer decides on her password, generates a hash of it,
        and then converts this to an integer value (x).

        Proofer sends Verifier the value of y = g^x (mod p) to store.
        :param y:
        :return:
        """
        self.__y = y

    def challenge(self, t):
        self.t = t
        self.c = random.randint(1, self.p)

        return self.c

    def verify(self, r):
        if r < 0:
            self.result = libnum.invmod(pow(self.g, -r, self.p), self.p) * pow(self.__y, self.c, self.p) % self.p
        else:
            self.result = (pow(self.g, r, self.p) * pow(self.__y, self.c, self.p)) % self.p

        if self.t == self.result:
            return True
        else:
            return False
