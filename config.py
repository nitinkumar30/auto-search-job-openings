from main import *

import chromedriver_autoinstaller

# download latest chromedriver for chrome
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)


# The website for career job posting
indeed = "https://in.indeed.com/jobs?q=" + key + "&l=" + city + "%2C%20" + state
