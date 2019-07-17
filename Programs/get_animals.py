# Scraping lists of animals, works from terminal
import requests
from lxml import html
import sys

def get_animals(link1, link2):
    web_page = requests.get(link1, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'})
    tree = html.fromstring(web_page.text)
    animals1 = set(tree.xpath("//div[@class='letter']//ul//li//b/text()"))
    web_page = requests.get(link2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'})
    tree = html.fromstring(web_page.text)
    animals2 = set(tree.xpath("//td/p/a/text()"))
    animals = animals1.union(animals2)
    input = []
    for el in animals:
        el = el.lower()
        if el.count(",") > 0:
            el = el[:el.index(",")]
            input.append(el)
        elif el.count(" ") > 0:
            del el
        else:
            input.append(el)
    with open("Unique_animal_names.txt", 'w', encoding="utf-8") as f:
        for el in sorted(list(set(input))):
            f.write(el)
            f.write("\n")

if __name__ == '__main__':
    get_animals(sys.argv[1], sys.argv[2])
