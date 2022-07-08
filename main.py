# This is a module to just search for the available job openings in portals

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

from myfunctions import findEleAndClick, findEleAndFindLink, findEleAndDispText
from variables import *
from config import *
from xpaths import *




# Website opened
driver.get(indeed)


# Writing the title of the newly file created
with open('jobReq.txt', 'w', encoding="utf-8") as f:
    toWrite = "Following job requirements are present as of " + str(datetime.now())
    f.write(toWrite)
    f.write('\n-------------------------------------------------------------------------')




    # Code started
    # findEleAndClick(role)
    role_ = findEleAndDispText(role)
    companyName_ = findEleAndDispText(companyName)
    companyLocation_ = findEleAndDispText(companyLocation)
    salary_ = findEleAndDispText(salary)
    jobType_ = findEleAndDispText(jobType)
    # shift_ = findEleAndDispText(shift)
    # hiringType_ = findEleAndDispText(hiringType)
    # noOfCandidatesHiring_ = findEleAndDispText(noOfCandidatesHiring)
    jobDesc_ = findEleAndDispText(jobDesc)
    datePosted_ = findEleAndDispText(datePosted).replace("\n", " ")
    linkToJob__ = driver.find_element(By.XPATH, eleForJobLink)
    linkToJob_ = linkToJob__.get_attribute('href')

    # write the newest text in new file jobReq.txt
    filename = str(datetime.now()) + '.txt'
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "-")

    with open('jobReq.txt', 'a', encoding="utf-8") as f:
        data = "\n\n\nRole: " + role_ + "\nCompany Name: " + companyName_ + "\nCompany Location: " + companyLocation_ + \
               "\nSalary: " + salary_ + "\nHiring Type: " + jobType_ + "\nJob Description: " + jobDesc_ + \
               "\nDate Posted: " + datePosted_ + "\nLink for job: " + linkToJob_
        rslt = f.write(data)
        if rslt:
            print("Writing into the file done.")

# driver.close()
