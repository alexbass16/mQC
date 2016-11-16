import random


GREETING = ["ja ne obicjav", "gitchigatchago", "...", "kypyj kotel"]
KOTEL = ('mnogo', 'troshk', 'malo')
WORDS = ('chakva','bibster', 'shubynja')


class Hlopaka:
    """ speak with some clever person """


    def __init__(self, KOTEL, WORDS, GREETING):
        self.kotel = KOTEL
        self.word = WORDS
        self.greet = GREETING 

    def hi_man(self):
        """ greeting form """
        print random.choice(self.greet)
        print "ja prodav {} kotliv".format(random.choice(self.kotel))
        print "tu {}".format(random.choice(self.word))


opo = Hlopaka(KOTEL, WORDS, GREETING)
opo.hi_man()

