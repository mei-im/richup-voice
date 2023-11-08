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
    def start_game(self):
        return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/button')
    
    @property
    def roll_dice(self):
        return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button')
    
    @property
    def end_turn(self):
        try:  
            return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/button')
        except Exception:
            return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/button')         


    @property
    def buy(self):
        return self.find_element('/html/body/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/button')

    @property
    def create_private_game(self):
        return self.find_element('/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/button[2]')

class Inputs(MapObject):
        @property
        def name(self):
            return self.find_element('/html/body/div/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/input')



class Houses(MapObject):

    @property
    def salvador(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[1]')
    
    @property
    def rio(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[3]')
    
    @property
    def tlv_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[5]')
    
    @property
    def tel_aviv(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[6]')
    
    @property
    def haifa(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[8]')
    
    @property
    def jerusalem(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[9]')
    
    @property
    def venice(self):
        return self.find_element('/html/body/div[3]/div[4]/div/div[2]/div/div/div[5]/div[1]')
    
    @property
    def electric_company(self):
        return self.find_element('/html/body/div[3]/div[4]/div/div[2]/div/div/div[5]/div[2]')

    @property
    def milan(self):
        return self.find_element('/html/body/div[3]/div[4]/div/div[2]/div/div/div[5]/div[3]')
    
    @property
    def rome(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[4]')
    
    @property
    def muc_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[5]')
    
    @property
    def frankfurt(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[6]')
    
    @property
    def munich(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[8]')
    
    @property
    def berlin(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[5]/div[9]')
    
    @property
    def shenzhen(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[1]')
    
    @property
    def beijing(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[3]')
    
    @property
    def shanghai(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[4]')
    
    @property
    def cdg_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[5]')
    
    @property
    def lyon(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[6]')
    
    @property
    def toulouse(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[7]')
    
    @property
    def water_company(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[8]')
    
    @property
    def paris(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[7]/div[9]')
    
    @property
    def liverpool(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[1]')
    
    @property
    def manchester(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[2]')
    
    @property
    def london(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[4]')
    
    @property
    def jfk_airport(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[5]')
    
    @property
    def san_francisco(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[7]')
    
    @property
    def new_york(self):
        return self.find_element('/html/body/div[2]/div[4]/div/div[2]/div/div/div[9]/div[9]')
