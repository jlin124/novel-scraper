#exit() to quit, if syntax errors
import requests
from bs4 import BeautifulSoup, SoupStrainer
from time import sleep
import json
from tqdm import tqdm
import os

pages = {
    'https://faqwiki.us/the-100th-regression-of-the-max-level-player-chapter-1/',
    'https://translatinotaku.net/novel/the-100th-regression-of-the-max-level-player/rmlp-chapter-1-the-midnight-bell-part-1/'
}


def get_pages():
    print('Getting pages!')
    soup = BeautifulSoup(open('links.txt').read(), features='lxml')

    link = soup.find_all('a', href=True)
    f = open('pg.txt', 'w+', encoding='utf-8')
    for li in link:
        f.write(li.get('href'))
        f.write('\n')
    f.close
    print('I got the goods.\n')


get_pages()

stop = 'Translating'

with open('pg.txt', 'r') as f:
    for page in tqdm(reversed(list(f)), total=291):
        print('\nScraping...')

        #parsing from page
        r = requests.get(page)
        soup = BeautifulSoup(r.content, 'html.parser')

        #extract chapter title/heading
        if soup.find('h1', class_='entry-title'):
            print(soup.find('h1', class_='entry-title').get_text())
            ch = soup.find('h1', class_='entry-title').get_text()
        elif(soup.find('h1', attrs={'id': 'chapter-heading'})):
            print(soup.find('h1', attrs={'id': 'chapter-heading'}).get_text())
            sp = soup.find('h1', attrs={'id': 'chapter-heading'}).get_text().split("- ")
            ch = '100th\\' + sp[1].replace(': ', ' - ') +'.txt'
            print(ch)
        #extract all <p> tagged text
        texts = soup.find_all('p', attrs={'class': None})

        #create file under a certain directory
        os.makedirs(os.path.dirname(ch), exist_ok=True)
        f = open( ch, 'w+', encoding='utf-8')
        f.write('\n\n'+sp[1] + '\n')

        #print lines of text to file
        for text in tqdm(texts, total=len(texts)-10):
            if(stop in text.get_text()):
                break
            f.write(text.get_text() + "\n")
            sleep(0.01)
        f.close
        print('Done\n')

