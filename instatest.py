from selenium import webdriver
from time import sleep

class Instabot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        #Enters username
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input[@name=\"username\"]")\
            .send_keys(username)

        #Enters password
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input[@name=\"password\"]")\
            .send_keys(pw)

        #Clicks login button
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button[@type="submit"]')\
            .click()
        sleep(2)

        #Clicks out of first tab
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

        #Clicks out of second tab
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2][contains(text(), 'Not Now')]")\
            .click()
        sleep(1)

    def find(self, tag):
        
        #Redirects to given tag and selects the first picture
        self.driver.get("https://instagram.com/explore/tags/" + tag + "/")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div")\
            .click()

        #Likes the picture displayed
    def like_pic(self):
        driver = self.driver
        driver.find_element_by_xpath("//button[@class='wpO6b ']").click()

        #Clicks the next arrow
    def next(self):
        self.driver.find_element_by_xpath("//a[@class=' _65Bje  coreSpriteRightPaginationArrow']").click()

#Enter a tag
while True:
    try:
        tag_given = str(input('Enter a tag you want to start with.'))
        break
    except TypeError:
        print('Please type a tag without numbers')
        continue

#Start the bot
mybot = Instabot('inu.blu', 'Babystar11!!')
count = 1
mybot.find(tag_given)
sleep(3)

#Like pictures to a given number
while count <= 70:
    mybot.like_pic()
    sleep(1)
    mybot.next()
    sleep(2)
    count += 1

        

