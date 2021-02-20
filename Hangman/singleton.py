import random
import proxy


class Singleton(object):

    __instance = None

    def __new__(cls):

        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)
            cls.word = random.choice(proxy.words)

        return cls.__instance


the_word = Singleton()
the_word_2 = Singleton()


wrd = the_word.word

print(wrd)
