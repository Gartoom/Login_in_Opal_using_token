#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get('https://bildungsportal.sachsen.de/opal/login')
token_dict = {
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "",
    "14": "",
    "15": "",
    "16": "",
    "17": "",
    "18": "",
    "19": "",
    "20": "",
    "21": "",
    "22": "",
    "23": "",
    "24": "",
    "25": ""
}
try:
    # Wait for the dropdown to appear and select "TU Dresden"
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'select'))
    )
    select = Select(select_element)
    select.select_by_visible_text('TU Dresden')

    # Wait for the "Login" button to become clickable and click on it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'id12'))  # Use the "Login" button ID
    )
    login_button.click()
    # Wait until the username and password can be entered
    username_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'username'))  # Replace 'username_field_id' with the real input field ID
    )
    username_input.send_keys('your_username')  # Replace 'your_username' with your username

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))  # Replace 'password_field_id' with the real input field ID
    )
    password_input.send_keys('your_password')  # Replace 'your_password' with your password

    # Search for and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, '_eventId_proceed'))  # Replace 'submit' with the actual button name
    )
    login_button.click()


    text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'legend'))
    )
    text = text_element.text

    # Use regular expressions to find all numbers after a certain phrase
    pattern = r"Indexed Secret value of position (\d+) & (\d+)"
    match = re.search(pattern, text)
    if match:
        # Retrieve numbers from the text
        indexes = [int(match.group(1)), int(match.group(2))]
        
        # Retrieve the token using the indexes
        token = ''.join(token_dict[str(index)] for index in indexes)
        token_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'fudis_otp_input')) 
        )
        token_input.send_keys(token)

        # Search for and click the login button
        validate_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, '_eventId_proceed'))
        )
        validate_button.click()
    else:
        print("Relevant text not found.")
except Exception as e:
    print("An error occurred during login:", e)
     # Close the driver in case of an error
    
# Close the driver after completion
while True:
    pass

