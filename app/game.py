import time
from selenium.webdriver import Firefox
from mapping import Buttons, Inputs, Houses


class Game:
    def __init__(self) -> None:
        self.browser = Firefox()
        self.browser.get('https://richup.io/')
        self.browser.maximize_window()
        self.button = Buttons(self.browser)
        self.input = Inputs(self.browser)
        self.house = Houses(self.browser)
        time.sleep(2)
        self.button.accept_cookies.click()


    def join_game(self, name):
        self.input.name.send_keys(name)
        self.button.play.click()
        time.sleep(2)
        self.button.join_game.click()

    def list_house_information(self,house_name):
        house = self.house.__getattribute__(house_name)
        house.click()

    def roll_dice(self):
        # verificar se o botão de rolar os dados está habilitado
        self.button.roll_dice.click()

    def end_turn(self):
        self.button.end_turn.click()

    def buy(self):
        self.button.buy.click()

    def close(self):
        self.browser.close()