from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox(executable_path=r'geckodriver.exe')
#driver=webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get("http://www.google.com")
# driver.maximize_window()
# driver.refresh()
# driver.set_page_load_timeout(20)
# driver.implicitly_wait(30)
# driver.find_element_by_xpath("//div[contains(@class,'a4')]/input").send_keys("shoes")
# driver.find_element_by_xpath("//div[contains(@class,'FP')]/center/input").click()
# driver.find_element_by_css_selector("")
# time.sleep(5)
# driver.back()
# driver.forward()
driver.maximize_window()
driver.get("http://www.rediffmail.com")
driver.refresh()
# l=driver.find_elements_by_tag_name("a")
# driver.find_element_by_class_name("mailicon").click()
# driver.find_element_by_css_selector("input#login1[name='login']").send_keys("ankit")
# driver.find_element_by_id("password").send_keys("passwd")
# driver.find_element_by_name("proceed").click()
# driver.find_element_by_link_text("Forgot Password?").click()
# driver.back()
# driver.find_element_by_partial_link_text("Password?").click()
driver.find_element_by_xpath("//div[@class='srch_outer']/input").send_keys("cricket")
time.sleep(10)
search_ele=driver.find_elements_by_xpath("//div[@id='sugbox']/div[contains(@id,'suggest')]")
print(len(search_ele))
search_ele[1].click()
#search_ele[1].click()
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_id('fruits01'))
select.select_by_visible_text()
select.select_by_index()
select.select_by_value()


# s=[]
# s=driver.window_handles
# print(len(s))
# o=driver.current_window_handle
# print(len(l))
# driver.back()
# driver.forward()
act=ActionChains(driver)
act.double_click().send_keys_to_element().perform()