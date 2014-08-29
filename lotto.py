from lxml import html
import requests
from twilio.rest import TwilioRestClient 

#Referenced: http://docs.python-guide.org/en/latest/scenarios/scrape/#html-scraping
 
# Twilio Auth 
ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxx" 
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxx" 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
#Scrape the website
#Note: XPath is used to navigate through elements 
#and attributes in an XML document.
page = requests.get('http://www.calottery.com/play/draw-games/powerball/winning-numbers')
tree = html.fromstring(page.text)
date = tree.xpath('//span[@id="objBody_content_0_pagecontent_0_objPastWinningNumbers_rptPast_ctl01_lblDrawDateNumber"]/text()')
lotto_5 = tree.xpath('//td/span/text()')
powerball = tree.xpath('//td[@class="center"]/text()')

print html.fromstring(page.txt)
#Format the info grab the first five loto
lotto_number=' '.join(lotto_5[:5]) + ' and powerball: ' + powerball[0]
current_date=''.join(date)

'''
#Send SMS to Grandma
client.messages.create(
	to="1-555-555-5555", 
	from_="+1650XXXXXXX", 
	body= 'Hi Grandma! ' + current_date +': '+lotto_number , 
)
'''