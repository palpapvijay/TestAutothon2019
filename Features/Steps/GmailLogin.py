from Features.CommonFuncs.common_func import *
import logging
from behave import *
from Lib import configReader
logger = logging.getLogger(__name__)


__author__ = 'vijayago'

########################## Gmail Login Page Common Steps ########################################



"""
Funtion to Enter Valid Username in Gmail Login Page
"""
@when(u'user enters valid gmail username')
def enter_valid_ucsd_username(context):
    locator = configReader.readConfigData("Script", "USERNAME")
    Enter_Text(context,locator,"testhackpune","XPATH")
    time.sleep(7)

"""
Funtion to Enter Valid Password in Gmail Login Page
"""
@when(u'user enters valid gmail password')
def enter_ucsd_password(context):
    locator = configReader.readConfigData("Script", "PASSWORD")
    Enter_Text(context,locator, "testautothon", "XPATH")
    time.sleep(7)

"""
Funtion to Click Next Button in Gmail Login Page
"""
@when(u'user clicks next button')
def click_ucsd_login_submit(context):
    locator = configReader.readConfigData("Script", "ClickNext")
    if Click_Button(context,locator,"XPATH") is True:
        pass
        #func_name = util.whoami()
        #ucsd_log_attach(func_name)
    else:
        pass
        func_name = util.whoami()
    time.sleep(7)



"""
Funtion to Validate Gmail Login success

"""
@then(u'user should be logged in successfully')
def gmail_login_success(context):
    locator=configReader.readgmailelements("gmaillogin","Inboxlink")
    if presence_of_element(context,locator, "XPATH") is True:
           logger.info("User Logged In Successfully")
    else:
        logger.critical("Gmail Login Failed..Exit Testing")
        quit_browser(context)
