# v1.0 Initial Release
# v1.1 Now it saves into one file + the ISINs


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.request



print("""
___  ____ _  _ ____ _  _ ____ _ _  _ _  _ ____ ____ ___                       
|  \ |__| |\ | [__  |_/  |___ | |\ | |  | |___ [__   |                        
|__/ |  | | \| ___] | \_ |___ | | \|  \/  |___ ___]  |                        
                                                                              
 ___  ____     ___  _  _     ____ _     _    _  _     _  _ ____     ____ ____ 
 |  \ |___     |  \ |_/      |___ |     |    |  |     |\ | |  |     [__  |___ 
.|__/ |___    .|__/ | \_    .|    |    .|___ |__|    .| \| |__|    .___] |___ 
                                                                              
___ _  _ ____    ___  ____ _ _ _ _  _ _    ____ ____ ___  ____ ____           
 |  |\ | |__|    |  \ |  | | | | |\ | |    |  | |__| |  \ |___ |__/           
 |  | \| |  |    |__/ |__| |_|_| | \| |___ |__| |  | |__/ |___ |  \           
                                                                      
 v.1.1 by tamas.fabian@dealogic.com
 last updated on:      Feb-02-2019
 initially created on: Jan-31-2019
""")

# THIS IS THE DE PART

header_counter = 1
de_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=117"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=117&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=117&p_nFund=" + id

	full_link_for_source = "https://www.danskeinvest.de/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id
	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	de_counter = de_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".de" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".de | Scraping " + fundname_text + " is done!")
	
	
print("")
print("I have successfully saved info for: " + str((de_counter)) + " funds' TNA from the .de page.")
print("")

# THIS IS THE END OF THE DE PART

# THIS IS THE DK PART

header_counter = 1
dk_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=75"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.dk/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	dk_counter = dk_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".dk" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".dk | Scraping " + fundname_text + " is done!")
	
	
	
print("")
print("I have successfully saved info for: " + str((dk_counter)) + " funds' TNA from the .dk page.")
print("")

# THIS IS THE END OF THE DK PART

# THIS IS THE DK2 PART

header_counter = 1
dk2_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=31"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.dk/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	dk2_counter = dk2_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".dk" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".dk | Scraping " + fundname_text + " is done!")
	
	
	
print("")
print("I have successfully saved info for: " + str((dk2_counter)) + " funds' TNA from the .dk page.")
print("")


# THIS IS THE END OF THE DK2 PART

# THIS IS THE DK3 PART

header_counter = 1
dk3_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=66"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.dk/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	dk3_counter = dk3_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".se" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".dk | Scraping " + fundname_text + " is done!")
	
	
	
print("")
print("I have successfully saved info for: " + str((dk3_counter)) + " funds' TNA from the .dk page.")
print("")

# THIS IS THE END OF THE DK3 PART

# THIS IS THE DK4 PART

header_counter = 1
dk4_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=32"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=75&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.dk/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	dk4_counter = dk4_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".se" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".dk | Scraping " + fundname_text + " is done!")
	
	
	
print("")
print("I have successfully saved info for: " + str((dk4_counter)) + " funds' TNA from the .dk page.")
print("")

# THIS IS THE END DK4 PART


# THIS IS THE FI PART

my_url = "https://www.danskeinvest.fi/web/show_page.prices_return?p_nId=61&p_nFundGroup=61&p_nTab=2"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")
fund_list_table = page_soup.find("div", {"class":"fundvaelger"})

list_counter = 1

fund_list = fund_list_table.findAll("option")
fund_counter = len(fund_list)

while fund_counter > list_counter: 
	fund_from_list = fund_list[list_counter]
	fund_list_text = fund_from_list.text.replace(",", "").strip()
	
	fund_link_from_list = fund_list[list_counter]
	fund_link_text = fund_link_from_list["value"]
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?" + fund_link_text 
	
	
	full_link_for_nav_text = "https://www.danskeinvest.fi/web/show_fund.stamdata?" + fund_link_text
	
	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	
	isin_locate = page_soup_NAV.find("table", {"id":"stamdataTabel"})
	isin_selector = isin_locate.find("td", {"class":"tTop tleftbold tOdd bordered_last"})
	isin_text = isin_selector.text.replace(",", "").strip()
	
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if list_counter == 1:
		f.write(headers)
	f.write(".fi" + "," + fund_list_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_name_text + "\n")
	
	print(".fi | Scraping " + fund_list_text + " is done!")
	
	list_counter = list_counter + 1


print("")
print("I have successfully saved info for: " + str((len(fund_list))) + " funds' TNA from the .fi page.")
print("")

fi_counter = len(fund_list)

# THIS IS THE END OF THE FI PART

# THIS IS THE LU PART

header_counter = 1
lu_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=81"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=81&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=81&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.lu/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	lu_counter = lu_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".lu" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".lu | Scraping " + fundname_text + " is done!")
	
	
	
