"""
@author: Rinku
This is the python script that is used to autobuy the product from the amazon during the flash sale
or in daily routine
"""

# This ActionChains is used for the HoverOver action
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import login_data_file

print("Checking all the requirements for running the script...")

# This is the Initial step which includes the path of the Chrome_driver and locate that to the desired website
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe', options=options)
action = ActionChains(driver)

# This get function is used to goto the desired website or URL
driver.get('http://www.amazon.in')
print("Requirements satisfied. The program has been started successfully!");print()

# This is used to copy the xpath to hover over on to sign in drop down menu
first_dropdown = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
action.move_to_element(first_dropdown).perform()

# This is used to copy the xpath to hover over on to second drop down and to click on signin
second_dropdown = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
second_dropdown.click()

print("filling email/phone...")

# This is used to get the email of the user who want to sign in
for_signin_button = driver.find_element_by_xpath('//*[@id="ap_email"]')
for_signin_button.send_keys(login_data_file.username)

print("email/phone has been successfully filled!")

# This is used to click on the continue button after typing the username/email/phone
for_continue_button = driver.find_element_by_xpath('//*[@id="continue"]')
for_continue_button.click()

print("filling password...")

# This is used to get the password of that particular email associated with that account
for_password = driver.find_element_by_xpath('//*[@id="ap_password"]')
for_password.send_keys(login_data_file.password)

print("password has been successfully filled!")

# This is to click onto the login button
for_login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
for_login.click()

# Dislaying the message which shows the user that the login was successful
print("Login successful!");print()

# This is used to for displaying the info about the URL of the user
print("opening the given URL...")

# This is used to get the data from the login file
driver.get(login_data_file.url)

# This message is for opening the desired URL of the product
print("URL opened successfully!");print()

# This count variable is user to check that the product is added to the cart if it's added it will be 1
count = 0
page_refreshed = 1
# This while loop is used to try to add the product to the cart untill the add to cart option is enabled.
while count<= 1:

    # This try statement used to add the product to the cart
    try:
        add_to_cart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
        add_to_cart.click()
        count += 2
        print("Button clicked!!! The item has been added to the cart successfully!");print()
        print("Thank you for using Amazon_AutoBuy!!!")
        print("********************** Developed by Mr.Rinku **********************");print()
    # This except statement used to reload the page every second untill the untill the add to cart option is enabled
    except:
        if count <= 1:
            print("Button not appeared, reloading...page reloaded "+str(page_refreshed)+" times!")
            driver.refresh()
            page_refreshed += 1
        pass

