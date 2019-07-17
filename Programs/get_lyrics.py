# Scraping lyrics, works from terminal
import requests
from lxml import html
import sys

def get_lyrics(link, output_file):
    web_page = requests.get(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'})
    tree = html.fromstring(web_page.text)
    links = tree.xpath("//a[contains(@href, '/lyric/')]/@href")
    with open(output_file, 'w') as f:
        f.write("\n#########\n")
    with open(output_file, 'a', encoding="utf-8") as f:
        for item in links:
            web_page = requests.get("https://www.lyrics.com{}".format(item), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'})
            tree = html.fromstring(web_page.text)
            song = tree.xpath("//pre/text()")
            song = "".join(song)
            f.write(song)
            f.write("\n#########\n")

if __name__ == '__main__':
    get_lyrics(sys.argv[1], sys.argv[2])
