
## <center> **Volume 2** </center>

### **Regular Expressions**

To use regular expressions in Python, we need to `import` the `re` library. Here are some useful functions:

`re.findall(regexp, s)`         return the list of substrings that match `regexp` or match groups defined in it  
`re.split(regexp, s)`           return `s` split into list by `regexp`  
`re.sub(regexp, repl, s)`       substitute all substrings in `s` that match `regexp` with `repl` and return the resulting string  
`re.search(regexp, s)`          check if `regexp` is in `s`; returns `None` if it isn't  
`re.search(regexp, s).span()`    return the indeces of the first match  
`re.search(regexp, s).group()`   return the first matched string  
`re.match(regexp, s)`           check if `regexp` matches `s`; returns `None` if it doesn't

For example:

```python
import re
my_string = "She sells seashells by the seashore."
re.findall(r"\bsea\w+", my_string)
```
>['seashells', 'seashore']

You must have noticed the letter `r` in front of regular expressions in the examples above. This is an indicator that says that you don't have to screen every slash used in the expression. Compare: `re.findall(r"\bsea\w+", my_string)` is the same as `re.findall("\\bsea\\w+", my_string)`.


```python
re.findall(r"\b((sea)\w+)", my_string)
```
>[('seashells', 'sea'), ('seashore', 'sea')]

```python
re.sub(r"[auioe]", "^", my_string)
```
>'Sh^ s^lls s^^sh^lls by th^ s^^sh^r^.'


```python
re.sub(r"(\w+) and (\w+)", r"\2 and \1", "Jack and Jill")
```
>'Jill and Jack'

The `re.search()` method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

If the search is successful, `re.search()` returns a match object; if not, it returns None.

```python
import re
string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search(r"^(?i)python\b", string)

if match:
  print("Pattern found inside the string")
else:
  print("Pattern not found")  

```
>Pattern found inside the string

```python
my_string = re.search(r"(\w+) (\w+)", "Isaac Newton, physicist")
my_string.group(2) 
```
>'Newton'


```python
my_string.group(1) 
```
>'Isaac'

Example: write a regular expression to extract all adjectives from the **tagged corpus** that end with "ing" and contain a hyphen (e.g., "good-looking").

```python
import re

with open("data/tagged.txt", "r") as input_file:
    input_file = input_file.read()
print(input_file[:189])
print(re.findall(regex, input_file))
```
> What_WP is_VBZ the_DT highest_JJS Roman_NNP numeral_NN ?_.
>
>What_WP 's_VBZ the_DT most_RBS popular_JJ form_NN of_IN bridge_NN ?_.
>
> Who_WP was_VBD the_DT inventor_NN of_IN the_DT stove_NN ?_.

### **Scraping time!**

There often appears a need to parse a web page in order to obtain information from it. Suppose you need to get the list of American Presidents from https://www.presidentsusa.net/vicepresidents.html. It's really inconvenient just to copy it from the page - you'll have to remove the Vice Presidents and the numbers at the beginning of each Vice President name.

Before we start: **Be NICE to the servers; you DON’T want to crash a website.**


```python
import requests
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
content = web_page.content
print(web_page)
print(content[:60])
```

>\<Response [200]\>
>
> b'\xef\xbb\xbf\<!doctype html\>\r\n\<html class="no-js" lang="en"\>\r\n  \<head\>'

But in this way our Presidents are hidden inside the HTML annotation. We'll have to clean it to get to the information - not very handy, again. To clean the HTML annotation, you can use the [lxml.html library](http://lxml.de/lxmlhtml.html):

```python
from lxml import html
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
only_text = html.fromstring(web_page.content).text_content()
print("Text: ", only_text[:70])
```
>Text:  
>
>
>   Vice Presidents of the United States  

