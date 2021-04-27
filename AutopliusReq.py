from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')



driver = webdriver.Chrome(options=options, executable_path='C:/Users/user/Downloads/chromedriver.exe')



def renew():

    driver.get ('https://autoplius.lt/mano-aplinka/skelbimai?action=renew_all&id=1&page_nr=1')

    driver.find_element_by_id('username-lookup').send_keys('test@gmail.com')
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//button[text()='Tęsti']").click();

    driver.find_element_by_id('password').send_keys('testpassword')

    driver.find_element_by_xpath("//button[text()='Prisijungti']").click();

    driver.implicitly_wait(4)
    driver.find_element_by_css_selector(".button.renew-all-button").click()

renew()
