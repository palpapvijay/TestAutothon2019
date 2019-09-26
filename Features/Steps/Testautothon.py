from Features.CommonFuncs.common_func import *
import logging
from behave import *
from Lib import configReader
logger = logging.getLogger(__name__)

@when(u'search "step-in forum facebook"')
def google_searchfor_StepIn(context):
    locator = configReader.stepinconfig("StepInForum", "GSearch")
    Click_Button(context,locator,"XPATH")
    logger.info("Clicking on the Google search button")
    time.sleep(5)
    locator1 = configReader.stepinconfig("StepInForum", "GsearchValue")
    Enter_Text(context, locator, locator1 , "XPATH")
    logger.info("Entering the text in Googlesearch box")
    time.sleep(8)

@when("click the google search button")
def clickingSearchbutton(context):
    locator = configReader.stepinconfig("StepInForum", "Click_GoogleSearch")
    Click_Button(context,locator,"NAME")
    logger.info("Clicking on google search button")

@then(u'Navigate to the link fetched from the above step')
def stepinsubmit_facebookpage(context):
    locator = configReader.stepinconfig("StepInForum", "ClickCommunity_Forum_Link" )
    Click_Button(context,locator,"XPATH")
    logger.info("Clicking on the forum link")
    locator=configReader.stepinconfig("StepInForum","enteremail")
    locator1=configReader.stepinconfig("StepInForum","entermailid")
    Enter_Text(context,locator,locator1, "XPATH")
    logger.info("Entered email successfully")
    logger.info("Clicking on the forum link")
    locator = configReader.stepinconfig("StepInForum", "enterpass")
    locator1 = configReader.stepinconfig("StepInForum", "enterpassword")
    Enter_Text(context, locator, locator1, "XPATH")
    locator = configReader.stepinconfig("StepInForum", "enterlogin")
    Click_Button(context,locator,"XPATH")
    time.sleep(6)
    locator = configReader.stepinconfig("StepInForum", "GSearch")
    locator1=configReader.stepinconfig("StepInForum", "enterforum")
    Enter_Text(context, locator, locator1,"XPATH")
    locator=configReader.stepinconfig("StepInForum", "clicksearch")
    Click_Button(context,locator,"XPATH")
    locator = configReader.stepinconfig("StepInForum", "clickstepforumfb")
    Click_Button(context, locator, "XPATH")
    if wait_until_title(context, "STep-IN Forum-Home") is True:
        logger.info("Navigated to STep-IN Forum-Home page Successfully")
    else:
        logger.critical("unable to Navigated to STep-IN Forum-Home page Successfully")
        quit_browser(context)




