# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
def webster_sample(word):

    url = 'https://www.merriam-webster.com/dictionary/' + word

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = word

    sample = soup.select("article div div div div ol li p em.vi")[0].get_text()

    print('merriam-webster: ' + sample)

def cambridge_sample(word):
    
    url = 'http://dictionary.cambridge.org/us/dictionary/english/' + word

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = word

    sample = soup.select("span div span.eg")[0].get_text()

    print('cambridge: ' + sample)

def iciba_sample(word):

    url = 'http://www.iciba.com/' + word

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = word

    sample = soup.select("div.sentence-item p.family-english span")[0].get_text()

    print('iciba: ' + sample)


def sample_collector(word):

    print(word + ':')
    iciba_sample(word)
    webster_sample(word)
    cambridge_sample(word)
    print('\n')

for i in range(10):

    word = raw_input('input your word：')

    if word == 'exit':
        break

    sample_collector(word)

