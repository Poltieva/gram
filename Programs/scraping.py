# Scraping practice
import requests
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
content = web_page.content
print(web_page)
print(content[:60])

from lxml import html
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
only_text = html.fromstring(web_page.content).text_content()
print("Text: ", only_text[:70])
# prints like on the site
import requests
from lxml import html
# get the page using requests
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
# read the html-tree from the text of the page
tree = html.fromstring(web_page.text)
# get the necessary elements
presidents = tree.xpath('//tr/td[4]/b/a/text()')

print(presidents[-9:])
# Xpath Helper for Chrome

import requests
from lxml import html
web_page = requests.get("https://hotline.ua/mobile-mobilnye-telefony-i-smartfony/samsung-galaxy-s7-edge-32gb-black/discussion/", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'})
tree = html.fromstring(web_page.text)
do_like = tree.xpath('//div[@class="cell-9 cell-sm"][1]/p/text()')
for elem in do_like:
    print(elem)
#do_not_like = tree.xpath(xpath)
#print(do_not_like)

