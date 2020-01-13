from random import randint

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.graphics import Color, Rectangle, Ellipse

class Player():
    """
    Contains attributes of both players
    """
    def __init__(self):
        self.score = 0
        self.pits = []

class Kivayo(App):
    # On application build handler

    def build(self):
        Config.set('graphics', 'resizable', '0')
        Config.set('graphics', 'width', '740')
        Config.set('graphics', 'height', '600')
        self.layout = FloatLayout(size=(600, 600))

        # design board background
        with self.layout.canvas:
            # set background colour to brown
            Color(0.55, 0.27, 0.075)
            Rectangle(size=(740, 600), pos=(0, 0))

            Color(0, 0, 0)
            Rectangle(size=(740, 50), pos=(0, 550))  # opponent
            Rectangle(size=(740, 50), pos=(0, 0))  # player

            # set colours for players' captures
            Color(1, 1, 1)
            Ellipse(size=(200, 100), pos=(270, 450))   # opponent
            Ellipse(size=(200, 100), pos=(270, 50))   # player

            # set colours for players' pits
            for i in range(20, 640, 120):
                Ellipse(size=(100, 100), pos=(i, 190))

            for i in range(20, 640, 120):
                Ellipse(size=(100, 100), pos=(i, 310))

        # show labels for bot and player positions
        human_label = Label(text='Player A', width=740, height=50, size_hint=(None, None), pos=(0, 0))
        self.layout.add_widget(human_label)
        bot_label = Label(text='Player B', width=740, height=50, size_hint=(None, None), pos=(0, 550))
        self.layout.add_widget(bot_label)

        black = (0, 0, 0) # font colour for seeds

        # show players' scores
        self.human_captures = Label(color=(black), markup=True, text='0', font_size=80,
                                    size_hint=(None, None), width=100, height=100, pos=(320, 50))
        self.layout.add_widget(self.human_captures)

        self.bot_captures = Label(color=(black), markup=True, text='0', font_size=80,
                                  size_hint=(None, None), width=100, height=100, pos=(320, 450))
        self.layout.add_widget(self.bot_captures)

        # show player seeds
        self.btn0 = Button(size_hint=(None, None), width=50, height=50, pos=(45, 215),
                           text="4", id='0', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn0.bind(on_release=self.hole_played)
        self.layout.add_widget(self.btn0)

        self.btn1 = Button(size_hint=(None, None), width=50, height=50, pos=(165, 215),
                           text="4", id='1', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn1.bind(on_release=self.hole_played)
        self.layout.add_widget(self.btn1)

        self.btn2 = Button(size_hint=(None, None), width=50, height=50, pos=(285, 215),
                           text="4", id='2', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn2.bind(on_release=self.hole_played)
        self.layout.add_widget(self.btn2)

        self.btn3 = Button(size_hint=(None, None), width=50, height=50, pos=(405, 215),
                           text="4", id='3', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn3.bind(on_release=self.hole_played)
        self.layout.add_widget(self.btn3)

        self.btn4 = Button(size_hint=(None, None), width=50, height=50, pos=(525, 215),
                           text="4", id='4', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn4.bind(on_release=self.hole_played)
        self.layout.add_widget(self.btn4)

        self.btn5 = Button(size_hint=(None, None), width=50, height=50, pos=(645, 215),
                           text="4", id='5', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn5.bind(on_release=self.hole_played)
        self.layout.add_widget(self.btn5)

        # show AI seeds
        self.btn11 = Button(size_hint=(None, None), width=50, height=50, pos=(45, 335),
                            text="4", id='11', color=black, font_size=(80), markup=True,
                            background_normal="", background_down="")
        self.btn11.bind(on_release=self.hole_played)
        self.btn11.disabled = True  # makes AI pits unclickable
        self.btn11.background_disabled_normal = ""
        self.btn11.disabled_color = (0, 0, 0)
        self.layout.add_widget(self.btn11)

        self.btn10 = Button(size_hint=(None, None), width=50, height=50, pos=(165, 335),
                            text="4", id='10', color=black, font_size=(80), markup=True,
                            background_normal="", background_down="")
        self.btn10.bind(on_release=self.hole_played)
        self.btn10.disabled = True
        self.btn10.background_disabled_normal = ""
        self.btn10.disabled_color = (0, 0, 0)
        self.layout.add_widget(self.btn10)

        self.btn9 = Button(size_hint=(None, None), width=50, height=50, pos=(285, 335),
                           text="4", id='9', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn9.bind(on_release=self.hole_played)
        self.btn9.disabled = True
        self.btn9.background_disabled_normal = ""
        self.btn9.disabled_color = (0, 0, 0)
        self.layout.add_widget(self.btn9)

        self.btn8 = Button(size_hint=(None, None), width=50, height=50, pos=(405, 335),
                           text="4", id='8', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn8.bind(on_release=self.hole_played)
        self.btn8.disabled = True
        self.btn8.background_disabled_normal = ""
        self.btn8.disabled_color = (0, 0, 0)
        self.layout.add_widget(self.btn8)

        self.btn7 = Button(size_hint=(None, None), width=50, height=50, pos=(525, 335),
                           text="4", id='7', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn7.bind(on_release=self.hole_played)
        self.btn7.disabled = True
        self.btn7.background_disabled_normal = ""
        self.btn7.disabled_color = (0, 0, 0)
        self.layout.add_widget(self.btn7)

        self.btn6 = Button(size_hint=(None, None), width=50, height=50, pos=(645, 335),
                           text="4", id='6', color=black, font_size=(80), markup=True,
                           background_normal="", background_down="")
        self.btn6.bind(on_release=self.hole_played)
        self.btn6.disabled = True
        self.btn6.background_disabled_normal = ""
        self.btn6.disabled_color = (0, 0, 0)
        self.layout.add_widget(self.btn6)

        return self.layout

    # On application start handler
    def on_start(self):
        self.init_players()

    def hole_played(self, button):
        """
        Initiates gameplay on player's choice.
        """
        amount = int(button.text)
        playing_pit = int(button.id)

        starting_pit = playing_pit + 1
        length = len(self.board)

        if not amount:
            return

        while int(button.text) > 0:
            if self.board[starting_pit % length] == playing_pit:
                continue

            seeds = int(self.board[starting_pit % length].text)
            seeds += 1
            self.board[starting_pit % length].text = str(seeds)

            seeds = int(self.board[playing_pit].text)
            seeds -= 1
            self.board[playing_pit].text = str(seeds)

            starting_pit += 1

        starting_pit -= 1
        self.check_capture(starting_pit)    # checks if the last hole is capturable
        self.change_turn()
        self.check_winner()

    def check_capture(self, pit):
        """
        Checks if player's move results in valid capture.
        :param pit: position of hole
        """
        length = len(self.board)
        amount = self.board[pit % length].text

        if self.board[pit % length] not in self.player.pits:
            if amount == "2" or amount == "3":
                self.player.score += int(amount)

                if self.player == self.human:
                    self.human_captures.text = str(self.player.score)

                elif self.player == self.bot:
                    self.bot_captures.text = str(self.player.score)

                self.board[pit % length].text = "0"

                pit -= 1
                self.check_capture(pit)

    def change_turn(self):
        """
        Passes control to next player.
        """ 
        temp_player = self.player
        self.player = self.next_player
        self.next_player = temp_player

        self.ai_play()

    def ai_play(self):
        """
        Executes gameplay of bot.
        """
        if self.player == self.bot:
            btnnn = self.player.pits[randint(0, 5)]
            while btnnn.text == "0":
                btnnn = self.player.pits[randint(0, 5)]
            btnnn.trigger_action(1)
        pass

    def check_winner(self):
        """
        Analyzes current game state and determine winner.
        """
        count = 0
        for i in self.next_player.pits:
            count += int(i.text)

        if not count:
            if self.player == self.human:
                popup = Popup(title="Game Over", size_hint=(None, None), size=(400, 100),
                              content=Label(text="You Lose. Your opponent's pits are all empty."))

            else:
                popup = Popup(title="Game Over", size_hint=(None, None), size=(400, 100),
                              content=Label(text="You Win. Your opponent's pits are all empty."))
            popup.open()

        if self.human.score >= 25:
            popup = Popup(title="Game Over", content=Label(text="You Win"),
                          size_hint=(None, None), size=(300, 100))
            popup.open()

        elif self.bot.score >= 25:
            popup = Popup(title="Game Over", content=Label(text="You Lose"),
                          size_hint=(None, None), size=(300, 100))
            popup.open()

    def init_players(self):
        """
        Initializes players.
        """
        self.human = Player()
        self.bot = Player()

        self.board = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5,
                      self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11]

        self.human.pits = self.board[:6]
        self.bot.pits = self.board[6:]

        self.player = self.human
        self.next_player = self.bot


if __name__ == '__main__':
    Kivayo().run()
