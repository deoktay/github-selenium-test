from githubUserinfo import userName, passWord
from selenium import webdriver
import time

class Github:
  def __init__(self, userName, passWord):
    self.browser = webdriver.Chrome()
    self.username = userName
    self.password = passWord
    self.followers = []

  def signIn(self):
    self.browser.get("https://github.com/login")
    time.sleep(2)

    self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
    self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

    time.sleep(2)

    self.browser.find_element_by_xpath("//*[@id='login']/form").submit()  
    
  def getFollowers(self):
    self.browser.get(f"https://github.com/{self.username}?tab=followers")
    time.sleep(2)

    items = self.browser.find_elements_by_css_selector(".d-table-cell.col-9.v-align-top.pr-3")
    for i in items:
      self.followers.append(i.find_element_by_css_selector(".d-inline-block.no-underline.mb-1").text)
  
  def finish(self):
    self.browser.close()

github = Github(userName, passWord)
github.signIn()

github.getFollowers()
print(github.followers)

time.sleep(3)
github.finish()


