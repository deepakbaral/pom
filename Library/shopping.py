import time
from selenium.webdriver.common.by import By
import Library.GlobalShareVariables as GSV

def product(Swag):
    Swag.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(2)
    Swag.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    time.sleep(2)
    print('item added to cart')

    # Now add to Cart (By using css selector)
    Swag.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
    Swag.find_element(By.ID, 'checkout').click()

    Swag.find_element(By.CSS_SELECTOR, '#first-name').send_keys(GSV.first_name)
    time.sleep(3)
    Swag.find_element(By.CSS_SELECTOR, '#last-name').send_keys(GSV.Last_name)
    time.sleep(2)
    Swag.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(GSV.zip_Code)

    Swag.find_element(By.CSS_SELECTOR, '#continue').click()
    time.sleep(3)
    Swag.find_element(By.ID, 'finish').click()
    print('Progress completed')
