'''
markers :
    * builtin
            * skip
            * skipif
            * parametrize
            * xfail
    * custom

'''

#-----------------------------------------------------------------
import pytest


## skip : To skip a specific testcase, we go for skip marker.
## This is an unconditional skip, because using skip we can skip the testcase without passing the condition
## and also without specifying the reason


# def test_login():
#     print('login executing')
#
# @pytest.mark.skip
# def test_signup():
#     print('signup executing')
#
# def test_reg():
#     print('reg executing')
#
# def test_logout():
#     print('logout executing')
#
# ## collected 4 items
# ## test_markers.py::test_login login executing             PASSED
# ## test_markers.py::test_signup                            SKIPPED (unconditional skip)
# ## test_markers.py::test_reg reg executing                 PASSED
# ## test_markers.py::test_logout logout executing           PASSED
#
# #------------------------------------------------------------------
#
# def test_login():
#     print('login executing')
#
# @pytest.mark.skip
# def test_signup():
#     prin('signup executing')
#
# ## collected 2 items
# ## test_markers.py::test_login login executing             PASSED
# ## test_markers.py::test_signup                            SKIPPED (unconditional skip)
#
# ## If we are having any error in the skipped testcases, the error will not be considered
#
# #------------------------------------------------------------------
#
# def test_login():
#     print('login executing')
#
# @pytest.mark.skip(reason="unwanted testcase")
# def test_signup():
#     print('signup executing')
#
# ## collected 2 items
# ## test_markers.py::test_login login executing             PASSED
# ## test_markers.py::test_signup                            SKIPPED (unwanted testcase)
#
# ## We can pass the reason to skip the testcase, however it is a optional parameter
#
# #--------------------------------------------------------------
#
# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print('login executing')
#
#     def test_signup(self):
#         print('signup executing')
#
# ## collected 2 items
# ## test_markers.py::TestSample::test_login SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup SKIPPED (unconditional skip)
#
# #----------------------------------------------------------------
#
# ## skipif : This is a marker used to skip the testcases,
# ## skipif takes two parameters, first one is the condition and the second parameter is the reason
# ## condition and reason, both are mandatory parameters
#
# str_ = 'python is awesome'
#
# @pytest.mark.skipif('Awe' in str_, reason='unnecessary tc')
# def test_case1():
#     print(str_)     ## execute
#
# @pytest.mark.skipif('awe' in str_, reason='unnecessary tc')
# def test_case2():
#     print(str_)     ## skipped
#
#
# ## collected 2 items
# ## test_markers.py::test_case1 python is awesome           PASSED
# ## test_markers.py::test_case2                             SKIPPED (unnecessary tc)
#
# #---------------------------------------------
# str_ = 'python is awesome'
#
# @pytest.mark.skipif('Awe' in str_)
# def test_case1():
#     print(str_)     ## execute
#
# @pytest.mark.skipif('awe' in str_)
# def test_case2():
#     print(str_)     ## skipped
#
# ## collected 2 items
# ## test_markers.py::test_case1 ERROR
# ## test_markers.py::test_case2 ERROR
#
# # ## Error because, the reason for skip is not mentioned
#
# #-------------------------------------------------------------------------------
# ## xfail
#
# def test_login():
#     print('login executing')
#
# @pytest.mark.xfail
# def test_signup():
#     print('signup executing')
#
# ## collected 2 items
# ## test_markers.py::test_login login executing         PASSED
# ## test_markers.py::test_signup signup executing       XPASS
#
# #-------------------------------------------------------
#
# def test_login():
#     print('login executing')
#
# @pytest.mark.xfail
# def test_signup():
#     prin('signup executing')
#
# ## collected 2 items
# ## test_markers.py::test_login login executing     PASSED
# ## test_markers.py::test_signup                    XFAIL
#
# #------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts =  webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# # driver.implicitly_wait(30)
# wait_object = WebDriverWait(driver, 30)
#
# driver.get('https://www.saucedemo.com/')
#
# def test_credentials():
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
#     driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
#
# @pytest.mark.xfail
# def test_click_login():
#     driver.find_element('xpath', '//input[@id="login-button"]').click()
#     home_page_element = driver.find_element('xpath', '//span[text()="Products"]')
#     wait_object.until(expected_conditions.visibility_of(home_page_element))

