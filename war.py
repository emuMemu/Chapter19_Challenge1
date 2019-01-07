from random import shuffle

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,
              "2", "3", "4",
              "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, value, suit):
        """スートも数値も整数値"""
        self.v = value
        self.s = suit

    def __lt__(self, c2):
        if self.v < c2.v:
            return True
        if self.v == c2.v:
            if self.s < c2.s:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.v > c2.v:
            return True
        if self.v == c2.v:
            if self.s > c2.s:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.v] +\
        " of " +\
        self.suits[self.s]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.n = name

class Game:
    def __init__(self):
        name1 = input("プレイヤー1の名前 ")
        name2 = input("プレイヤー2の名前 ")
        self.d = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは {} が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} は {}、{} は {} を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.d.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでplay : "
            response = input(m)
            if response == 'q':
                break
            p1c = self.d.rm_card()
            p2c = self.d.rm_card()
            p1n = self.p1.n
            p2n = self.p2.n
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.n)
            else:
                self.p2.wins += 1
                self.wins(self.p2.n)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{} の勝利です！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.n
        if p1.wins < p2.wins:
            return p2.n
        return "引き分け！"

game = Game()
game.play_game()
