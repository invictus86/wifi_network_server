# -*- encoding=utf8 -*-
__author__ = "ivan.zhao"

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import time
import logging

logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='./log/wifi_chrome.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )


def set_wifi_parameter_wep():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[3]/a').click()
        driver.find_element_by_id("inetsetup").click()
        time.sleep(2)
        s1 = Select(driver.find_element_by_id('security_type'))
        s1.select_by_value("wep")
        time.sleep(1)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[3]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        logging.info('set_parameter_wep success')
    except:
        logging.info('set_parameter_wep fail')


def set_wifi_parameter_wpa():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[3]/a').click()
        driver.find_element_by_id("inetsetup").click()
        time.sleep(2)
        s1 = Select(driver.find_element_by_id('security_type'))
        s1.select_by_value("wpa_1")
        time.sleep(1)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[3]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        logging.info('set_parameter_wpa success')
    except:
        logging.info('set_parameter_wpa fail')


def set_wifi_parameter_wpa2():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[3]/a').click()
        driver.find_element_by_id("inetsetup").click()
        time.sleep(2)
        s1 = Select(driver.find_element_by_id('security_type'))
        s1.select_by_value("wpa_2")
        time.sleep(1)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[3]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        logging.info('set_parameter_wpa2 success')
    except:
        logging.info('set_parameter_wpa2 fail')


def set_wifi_parameter_wpa_wpa2():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[3]/a').click()
        driver.find_element_by_id("inetsetup").click()
        time.sleep(2)
        s1 = Select(driver.find_element_by_id('security_type'))
        s1.select_by_value("wpa")
        time.sleep(1)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[3]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        logging.info('set_parameter_wpa_wpa2 success')
    except:
        logging.info('set_parameter_wpa_wpa2 fail')


def set_wifi_parameter_802_11n():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="menu"]/div[2]/a[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[9]/a').click()
        s1 = Select(driver.find_elements_by_xpath('//*[@id="wlan_mode"]')[0])
        time.sleep(2)
        s1.select_by_value("n")
        time.sleep(2)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[2]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        logging.info('set_parameter_802_11n success')
    except:
        logging.info('set_parameter_802_11n fail')


def set_wifi_parameter_802_11b_g():
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="menu"]/div[2]/a[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[9]/a').click()
        s1 = Select(driver.find_elements_by_xpath('//*[@id="wlan_mode"]')[0])
        time.sleep(2)
        s1.select_by_value("bg")
        time.sleep(2)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[2]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        logging.info('set_parameter_802_11b_g success')
    except:
        logging.info('set_parameter_802_11b_g fail')


def set_wifi_ap_on():
    try:
        start_time = time.time()
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[3]/a').click()
        driver.find_element_by_id("inetsetup").click()
        time.sleep(2)
        driver.find_element_by_id("en_wifi").click()
        time.sleep(1)
        driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[3]/input[1]')[0].click()
        sleep(5)
        driver.quit()
        end_time = time.time()
        logging.info('set_wifi_ap_on success')
        return end_time - start_time
    except:
        logging.info('set_wifi_ap_on fail')
        return 0


def set_wifi_ap_off():
    try:
        start_time = time.time()
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("http://192.168.0.1")
        driver.find_element_by_id("noGAC").click()
        driver.find_element_by_id("config_manual").click()
        driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[3]/a').click()
        driver.find_element_by_id("inetsetup").click()
        time.sleep(2)
        driver.find_element_by_id("en_wifi").click()
        time.sleep(1)
        # driver.find_elements_by_xpath('//*[@id="mainform"]/div[1]/p[3]/input[1]')[0].click()
        text = driver.find_element_by_id('sch')
        print(text)
        sleep(5)
        driver.quit()
        end_time = time.time()
        logging.info('set_wifi_ap_off success')
        return end_time - start_time
    except:
        logging.info('set_wifi_ap_off fail')
        return 0


if __name__ == '__main__':
    # set_wifi_parameter_wep()
    # time.sleep(5)
    # set_wifi_parameter_wpa()
    # time.sleep(5)
    # set_wifi_parameter_wpa2()
    # time.sleep(5)
    # set_wifi_parameter_wpa_wpa2()
    # time.sleep(5)
    # set_wifi_parameter_802_11n()
    # set_wifi_parameter_802_11b_g()
    # start_time = time.time()
    # set_wifi_ap_on()
    # end_time = time.time()
    # print(end_time - start_time)
    set_wifi_ap_off()