#--------------------------------------------------------------------------------------------
## parametrize

# @pytest.mark.parametrize("a, b", [(1, 2)])
# def test_additon(a, b):
#     print(a + b)

## collected 1 item
## test_markers.py::test_additon[1-2] 3        PASSED

#--------------------------------------------------
# @pytest.mark.parametrize("a, b", [(1, 2), (2, 3), (-10, -20), (2, 3)])
# def test_additon(a, b):
#     print(a + b)

## collected 4 items
## test_markers.py::test_additon[1-2] 3        PASSED
## test_markers.py::test_additon[2-30] 5       PASSED
## test_markers.py::test_additon[-10--20] -30  PASSED
## test_markers.py::test_additon[2-31] 5       PASSED

#_---------------------------------------------

# @pytest.mark.parametrize("a, b", [(1, 2), (2, 3)])
# def test_additon(a, b, c):
#     print(a + b + c)

## collected 2 items
## test_markers.py::test_additon[1-2] ERROR
## test_markers.py::test_additon[2-3] ERROR


## Number of parameters are not matching

#---------------------------------------------
# @pytest.mark.parametrize("a, b, c", [(1, 2), (2, 3, 4)])
# def test_additon(a, b, c):
#     print(a + b + c)

## Error

#-----------------------------------------
# @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (2, 3, 4)])
# def test_additon(a, b, c):
#     print(a + b + c)

## collected 2 items
## test_markers.py::test_additon[1-2-3] 6          PASSED
## test_markers.py::test_additon[2-3-4] 9          PASSED

#------------------------------------------
# @pytest.mark.parametrize("a, b, c", [(1, 2), (2, 3, 4)])
# def test_additon(a, b, c=0):
#     print(a + b + c)
#
# ## ERROR

#---------------------------------------------
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# wait_object = WebDriverWait(driver, 30)
#
#
# @pytest.mark.parametrize("username, pwd", [('standard_user', 'secret_sauce'), ('abcd', 'secret_sauce'), ('standard_user', 'secret_sauce'), ('abcd', 'abcd')])
# def test_login(username, pwd):
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys(username)
#     driver.find_element('xpath', '//input[@id="password"]').send_keys(pwd)
#     driver.find_element('xpath', '//input[@id="login-button"]').click()
#
#     try:
#         home_page_element = driver.find_element('xpath', '//span[text()="Products"]')
#         wait_object.until(expected_conditions.visibility_of(home_page_element))
#         print('successfull login')
#     except:
#         print('unsuccessfull login')
#     time.sleep(2)
#
#
# ## collected 4 items
# ## test_markers.py::test_login[standard_user-secret_sauce0]    successfull login               PASSED
# ## test_markers.py::test_login[abcd-secret_sauce]              unsuccessfull login             PASSED
# ## test_markers.py::test_login[standard_user-secret_sauce1]    successfull login               PASSED
# ## test_markers.py::test_login[abcd-abcd]                      unsuccessfull login             PASSED

#-------------------------------------------------------------------------------------

# @pytest.mark.sanity
# def test_add():
#     print('addition executing')
#
# @pytest.mark.smoke
# def test_sub():
#     print('subtraction executing')
#
# @pytest.mark.sanity
# def test_mul():
#     print('multiplicatiion executing')
#
# @pytest.mark.regression
# def test_div():
#     print('division executing')


## In terminal --> pytest test_markers.py -vs -m="sanity"
## collected 4 items / 2 deselected / 2 selected
## test_markers.py::test_add addition executing                PASSED
## test_markers.py::test_mul multiplicatiion executing         PASSED

## In terminal --> pytest test_markers.py -vs -m="smoke" --> test_sub will execute

## In terminal --> pytest test_markers.py -vs -m="sanity and smoke" -->  All 4 will be deselected
## In terminal --> pytest test_markers.py -vs -m="sanity or smoke" --> test_Add, test_sub, test_mul will execute

#----------------------------------------------------------------------------

@pytest.mark.sanity
def test_add():
    print('addition executing')

@pytest.mark.sanity
@pytest.mark.smoke
def test_sub():
    print('subtraction executing')

@pytest.mark.sanity
def test_mul():
    print('multiplicatiion executing')

@pytest.mark.smoke
@pytest.mark.regression
def test_div():
    print('division executing')





































































































































































