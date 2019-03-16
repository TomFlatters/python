from bs4 import BeautifulSoup as bs;
import requests;
import sys;

word = sys.argv[1]

try:
    r = requests.get("https://www.dictionary.com/browse/"+word)
    soup = bs(r.content, 'lxml')

    pos = soup.findAll("span", {"class":"luna-pos"})
    defs = soup.findAll("div", {"class":"css-1o58fj8 e1hk9ate4"})

    meanings = defs[0].findChildren("div")

    print("Part of speech: " + pos[0].text)
    print("Meanings: ")

    for (i, meaning) in enumerate(meanings):
        print(str(i+1) + ")" + meaning.text)


except:
    print("Word not found! Have you made a typo?")