...or we can use the [BeautifulSoup library](http://www.crummy.com/software/BeautifulSoup/)

```python
from bs4 import BeautifulSoup
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
content = web_page.content
raw = BeautifulSoup(content, "lxml").get_text()
raw[:45]
```
>'\n\n\n\n\nVice Presidents of the United States\n\n\n\n'

In this way, the result is also of the type string, so you'll have to extract the necessary data using regular expressions, for example, but it could still take time.

The best and the most recommended way to work with HTML-pages is to read them as trees. The `Requests` and `lxml` libraries will help us do that:

```python
import requests
from lxml import html
# get the page using requests
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
# read the html-tree from the text of the page
tree = html.fromstring(web_page.text)
# get the necessary elements
presidents = tree.xpath('//tr/td[4]/b/a')

print(presidents[-9:])
```
>[<Element a at 0x1136cab38>, <Element a at 0x1136cab88>, <Element a at 0x1136cabd8>, <Element a at 0x1136cac28>, <Element a at 0x1136cac78>, <Element a at 0x1136cacc8>, <Element a at 0x1136cad18>, <Element a at 0x1136cad68>, <Element a at 0x1136cadb8>]


When you directly want to access a content of the node use `text()`

```python
presidents = tree.xpath('//tr/td[4]/b/a/text()')
print(presidents[-9:])
```
>['Gerald Ford', 'Gerald Ford', 'Jimmy Carter', 'Ronald Reagan', 'George Bush', 'Bill Clinton', 'George W. Bush', 'Barack Obama', 'Donald Trump']

`tree.xpath('//tr/td[4]/b/a/text()')` gets the text (`text()`) of the link (tag <`a`>) in every fourth column (`td[4]`) of every row (`tr`) of the table on our html page. You can write such structures easily after inspecting the source of the web-page.

This is how we get our Presidents clean and ready to be used. You can find all necessary details on Requests, lxml and XPath at http://docs.python-guide.org/en/latest/scenarios/scrape/

#### **Xpath**

XPath stands for XML Path Language. It uses a non-XML syntax to provide a flexible way of addressing (pointing to) different parts of an XML document. It can also be used to test addressed nodes within a document to determine whether they match a pattern or not.

```python
//article         # find all <article> tags
//article/h1      # find all <h1> tags directly below an <article>
//a/@href         # find all href attributes of <a> tags
//span[@class='someclass']        # find all <span> with class set to 'someclass'
//input[@class='someclass' and @name='searchtext']   # find by multiple attributes
//a[contains(@href, 'https')]       # Get all HTTPS links
//a[not(contains(@href, 'https')]   # Get all non-HTTPS links
//a[starts-with(@href, '/blog')]    # checks whether the first string starts with the second string
```

You can find more Xpath examples [here.](https://gist.github.com/LeCoupa/8c305ec8c713aad07b14)

We can extract links as well:

```python
import requests
from lxml import html
# get the page using requests
web_page = requests.get("https://www.presidentsusa.net/vicepresidents.html")
# read the html-tree from the text of the page
tree = html.fromstring(web_page.text)
presidents_links = tree.xpath('//tr/td[4]/b/a/@href')
presidents_links[:5]
```
>['washington.html', 'jadams.html', 'jefferson.html', 'jefferson.html', 'madison.html']

#### Is there a better way to edit, extract and evaluate XPath queries?

The short aswer is yes ([XPath Helper for Chrome](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl))

```python
import requests
from lxml import html
web_page = requests.get("https://hotline.ua/mobile-mobilnye-telefony-i-smartfony/samsung-galaxy-s7-edge-32gb-black/discussion/", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'})
tree = html.fromstring(web_page.text)
do_like = tree.xpath(xpath)
print(do_like)
do_not_like = tree.xpath(xpath)
print(do_not_like)
```

**NB!** Important detail to verify: the robots.txt file, which can be found at the root of the website and which states what is allowed to be scraped or not. For example, here is the file for the Lowcostavia website: http://lowcostavia.com.ua/robots.txt

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
```

###  **More Advanced scraping tricks**

These aren’t really things you’ll need if you’re building a simple, small scale scraper for 90% of websites. But they’re useful tricks to keep up your sleeve.

**Delays and Backing Off**

Be polite and not overwhelm the target site you’re scraping, you can introduce an intentional delay or lag in your scraper to slow it down

```python
import time

for item in ["page/1/", "page/2/", "page/3/"]:
    r = requests.get("http://example.com/" + item)
    print(item)
    time.sleep(5)  # wait 5 seconds before we make the next request
```

**Handling Network Errors**

Just as you should never trust user input in web applications, you shouldn’t trust the network to behave well on large web scraping projects. Eventually you’ll hit closed connections, SSL errors or other intermittent failures.

```python
try:
    requests.get("http://example.com")
except requests.exceptions.RequestException:
    pass  # handle the exception. maybe wait and try again later
```

You can inspect **exceptions handling** on your own using [the examples here](https://www.tutorialspoint.com/python/python_exceptions.htm).

**Setting Timeouts**

If you’re experiencing slow connections and would prefer that your scraper moved on to something else, you can specify a timeout on your requests.

```python
try:
    # wait up to 10 seconds
    requests.get("http://example.com", timeout=10) 
except requests.exceptions.Timeout:
    pass  # handle the timeout
```

#### **The importance of the User-Agent**

Everytime you visit a website, it gets your browser information via user agent. Some websites won’t show you any content unless you provide a user agent. Also, some sites offer different content to different browsers. Websites do not want to block genuine users but you would look suspicious if you send 200 requests/second with the same user agent. A way out might be either to generate (almost) random user agent using [User_agent module](https://pypi.org/project/user_agent/) or to set one yourself.


```python
import requests
web_page = requests.get("http://lowcostavia.com.ua/")
print(web_page)
print(web_page.content[:70])
```
>\<Response [424]\>
>
>b'\<!doctype html\>\n\<html\>\n\<head\>\n    \<title\>424 Failed Dependency\</title\>'

```python
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
print(headers)
```
>{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)'}

```python
web_page = requests.get("http://lowcostavia.com.ua/", headers=headers)
print(web_page)
```
>\<Response [200]\>

```python
from lxml import html
tree = html.fromstring(web_page.text)
headlines = tree.xpath("//article//h2[@class='post-title']/a//text()")
print(headlines[:5])
```
>['35% знижки на авіаквитки від Qatar Airways! Кувейт, Маскат, Токіо, Сеул від €461 у два боки!', 'Kiwi – найкращий пошук дешевих авіаквитків лоукост авіакомпаній. Нові можливості!', 'Авіаквитки з України у Фінляндію від €61 у два боки!', 'Літній розпродаж від A&O – хостели від €9!', 'Гарячі дешеві тури в Туреччину з Києва на 7 ночей від €173 за одного!']


**IP Rotation**

Even if you randomize your user agent, all your requests will be from the same IP address. That doesn’t sound abnormal because libraries, universities, and also companies have only a few IP addresses. However, if there are uncommonly many requests coming from a single IP address, a server can detect it. 

Using [shared proxies](https://free-proxy-list.net/), VPNs or TOR can help you become a ghost ;).
```python
proxies = {'http' : 'http://10.10.0.0:0000',  
          'https': 'http://120.10.0.0:0000'}
page_response = requests.get(page_link, proxies=proxies, timeout=5
```
By using a shared proxy, the website will see the IP address of the proxy server and not yours. A VPN connects you to another network and the IP address of the VPN provider will be sent to the website.

**Sessions and Cookies**

While HTTP is stateless, sometimes you want to use cookies to identify yourself consistently across requests to the site you’re scraping.

The most common example of this is needing to login to a site in order to access protected pages. Without the correct cookies sent, a request to the URL will likely be redirected to a login form or presented with an error response.

```python
# create a session
import requests
session = requests.Session()

# make a login POST request, using the session
session.post("http://example.com/login", data=dict(email="me@domain.com", password="secret_value"))

# subsequent requests that use the session will automatically handle cookies
r = session.get("http://example.com/protected_page")
```

Again, do not overload the website by sending hundreds of requests per second!

### **Scripting**

In computer programming, a script is usually a rather short program containing a sequence of rather simple instructions. You usually write it once and then run it when you need it. Often you would want to run a script from the Terminal. Let us see how it's done. Here is [an example of a script](data/is_valid_password.py).

A Python module usually begins with a group of comment lines giving a one-line title of the module and identifying the author:

```python
## Password Check Example
## By Mariana Romanyshyn
```

If the code is distributed, it also includes the URL where the code is available, a copyright statement, and license information.

Next is the module-level docstring, a triple-quoted multiline string containing information about the module that will be printed when someone types `help(the_name_of_the_module)`:

```python
"""
Password Check.

Check if the password satisfies the following requirements:
- A password must have at least eight characters (letters, numbers or underscores), and its length must be divisible by four.
- A password must have an underscore every three characters.
- A password must contain exactly two digits.
- A password must contain exactly two capitalized letters.

The password must be a string.

"""
```

After this come all `import` statements, then global variables, followed by function definitions that make up most of the module:

```python
import sys, re

def has_underscore(password):
    return re.match(r"([a-zA-Z\d]{3}_)+", password)

def is_valid_password(password):
    """Check if the password is valid."""
    if len(password) > 7 and has_underscore(password):
        cap, num = 0, 0
        for i in password:
            if i.isupper():
                cap += 1
            elif i.isdigit():
                num += 1
        if cap == 2 and num == 2:
            return True
    return False
```

The main part of the module - the sequence of actions to be executed when called from the Terminal - is usually stated under `if __name__ == '__main__':`. "Why do we need that?" you will ask. The main reason is that if you don't use this condition and decide to import a function from this module at a certain point of time, you will not only import the functions, but will have your code executed.

```python
if __name__ == '__main__':
    # execute only if run as a script
    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " \"<password>\""
    else:
        if is_valid_password(sys.argv[1]):
            print "The password " + sys.argv[1] + " is valid."
        else:
            print "The password " + sys.argv[1] + " is invalid."
```

Let us look closer at `sys.argv` used in the code above. The `sys` (System-specific parameters and functions) library (that also has to be imported) allows you to get arguments from the Terminal. `sys.argv` is the list of arguments that you type in after calling Python. Everything you type in terminal is read as a string and is then split by spaces. This is how `sys.argv` becomes a list. Thus, `sys.argv[0]` will be the name of your module. `sys.argv[1]` will be the password that you want to check.

If you ever need an argument to be a number, you will still have to read it from the string, e.g., `int(sys.argv[1])`.

Now you can test your program in the Terminal. Note that you either have to go to the folder containing your script or state its address:

`$ python is_valid_password.py "hG3_n5T_ghy_"`
"The password is valid."

`$ python is_valid_password.py "hG3_n5T_ghy__"`
"The password is invalid."

`$ python is_valid_password.py`
Usage: "`is_valid_password.py <password>`"

**NB!** Windows users will have to call python using its whole address, for example, `C:\\Python27\\python.exe`.

### **Bibliography**

1. Python 3.6 documentation, available at https://docs.python.org/3.6/
2. Regular expression operations available at https://docs.python.org/3/library/re.html
3. HTML Scraping, available at http://docs.python-guide.org/en/latest/scenarios/scrape/
4. More information about Xpath available at https://www.w3schools.com/xml/xpath_intro.asp
