from selenium import webdriver
driver=webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.maximize_window()
driver.get("https://www.toolsqa.com/automation-practice-switch-windows/")
ori=driver.current_window_handle
driver.find_element_by_id("button1").click()
s=driver.window_handles
for n in range(len(s)):
    if s[n]!=ori:
        driver.switch_to.window(s[n])
        driver.close()
driver.switch_to.window(ori)

print(driver.title)
