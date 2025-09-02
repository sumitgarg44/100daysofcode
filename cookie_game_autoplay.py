"""Auto play Cookie Clicker Game"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def do_click_for_seconds(seconds=5):
    """Click on cookie for given seconds"""
    start_secs = 0

    while start_secs < seconds:
        cookie.click()
        start_secs += 0.01


def closest_price(prices, cookies):
    """Find closest product price"""
    affordable_products_price = []

    for price in prices:
        if price <= cookies:
            affordable_products_price.append(price)
    return max(affordable_products_price)


# Main Code Starts here
autoplay_run = int(input("How many times should autoplay run (a whole number): "))

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for loading of the game
time.sleep(5)

cookie = driver.find_element(By.ID, value="bigCookie")

while autoplay_run != 0:
    do_click_for_seconds(seconds=5)

    # Wait for number of clicked cookies to account for last click
    time.sleep(1)

    baked_cookies = int(
        driver.find_element(By.ID, value="cookies").text.split()[0].replace(",", "")
    )
    all_upgrades = driver.find_elements(By.CSS_SELECTOR, value="#products .price")
    products_price_list = [
        int(upgrade.text.replace(",", "")) for upgrade in all_upgrades
    ]
    price_in_budget = closest_price(prices=products_price_list, cookies=baked_cookies)
    product_index = products_price_list.index(price_in_budget)
    buy_product = all_upgrades[product_index]
    buy_product.click()

    autoplay_run -= 1

driver.quit()
