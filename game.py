import random

WORDS = ('skillfactory', 'testing', 'blackbox', 'pytest', \
        'unittest', 'coverage')

FIELD_SYMBOL = '.'

MAX_FAILURES = 4

class Game():
    def __init__(self):
        self.word = random.choice(WORDS).lower()
        self.field = [FIELD_SYMBOL for _ in self.word]
        self.tried_symbols = []
        self.is_win = False
        self.failures = 0

    def print_stat(self):
        print('')
        print('[ {} ]'.format( "".join(self.field) ))
        print(f'Privious: {self.tried_symbols}')
        print(f"Fails: {self.failures} of {MAX_FAILURES}")

    def get_symbol(self):
        symbol = None
        while not symbol:
            try:
                symbol = input("? ")[0].lower()
            except IndexError:
                pass
            if symbol in self.tried_symbols:
                print("Has been")
                symbol = None
        self.tried_symbols.append(symbol)
        return symbol

    def check(self, symbol):
        found = 0
        for i, c in enumerate(self.word):
            if c == symbol:
                found += 1
                self.field[i] = c
        if found:
            print(f"You guess ({found})")
            if not self.field.count(FIELD_SYMBOL):
                self.is_win = True
        else:
            self.failures += 1

    def round(self):
        self.print_stat()
        symbol = self.get_symbol()
        self.check(symbol)

    def run(self):
        while self.failures < MAX_FAILURES and not self.is_win:
            self.round()
        self.print_stat()
        if self.is_win:
            print('You win!!!')
        else:
            print('You lose...')


def init():
    if __name__ == '__main__':
        game = Game()
        game.run()

init()
