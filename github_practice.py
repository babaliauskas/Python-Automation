from selenium import webdriver
import os
import time

user_input = input("Enter Repository name: ")

driver = webdriver.Chrome()
driver.get("http://github.com")

signin_btn = driver.find_element_by_xpath("//a[@href='/login']")
signin_btn.click()

login_username_input = driver.find_element_by_css_selector("input#login_field")
login_password_input = driver.find_element_by_css_selector("input#password")
login_btn = driver.find_element_by_css_selector("input[type='submit']")


login_username_input.send_keys('YourUsername')  # Change it to your username
login_password_input.send_keys('YourPassword')  # Change it to your password
login_btn.click()


new_repository_btn = driver.find_element_by_css_selector(
    "div.js-repos-container > h2 > a[href='/new']")
new_repository_btn.click()


new_repository_input = driver.find_element_by_css_selector(
    "input#repository_name")
new_repository_input.send_keys(user_input)

repository_description_input = driver.find_element_by_css_selector(
    "input#repository_description")
repository_description_input.send_keys("From Python")

create_repository_btn = driver.find_element_by_css_selector(
    "div.js-with-permission-fields > button[type='submit']")

time.sleep(0.5)
create_repository_btn.click()

time.sleep(0.5)
os.chdir("/Users/babaliauskas/coding/projects/python")
time.sleep(0.5)
os.system(f"mkdir {user_input}")
time.sleep(0.5)
os.chdir(f"/Users/babaliauskas/coding/projects/python/{user_input}")
time.sleep(0.5)
os.system('touch index.py')
time.sleep(0.5)
os.system("git init")
time.sleep(0.5)
os.system("git add .")
time.sleep(0.5)
os.system("git commit -m 'first commit'")
time.sleep(0.5)
os.system(
    f"git remote add origin https://github.com/babaliauskas/{user_input}.git")
time.sleep(0.5)
os.system("git push -u origin master")

time.sleep(1)
driver.refresh()
