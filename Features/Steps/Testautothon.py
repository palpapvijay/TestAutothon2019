from Features.CommonFuncs.common_func import *
import logging
from behave import *
from Lib import configReader
logger = logging.getLogger(__name__)

@when(u'search "step-in forum facebook"')
def google_searchfor_StepIn(context):
    locator = configReader.stepinconfig("StepInForum", "GSearch")
    Click_Combo(context,locator,"XPATH")
    locator1 = configReader.stepinconfig("StepInForum", "GsearchValue")
    Enter_Text(context, locator, locator1 , "XPATH")
    time.sleep(8)

@when("click the google search button")
def clickingSearchbutton(context):
    locator = configReader.stepinconfig("StepInForum", "Click_GoogleSearch")
    Click_Button(context,locator,"XPATH")

@then(u'Navigate to the link fetched from the above step')
def stepinsubmit_facebookpage(context):
    locator = configReader.stepinconfig("StepInForum", "ClickCommunity_Forum_Link" )
    Click_Button(context,locator,"XPATH")


