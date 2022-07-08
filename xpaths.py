from main import *

popupForMailSignup = "//button[@class='popover-x-button-close icl-CloseButton']"

for i in range(1, 11):
    # xpaths for this website
    role = "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[5]/div/ul/li["+str(i)+"]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a/span"
    companyName = "//*[@id='mosaic-provider-jobcards']/ul/li["+str(i)+"]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/span"
    companyLocation = "//*[@id='mosaic-provider-jobcards']/ul/li["+str(i)+"]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div"
    salary = "///*[@id='mosaic-provider-jobcards']/ul/li["+str(i)+"]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[3]/div"
    jobType = "//*[@id='jobDetailsSection']/div["+str(i+1)+"]/div[2]"
    # shift = "//div[@class='attribute_snippet'][3]"
    # hiringType = "//div[@class='urgentlyHiring']"
    # noOfCandidatesHiring = "//div[@class='hiringMultipleCandidatesCaption']"
    jobDesc = "//*[@id='jobDescriptionText']"
    datePosted = "//*[@id='mosaic-provider-jobcards']/ul/li["+str(i)+"]/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div/span"
    eleForJobLink = "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div[5]/div/ul/li[1]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a"
