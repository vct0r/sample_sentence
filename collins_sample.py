# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
def sample_collector(word):

    url = 'https://www.collinsdictionary.com/dictionary/english/' + word

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = word

    sample = soup.select("div.quote")[0].get_text()

    print(title + ':\n' + sample)


word = raw_input('input your word：')

sample_collector(word)
