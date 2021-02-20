class TheWords:

    def __init__(self):
        self.words = ['IDE', 'PYTHON', 'PROJECT', 'DEVELOPER']

    def some_words(self):
        return self.words


class AccessManager(TheWords):

    def __init__(self, arg):
        super(TheWords, self).__init__()
        self.arg = arg

    def words(self, password):
        if password == 'parola123':
            return self.arg.words
        else:
            print('Wrong password.')


am = AccessManager(TheWords())
words = am.words('parola123')
