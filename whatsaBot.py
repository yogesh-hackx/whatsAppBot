from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

input("Scan QR press enter if scanned \n")

print("Select a Contact from recents, or Enter 'c' to select from contact list: \n")

recents = []
sNo = 1
for i in (driver.find_elements_by_xpath('//span[@class = "_19RFN"]')):
	recents.append(i.text)
	print(str(sNo)+" "+i.text)
	sNo += 1

option = input("\n") - 1

user = (driver.find_elements_by_xpath('//span[@class = "_19RFN"]'))[option]
user.click()