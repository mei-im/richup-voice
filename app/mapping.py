from selenium.webdriver.common.by import By

class MapObject:
    
    def __init__(self,browser) -> None:
        self.browser = browser
    
    def find_element(self, xpath):
        return self.browser.find_element(By.XPATH, xpath)


class Buttons(MapObject):

    @property
    def play(self):
        return self.find_element('/html/body/div/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/button')

    @property
    def join_game(self):
        return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/button')

    @property
    def join_game_after_color(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/button')
    
    @property
    def start_game(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button')
    
    @property
    def roll_dice(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button')
    
    @property
    def end_turn(self):
        try:  
            return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button')
        except Exception:
            return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/button')         

    @property
    def enable_bots(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[3]/div/div[3]/div[2]/div[1]/div[3]/div[3]/span/button')
    
    @property
    def accept_cookies(self):
        try:
            return self.find_element('/html/body/div[1]/div/div/div/div[2]/div/button[2]')
        except Exception:
            return self.find_element('/html/body/div[1]/div[1]/div[2]/span[1]/a')
        
    @property
    def buy(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/button')

    @property
    def create_private_game(self):
        return self.find_element('/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/button[2]')
    
    @property
    def randomize_name(self):
        return self.find_element('/html/body/div/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div')
    
    @property
    def bankrupt(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[3]/div/div[2]/div/button')

    @property
    def confirm_bankrupt(self):
        return self.find_element('/html/body/div[6]/div/div/div/button[1]')
    
    @property
    def cancel_bankrupt(self):
        return self.find_element('/html/body/div[6]/div/div/div/button[2]')
    
    @property
    def prison_pay(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/button')

    @property
    def mute(self):
        return self.find_element("/html/body/div[2]/div[4]/div/div[1]/div[1]/div/button[2]")

    @property
    def unmute(self):
        return self.find_element("/html/body/div[2]/div[4]/div/div[1]/div[1]/div/button[2]")   
    
class Inputs(MapObject):
    @property
    def name(self):
        return self.find_element('/html/body/div/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/input')

class Houses(MapObject):

    @property
    def salvador(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[1]/div[3]/div[1]')
    
    @property
    def rio(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[3]/div[3]/div[1]')
    
    @property
    def tlv_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[5]/div[3]/div[1]')
    
    @property
    def tel_aviv(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[6]/div[3]/div[1]')
    
    @property
    def haifa(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[8]/div[3]/div[1]')
    
    @property
    def jerusalem(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[9]/div[3]/div[1]')
    
    @property
    def venice(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[1]/div[3]/div[1]')
    
    @property
    def electric_company(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[2]/div[3]/div[1]')

    @property
    def milan(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[3]/div[3]/div[1]')
    
    @property
    def rome(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[4]/div[3]/div[1]')
    
    @property
    def muc_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[5]/div[3]/div[1]')
    
    @property
    def frankfurt(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[6]/div[3]/div[1]')
    
    @property
    def munich(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[8]/div[3]/div[1]')
    
    @property
    def berlin(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[9]/div[3]/div[1]')
    
    @property
    def shenzhen(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[1]/div[3]/div[1]')
    
    @property
    def beijing(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[3]/div[3]/div[1]')
    
    @property
    def shanghai(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[4]/div[3]/div[1]')
    
    @property
    def cdg_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[5]/div[3]/div[1]')
    
    @property
    def lyon(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[6]/div[3]/div[1]')
    
    @property
    def toulouse(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[7]/div[3]/div[1]')
    
    @property
    def water_company(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[8]/div[3]/div[1]')
    
    @property
    def paris(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[9]/div[3]/div[1]')
    
    @property
    def liverpool(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[1]/div[3]/div[1]')
    
    @property
    def manchester(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[2]/div[3]/div[1]')
    
    @property
    def london(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[4]/div[3]/div[1]')
    
    @property
    def jfk_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[5]/div[3]/div[1]')
    
    @property
    def san_francisco(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[7]/div[3]/div[1]')
    
    @property
    def new_york(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[9]/div[3]/div[1]')

class Colors(MapObject):
    # TODO MUDAR CORES PARTE 2
    # /html/body/div[2]/div[4]/div/div[3]/div/div[1]/div/div/div/div[2]/button
    # /html/body/div[7]/div/div[1]/div/div/div[1]/div/button[1]
    # /html/body/div[7]/div/div[1]/div/div/div[1]/div/button[12]

    @property
    def lime(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[1]')
    
    @property
    def yellow(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[2]')
    
    @property
    def orange(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[3]')
    
    @property
    def red(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[4]')
    
    @property
    def blue(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[5]')
    
    @property
    def cyan(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[6]')
    
    @property
    def water(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[7]')
    
    @property
    def green(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[8]')
    
    @property
    def brown(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[9]')
    
    @property
    def hotpink(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[10]')
    
    @property
    def pink(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[11]')
    
    @property
    def purple(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/button[12]')