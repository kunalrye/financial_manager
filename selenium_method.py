from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass
import os
import time
import shutil
 
chromedriver = ('/Users/kunal/Downloads/chromedriver')
 
username = "######"
m_word = "######"
password = "######"
browser = webdriver.Chrome(chromedriver)
print ("Logging into HSBC...")
 
browser.set_window_position(-3000, 0)
browser.get("https://www.hsbc.co.uk/1/2/welcome-gsp?initialAccess=true&IDV_URL=hsbc.MyHSBC_pib")
browser.find_element_by_id('Username1').send_keys(username)
browser.find_element_by_xpath('//*[@id="ibLogonForm"]/div[2]/div[2]/span/input').click()
browser.find_element_by_xpath('//*[@id="innerPage"]/div/div/div/div/div/div[2]/ul/li[2]/a/span').click()
 
browser.find_element_by_xpath('//*[@id="memorableAnswer"]').send_keys(m_word)
 
pass1 = browser.find_element_by_xpath('//*[@id="hsbcwidget_CharacterChallenge_0"]/div/h4/span[1]').text
pass1 = int(pass1[0])
passcha1 = password[(pass1)-1]
pass2 = browser.find_element_by_xpath('//*[@id="hsbcwidget_CharacterChallenge_0"]/div/h4/span[2]').text
pass2 = (pass2[0])
 
if pass2 ==("s"):
    pass2 = "7"
    passcha2 = password[14]
 
else:
    pass2 = int(pass2)
    passcha2 = password[(pass2)-1]
 
pass3 = browser.find_element_by_xpath('//*[@id="hsbcwidget_CharacterChallenge_0"]/div/h4/span[3]').text
pass3 = (pass3[0])
if pass3 ==("s"):
    pass3 = "7"
    passcha3 = password[14]
elif pass3 ==("l"):
    pass3 = "8"
    passcha3 = password[15]
else:
    pass3 = int(pass3)
    passcha3 = password[(pass3)-1]
 
browser.find_element_by_xpath('//*[@id="pass%s"]' %pass1).send_keys(passcha1)
browser.find_element_by_xpath('//*[@id="pass%s"]' %pass2).send_keys(passcha2)
browser.find_element_by_xpath('//*[@id="pass%s"]' %pass3).send_keys(passcha3)
browser.find_element_by_xpath('//*[@id="dijit_form_Form_0"]/div[3]/div/div/span/input').click()
print ("Retrieving transactions from HSBC...")
time.sleep(10)
balance = browser.find_element_by_xpath('//*[@id="balanceField"]/span[3]').text
browser.find_element_by_xpath('//*[@id="dapViewMoreDownload"]').click()
browser.find_element_by_xpath('//*[@id="$group_gpib_acct_bijit_AccountFilterPayments_0_ofx"]').click()
time.sleep(5)
browser.find_element_by_xpath('//button[text()="Download"]').click()
print ("HSBC Balance: " +balance)
 
time.sleep(5)
browser.quit()
 
username = "######"
password = "######"
passcode = "######"
browser = webdriver.Chrome(chromedriver)
 
print ("Logging into ###### Barclaycard...")
 
#browser.set_window_position(-3000, 0)
browser.get("https://www.barclaycard.co.uk/personal")
time.sleep(5)
browser.get("https://www.barclaycard.co.uk/personal")
 
time.sleep(5)
browser.find_element_by_xpath('/html/body/header/div[1]/div[2]/div[3]/ul/li[1]/a').click()
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').send_keys(passcode)
browser.find_element_by_id('AS6').click()
time.sleep(5)
 
pass1 = browser.find_element_by_id('letter1Answer-label').text
pass1 = int(pass1[0])
pass2 = browser.find_element_by_id('letter2Answer-label').text
pass2 = int(pass2[0])
passcha1 = password[(pass1)-1]
passcha2 = password[(pass2)-1]
 
browser.find_element_by_id('letter1Answer').send_keys(passcha1)
browser.find_element_by_id('letter2Answer').send_keys(passcha2)
 
browser.find_element_by_xpath('//*[@id="btn-login"]/span[1]').click()
 
#print ("Retrieving transactions from ##### Barclaycard...")
time.sleep(5)
browser.get("https://as2r-clb-bcc1-bcol.barclaycard.co.uk/ecom/as2/recentTransactions.do?ref=home-recentTrans")
balance = browser.find_element_by_xpath('//*[@id="contentBody"]/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr/td/strong').text
browser.get("https://as2r-clb-bcc1-bcol.barclaycard.co.uk/ecom/as2/export.do?doAction=processRecentExportTransaction&type=OFX_2_0_2&statementDate=&sortBy=transactionDate&sortType=Dsc")
print ("###### Barclaycard Balance: " +balance)
 
time.sleep(5)
browser.quit()
 
username = "######"
password = "######"
passcode = "######"
browser = webdriver.Chrome(chromedriver)
 
print ("Logging into ###### Barclaycard...")
 
browser.set_window_position(-3000, 0)
browser.get("https://www.barclaycard.co.uk/personal")
time.sleep(5)
browser.get("https://www.barclaycard.co.uk/personal")
 
time.sleep(5)
browser.find_element_by_xpath('/html/body/header/div[1]/div[2]/div[3]/ul/li[1]/a').click()
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').send_keys(passcode)
browser.find_element_by_id('AS6').click()
time.sleep(5)
 
pass1 = browser.find_element_by_id('letter1Answer-label').text
pass1 = int(pass1[0])
pass2 = browser.find_element_by_id('letter2Answer-label').text
pass2 = int(pass2[0])
passcha1 = password[(pass1)-1]
passcha2 = password[(pass2)-1]
 
browser.find_element_by_id('letter1Answer').send_keys(passcha1)
browser.find_element_by_id('letter2Answer').send_keys(passcha2)
 
browser.find_element_by_xpath('//*[@id="btn-login"]/span[1]').click()
 
#print ("Retrieving transactions from ##### Barclaycard...")
time.sleep(5)
browser.get("https://as2r-clb-bcc4-bcol.barclaycard.co.uk/ecom/as2/recentTransactions.do?ref=home-recentTrans")
balance = browser.find_element_by_xpath('//*[@id="contentBody"]/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div/table/tbody/tr/td/strong').text
browser.get("https://as2r-clb-bcc4-bcol.barclaycard.co.uk/ecom/as2/filter.do?doAction=handleLast3MonthsTransactions")
browser.get("https://as2r-clb-bcc1-bcol.barclaycard.co.uk/ecom/as2/export.do?doAction=processRecentExportTransaction&type=OFX_2_0_2&statementDate=&sortBy=transactionDate&sortType=Dsc")
print ("###### Barclaycard Balance: " +balance)
 
time.sleep(5)
browser.quit()
 
import os
import shutil
sourcepath='C:/Users/#####/Downloads'
source = os.listdir(sourcepath)
destinationpath = 'C:/Users/PeterGibson/Downloads/transactions'
for files in source:
    if files.endswith('.ofx'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
 
os.system('pause')