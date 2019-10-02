from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import time
import keyboard
from joblib import Parallel, delayed
from datetime import datetime
from tqdm import tqdm

def loadOnce(n):
    #browsers.append(webdriver.Chrome(options=options,executable_path='C:\dev\chromedriver\chromedriver.exe'))
    browsers.append(webdriver.Chrome(options=options))
    browser = browsers[len(browsers)-1]
    #print('bam')
    browser.get('http://www.kahoot.it')
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, 'game-input')))
    elem = browser.find_element_by_id('game-input') 
    elem.send_keys(game)
    #print('boom')
    butto =  browser.find_element_by_css_selector('button')
    butto.click() 
    #print('hehe')
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.invisibility_of_element((By.ID, 'waitOverlay')))
    element = wait.until(EC.visibility_of_element_located((By.ID, 'nickname')))
    elem2 = browser.find_element_by_id('nickname')
    newnam = usern + str(n)
    elem2.send_keys(newnam)
    butto2 = browser.find_element_by_css_selector('button')
    butto2.click()
    pass

def stopOnce(n):
    # for i in browsers:
    #     i.quit()

    browser = browsers[n]
    browser.quit()
    pass
if __name__ == '__main__':
    game = "423"
    usern = "banana69"
    num = 0
    
    # num = 0
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    game = input("Game number: ")
    usern = input("Username: ")
    num = input("Num: ")
    # usern = input("Username: ")
    browsers = []
    allTheBots = Parallel(n_jobs=-1,verbose=0,prefer="threads")(delayed(loadOnce)(i)for i in tqdm(range(int(num))))
    while True:
        if keyboard.is_pressed('f'):
            break
    allTheBots = Parallel(n_jobs=-1,verbose=0,prefer="threads")(delayed(stopOnce)(i)for i in tqdm(range(int(num))))
