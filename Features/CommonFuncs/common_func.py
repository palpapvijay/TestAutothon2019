import moment
import logging
#from PyScripts import ucsd_infra_log_validator
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from utils import util as util
import subprocess
import requests
from requests.auth import HTTPBasicAuth
import json
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Lib import configReader
import time
from selenium.common.exceptions import TimeoutException
import logging
logger = logging.getLogger(__name__)

__author__ = 'vijayago'

"""
Function to will store the Infra Error log in local Logs folder
And it will be attached to Allure Reports.

func_name = function name of calling function
"""
def gmail_log_attach(func_name):
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        Infrafilename = func_name + "_" + currTime
        conn = gmail_infra_log_validator.gmail_ssh_connector(util.sshServer, util.sshUsername, util.sshPassword)
        status = gmail_infra_log_validator.gmail_error_file(conn, Infrafilename)
        if status == True:
                path = "./Logs/" + Infrafilename + ".html"
                allure.attach(open(path, "rb").read(), name=Infrafilename, attachment_type=AttachmentType.HTML)
        elif status == False:
                print("No Logs files to attach in Allure reports")
"""
Function to attach the failure scenario snapshots in allure reports.
func_name = function name of calling function
"""
def gmail_screenshot_attach_allure(context,func_name):
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        Snapshotfilename = func_name + "_" + currTime
        allure.attach(context.driver.get_screenshot_as_png(), name=Snapshotfilename, attachment_type=AttachmentType.PNG)
        print("Snapshot Attached in Allure Reports")

"""
Function to save snapshots in local Screenshots folder.
func_name = function name of calling function
"""
def gmail_screenshot_save(context,func_name):
        currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        Snapshotfilename = func_name + "_" + currTime
        context.driver.save_screenshot("./Screenshots/" + Snapshotfilename + ".png")
        print("Snapshot Saved in Specified Path")

def get_text(context, locator, Type):
    try:
        if Type == "ID":
            logging.info("Getting the text in the given locator: " + locator)
            element = context.driver.find_element_by_id(locator)
            return element.text

        elif Type == "NAME":
            logging.info("Getting the text in the given locator: " + locator)
            element = context.driver.find_element_by_name(locator)
            return element.text

        elif Type == "XPATH":
            logging.info("Getting the text in the given locator: " + locator)
            element = context.driver.find_element_by_xpath(locator)
            return element.text

        elif Type == "CSS":
            logging.info("Getting the text in the given locator: " + locator)
            element = context.driver.find_element_by_css_selector(locator)
            return element.text

        else:
            logger.warning("Please specify Proper locator")
            return False

    except TimeoutException:
        logger.error("Unable to find the speficied element:" + locator)
        return False
        raise

"""
Function to wait until specified browser title
if successfully loaded it will return True 
else False
"""
def wait_until_title(context,title):
        try:
                WebDriverWait(context.driver, 30).until(EC.title_is(title))
                print("Expected Title Present:" " "+title)
                return True

        except TimeoutException:
                print("Unable to locate title:" " "+title)
                return False
                raise

"""
Function will compare actual value with expected value.
if it matches it will return True
else False
"""
def compare(context,actual,expected):
        try:
                assert actual == expected
                print("Compared both Actual:" +actual  +"and Expected:" + expected +"are equal")
                return True

        except AssertionError:
                print("Compared both Actual:" +actual + "and Expected:" + expected + "are Not equal")
                return False
                raise

"""
Function will Close the Browser
"""
def close_browser(context):
        context.driver.close()

"""
Function will Quit the Browser
"""
def quit_browser(context):
        context.driver.quit()

"""
Function to Enter Text in Text box
"""

def Enter_Text(context,locator,input,Type):
        if Type == "ID":
                context.driver.find_element_by_id(locator).clear()
                context.driver.find_element_by_id(locator).send_keys(input)
        elif Type == "NAME":
                context.driver.find_element_by_id(locator).clear()
                context.driver.find_element_by_name(locator).send_keys(input)
        elif Type == "XPATH":
                context.driver.find_element_by_xpath(locator).clear()
                context.driver.find_element_by_xpath(locator).send_keys(input)
        else:
                print("Please specify Proper Type Value")

"""
Function to Click Any Button
Return True for success else False
"""
def Click_Button(context,locator,Type):
        try:
                if Type == "ID":
                        WebDriverWait(context.driver,30).until(EC.element_to_be_clickable((By.ID,locator)))
                        context.driver.find_element_by_id(locator).click()
                        return True

                elif Type == "NAME":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.NAME, locator)))
                        context.driver.find_element_by_name(locator).click()
                        return True

                elif Type == "XPATH":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
                        context.driver.find_element_by_xpath(locator).click()
                        return True

                elif Type == "CSS":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
                        context.driver.find_element_by_xpath(locator).click()
                        return True
                else:
                        print("Please specify Proper Type Value")
                        return False

        except TimeoutException:
                print("Unable to Click Specified Button:" + locator)
                return False
                raise

"""
Function to Check Presence of any any element
return True if found else False
"""

def presence_of_element(context,locator,Type):
        try:
                if Type == "ID":
                        WebDriverWait(context.driver, 30).until(EC.presence_of_element_located((By.ID, locator)))
                        return True

                elif Type == "NAME":
                        WebDriverWait(context.driver, 30).until(EC.presence_of_element_located((By.NAME, locator)))
                        return True

                elif Type == "XPATH":
                        WebDriverWait(context.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator)))
                        return True
                else:
                        print("Please specify Proper Type Value")
                        return False

        except TimeoutException:
                print("Unable to find Specified Element:" + locator)
                raise


"""
Function to Click Menu's in Application
Return True for success else False
"""

def Click_Menu(context,locator,Type):
        try:
                if Type == "ID":
                        WebDriverWait(context.driver,30).until(EC.element_to_be_clickable((By.ID,locator)))
                        context.driver.find_element_by_id(locator).click()
                        return True

                elif Type == "NAME":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.NAME, locator)))
                        context.driver.find_element_by_name(locator).click()
                        return True

                elif Type == "XPATH":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
                        context.driver.find_element_by_xpath(locator).click()
                        return True
                else:
                        print("Please specify Proper Type Value")
                        return False

        except TimeoutException:
                print("Unable to Click Specified Menu:" + locator)
                return False


"""
Function to Click Combo box in the Application
Return True for Success else False
"""

def Click_Combo(context,locator,Type):
        try:
                if Type == "ID":
                        WebDriverWait(context.driver,30).until(EC.element_to_be_clickable((By.ID,locator)))
                        context.driver.find_element_by_id(locator).click()
                        return True

                elif Type == "NAME":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.NAME, locator)))
                        context.driver.find_element_by_name(locator).click()
                        return True

                elif Type == "XPATH":
                        WebDriverWait(context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
                        context.driver.find_element_by_xpath(locator).click()
                        return True
                else:
                        print("Please specify Proper Type Value")
                        return False

        except TimeoutException:
                print("Unable to Click Specified Combo:" + locator)
                return False
                raise