print("")
print("I have successfully saved info for: " + str(lu_counter) + " funds' TNA from the .lu page.")
print("")

# THIS IS THE END OF THE LU PART

# THIS IS THE NO PART

header_counter = 1
no_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=90"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=90&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=90&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.no/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	no_counter = no_counter + 1 
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".no" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".no | Scraping " + fundname_text + " is done!")
	
	
print("")
print("I have successfully saved info for: " + str((no_counter)) + " funds' TNA from the .no page.")
print("")

# THIS IS THE END OF THE NO PART

# THIS IS THE NO 2 PART

header_counter = 1
no2_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=89"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=90&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=90&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.no/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	no2_counter = no2_counter + 1 
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".no" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".no | Scraping " + fundname_text + " is done!")
	
	
print("")
print("I have successfully saved info for: " + str((no2_counter)) + " funds' TNA from the .no page.")
print("")
	

# THIS IS THE END OF THE NO 2 PART

# THIS IS THE SE PART

header_counter = 1
se_counter = 0

my_url = "https://www.danskeinvest.lu/w/show_list.products?p_nId=1181&p_nFundGroup=74"

# This needed for some pages against the 403 error
req = urllib.request.Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = urllib.request.urlopen(req).read()

# We first locate all Fund's name and link
page_soup = soup(page_html, "html.parser")

fund_list_table = page_soup.tbody


containers = fund_list_table.findAll('tr', {"class":"table-data product-element js-label"})


for container in containers:
	id = container["id"]
	fundname = container.findAll("span", {"class":"headline-text"})
	fundname_text = fundname[0].text.replace(",", "").strip()
	isin_locate = container.findAll("td", {"class":"table-data-value"})
	isin_text = isin_locate[0].text.replace(",", "").strip()
	
	
	full_link_for_name_text = "https://www.danskeinvest.fi/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id
	
	full_link_for_nav_text = "https://www.danskeinvest.lu/web/show_fund.stamdata?p_nId=1181&p_nFundgroup=74&p_nFund=" + id
	
	full_link_for_source = "https://www.danskeinvest.se/web/show_fund.produkt?p_nId=1181&p_nFundgroup=74&p_nFund=" + id

	
	# Get the NAV for each Fund
	my_url_02 = str(full_link_for_nav_text)
	req = urllib.request.Request(my_url_02, headers={'User-Agent': 'Mozilla/5.0'})
	page_html_NAV = urllib.request.urlopen(req).read()
	page_soup_NAV = soup(page_html_NAV, "html.parser")
	fund_NAV_list = page_soup_NAV.find("table", {"id":"dagenstalTabel"})
	
	
	
	#for nav_info in fund_NAV_list:
	NAV_four_info = fund_NAV_list.findAll("tr")
		
	NAV_four_info_TA_date = fund_NAV_list.find("td", {"class":"tTop tleft tOdd"})
	NAV_four_info_TA_val = fund_NAV_list.find("td", {"class":"tTop trightbold tOdd bordered_last"})
	NAV_four_info_NAV_date = fund_NAV_list.find("td", {"class":"tTop tleft tEven"})
	NAV_four_info_NAV_val = fund_NAV_list.find("td", {"class":"tTop trightbold tEven bordered_last"})
		
	TA_date = NAV_four_info_TA_date
	try:
		TA_date_text = TA_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	TA_val = NAV_four_info_TA_val
	try:
		TA_val_text = TA_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_date = NAV_four_info_NAV_date
	try:
		NAV_date_text = NAV_date.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
		
	NAV_val = NAV_four_info_NAV_val
	try:
		NAV_val_text = NAV_val.text.replace(",", "").strip()
	except:
		TA_date_text = "NO INFO ON WEBSITE"
	
	se_counter = se_counter + 1
	
	filename = "DanskeInvest.csv"
	f = open(filename, "a", encoding="utf-8")
	headers = "site, Fund_Name, ISIN, NAV_date, NAV_val, TA_date, TA_val, Fund_Link\n"
	if header_counter == 1:
		f.write(headers)
	f.write(".se" + "," + fundname_text + "," + isin_text + "," + NAV_date_text + "," + NAV_val_text + "," + TA_date_text + "," + TA_val_text + "," + full_link_for_source + "\n")
	header_counter = header_counter - 1
	
	print(".se | Scraping " + fundname_text + " is done!")
	
	
	
print("")
print("I have successfully saved info for: " + str((se_counter)) + " funds' TNA from the .se page.")
print("")

# THIS IS THE END OF THE SE PART

# SUMMARY

total_funds = de_counter + dk_counter + dk2_counter + dk3_counter + dk4_counter + fi_counter + lu_counter + no_counter + no2_counter + se_counter

print("")
print("I have successfully saved info for a total of: " + str(total_funds) + " funds' TNA from the pages.")
print("")

