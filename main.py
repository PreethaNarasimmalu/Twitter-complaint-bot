# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

TWITTER_URL = "https://twitter.com/login"
TWITTER_MAIL = YOUR_EMAIL
TWITTER_PSWD = YOUR_PSWD
CHROME_DRIVER_PATH = "../Development/chromedriver.exe"
PROMISED_DOWN = 100
PROMISED_UP = 100
SPEED_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        try:
            self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        except:
            self.driver.find_element(By.XPATH, value='//*[@id="onetrust-close-btn-container"]/button').click()
            self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(45)
        down_speed = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        self.down = float(down_speed.text)
        up_speed = self.driver.find_element(By.CLASS_NAME, value="upload-speed")
        self.up = float(up_speed.text)
        print(self.down, self.up)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN :
            tweet = f"Hey @Internet Provider, why is my internet speed {self.down} down / {self.up} up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up ?"
            self.driver.get(TWITTER_URL)
            sleep(10)
            #mail = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
            mail = self.driver.find_element(By.NAME, value='text')
            mail.send_keys(TWITTER_MAIL)
            mail.send_keys(Keys.ENTER)
            sleep(10)
            pswd = self.driver.find_element(By.NAME, value='password')
            pswd.send_keys(TWITTER_PSWD)
            pswd.send_keys(Keys.ENTER)
            sleep(10)
            #tweet_compose = self.driver.find_element(By.ID, value='placeholder-67m17')
            tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_compose.send_keys(tweet)
            self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span').click()


            sleep(20)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

bot.driver.quit()
