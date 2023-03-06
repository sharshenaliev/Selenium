from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from proxy_randomizer import RegisteredProviders
import time
from editor import edit
from solver import opencv
from data import profile

rp = RegisteredProviders()
rp.parse_providers()
proxy = rp.get_random_proxy()
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server="http={proxy.ip_address}:{proxy.port};https={proxy.ip_address}:{proxy.port}"')
# chrome_options.headless = True

def main():
    driver = webdriver.Chrome()
    try:
        # driver.get('https://cova.mfa.gov.cn/')
        # menu = driver.find_element(By.ID, "AS")
        # menu.click()
        # element = driver.find_element(By.ID, "KGZ")
        # link = element.find_element(By.TAG_NAME, "li")
        # link.click()
        # button = driver.find_element(By.TAG_NAME, "button")
        # button.click()
        # code = driver.find_element(By.TAG_NAME, "code")
        # number = code.text
        driver.get('https://avas.mfa.gov.cn/qzyyCoCommonController.do?yypersoninfo&status=continue&1677827277761&locale=ru_RU')
        applyid = driver.find_element(By.ID, "applyid1")
        applyid.send_keys(profile['applyid'], Keys.ARROW_DOWN)
        linkname = driver.find_element(By.ID, "linkname")
        linkname.send_keys(profile['linkname'], Keys.ARROW_DOWN)
        linkphone = driver.find_element(By.ID, "linkphone")
        linkphone.send_keys(profile['linkphone'], Keys.ARROW_DOWN)
        mail = driver.find_element(By.ID, "mail")
        mail.send_keys(profile['mail'], Keys.ARROW_DOWN)
        div = driver.find_element(By.ID, "GoToDefUrl")
        button_go = div.find_element(By.TAG_NAME, "button")
        button_go.click()
        time.sleep(10)
        iframe = driver.find_element(By.ID, "tcaptcha_iframe_dy")
        driver.switch_to.frame(iframe)
        style = driver.find_element(By.ID, "slideBg")
        style.screenshot('image.png')
        edit()
        position = opencv()
        newpos = (position[0]- 35)
        mydiv = driver.find_element(By.ID, "tcOperation")
        inputTag = mydiv.find_element(By.XPATH, "//div[@class='tc-fg-item tc-slider-normal']")
        action = ActionChains(driver)
        webdriver.ActionChains(driver).drag_and_drop_by_offset(inputTag, newpos, 0).perform()
        time.sleep(60 * 60 * 2)
    except:
        print('please try again')
    driver.quit()
    
if __name__ == "__main__":
    main()