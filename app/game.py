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
        # aceitar cookies

    def join_game(self, name):
        self.input.name.send_keys(name)
        self.button.play.click()
        time.sleep(2)
        self.button.join_game.click()

    def list_house_information(self,house_name):
        house = self.house.__getattribute__(house_name)
        house.click()
        # time.sleep(10)
        # fechar a janela de informação da casa