from selenium import webdriver
from Lib import configReader
import os
import glob
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


__author__ = 'vijayago'

# Before and After All feature
def before_all(context):

    print("Cleanup Logs and Snapshots Folders")
    files = glob.glob('./Logs/*')
    for f in files:
        os.remove(f)
    files = glob.glob('./Screenshots/*')
    for f in files:
        os.remove(f)

    if (configReader.readConfigData('Details', 'Browser')) == "chrome":
        path = "./Drivers/chromedriver.exe"
        context.driver = webdriver.Chrome(executable_path=path)
    elif (configReader.readConfigData('Details', 'Browser')) == "firefox":
        path = "./Drivers/geckodriver.exe"
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        context.driver = webdriver.Firefox(capabilities=cap, executable_path=path)
    elif (configReader.readConfigData('Details', 'Browser')) == "ie":
        path = "./Drivers/IEDriverServer.exe"
        context.driver = webdriver.Ie(executable_path=path)
    else:
        path = "./Drivers/chromedriver.exe"
        context.driver = webdriver.Chrome(executable_path=path)

    context.driver.get(configReader.readConfigData('Details', 'gmail IP'))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()



def after_all(context):
    context.driver.close()

# Before and After for every All feature
# def before_feature(context,feature):
#     path = "./Drivers/chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#
#
# def after_feature(context,feature):
#     context.driver.close()

# Before and After for every Scenario feature
# def before_scenario(context,scenario):
#     path = "./Drivers/chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#
#
# def after_scenario(context,scenario):
#     context.driver.close()
