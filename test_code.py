from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# driver = webdriver.Chrome()
# driver.get('http://sahitest.com/demo/selectTest.htm')
#
# s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
#
# s1.select_by_index(1)  # 选择第二项选项：o1
# s1.select_by_value("o2")  # 选择value="o2"的项
# s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本
#
# time.sleep(10)
# driver.quit()


# !/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)  # 关掉浏览器左上角的通知提示
options.add_argument("disable-infobars")  # 关闭'chrome正受到自动测试软件的控制'提示
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://wenku.baidu.com/")  # 百度文库
radios = driver.find_elements_by_xpath("//*/input[@type='radio']")  # 找到页面的单选按钮
count = 0
for radio in radios:
    is_selected = radio.is_selected()  # 判断按钮是否被选中，选中返回True，没有选中返回false
    if is_selected:  # 返回True时，就执行下面的语句
        count += 1
        print("被选中", " ", count)
    else:
        print("没有被选中", is_selected)
time.sleep(5)
driver.quit()
