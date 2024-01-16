from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_browser = webdriver.Chrome()

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button_text = show_message_button.get_attribute('innerHTML')
print(show_message_button_text)

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I\'m really filling this form out from my code')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'I\'m really filling this form out from my code' in output_message.text

print(output_message)





input("Press Enter to close the browser...")

chrome_browser.quit()





# print(chrome_browser)
