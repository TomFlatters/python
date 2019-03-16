# new imports:
import bs4 as bs
import pickle       # so you can save objects
import requests    

def save_ftse250_tickers():
    resp = requests.get("https://en.wikipedia.org/wiki/FTSE_250_Index")
    soup = bs.BeautifulSoup(resp.text, 'lxml')       # the text of the source code
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        tickers.append(ticker[:-1])         # remove the "\n" at the end of each row (it's a new line)

    with open("ftse250tickers.pickle","wb") as f:
        pickle.dump(tickers, f)
    
    print(tickers)
    
    return tickers

save_ftse250_tickers()      # save the ftse 250 tickers into a pickle file