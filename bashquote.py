import lxml
import requests
from bs4 import BeautifulSoup
from random import randint

def getPage(url):
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    headers = {'User-Agent': useragent}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup

def getScore(y):
    #If the score is positive or negative, this will effect the colour of the text
    #So if we need to get the text, we need to know what colour it is
    colourString = "green"
    startingLength = 20
    if (y.find("<font color=\"green\">")) == -1:
        colourString = "red"
        startingLength = 18

    if colourString == "green":
        start = y.find("<font color=\"green\">")
    else:
        start = y.find("<font color=\"red\">")
    y = y[start:]

    end = y.find("</font>")
    y = y[startingLength:end]
    return y

def getID(y):
    y = y[27:]
    y = y[:y.find("\"")]
    return y

soup = getPage('http://bash.org/?random')

#http://bash.org/?random sorts the random entries by ID, so you will only get very early entries if you pick the first entry from the random page
#As such, we pick a random entry from the random page
randomQuoteNumber = randint(0,49) #50 entries in the page
quote = str(soup.find_all(class_="qt")[randomQuoteNumber])
quoteData = str(soup.find_all(class_="quote")[randomQuoteNumber])


#quote = str(soup.find(class_="qt"))
#quoteData = str(soup.find(class_="quote"))

score = getScore(quoteData)
quoteID = getID(quoteData)

quote = quote.replace("<p class=\"qt\">",'')
quote = quote.replace("&lt;",'<')
quote = quote.replace("&gt;",'>')
quote = quote.replace("</p>",'')
quote = quote.replace("<br/>",'')

print("Quote ID:", quoteID,"- Score:", score)
print(quote)

