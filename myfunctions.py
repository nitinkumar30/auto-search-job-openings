from main import *


# Find element and display the text provided xpath
def findEleAndDispText(xpath):
    try:
        if driver.find_element(By.XPATH, xpath).is_displayed():
            elmTxt = driver.find_element(By.XPATH, xpath).text
            return elmTxt
    except:
        print(xpath, ' not found.')
        elmTxt = "N.A."
        return elmTxt


# Find element and click on it if it's visible
def findEleAndClick(xpath):
    try:
        if driver.find_element(By.XPATH, xpath).is_displayed():
            driver.find_element(By.XPATH, xpath).click()
    except:
        print(xpath, ' not found.')
        elmTxt = "N.A."
        return elmTxt


def findEleAndFindLink(xpath):
    try:
        if driver.find_element(By.XPATH, xpath).is_displayed():
            url = driver.find_element(By.TAG_NAME, 'a').get_attribute('href')
            return url
    except:
        print(xpath, ' not found.')
        url = "N.A."
        return url
