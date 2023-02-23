from selenium import webdriver
import time
from Library.LocalShareVariables import LSV
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By


def openBrowser():
    print("START>>openBrowser")
    global Swag
    ChromePath = LSV.ChromeDriverPath
    Swag = webdriver.Chrome(executable_path=ChromePath)
    Swag.set_window_position(-2000, 0)
    Swag.maximize_window()
    Swag.get(GSV.appURL)
    print("END>>openBrowser")
    return Swag


def closeBrowser():
    print("START>>closeBrowser")
    Swag.close()
    print("END>>closeBrowser")
    print("###TEST CASE: PASSED###")



def login (userid,pwd):
    print("START>>login")
    time.sleep(5)
    Swag.find_element(By.XPATH, "//input[@id='user-name']").send_keys(userid)
    Swag.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)
    Swag.find_element(By.XPATH, "//input[@id='login-button']").click()

def wait_for_window(swag, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = Swag.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
