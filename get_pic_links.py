import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

hashtag = input('Enter hashtag for pictures: ')
url = 'https://pixabay.com/en/photos/{}/?image_type=photo&amp;order=latest&amp;orientation=vertical&amp;pagi=1'.format(hashtag)

# Get HTML
def get_html(url):
    r = requests.get(url)
    return r.text

# Get the number of pages for hashtag
def number_of_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    for items in soup.find_all('div',{'class':'paginator'}):
        str = items.text
        #extract only number from code
        number_of_pages = [int(n) for n in str.split() if n.isdigit()]
        return number_of_pages[0]

# Get all links from one page
def pic_links(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div',{'class':'item'})
    links = []
    for item in items:
        a = item.find('a').get('href')
        link = 'https://pixabay.com' + a
        links.append(link)
    return links

# get all pages url
def pages_url(number_of_pages):
    pages_url = []
    while number_of_pages > 0:
        url = 'https://pixabay.com/en/photos/{}/?image_type=photo&amp;order=latest&amp;orientation=vertical&amp;pagi='.format(hashtag)
        url = link + str(number_of_pages)
        pages_url.append(url)
        number_of_pages -=1
    return pages_url

# Append links in file
def write_csv(pics_links):
    file = 'Pixabay_pics_{}.txt'.format(hashtag)
    with open (file,'a') as f:
        for i in pics_links:
            f.write(i+'\n')

def main():
    count = 0
    start = datetime.now()
    n = number_of_pages(get_html(url))
    for i in pages_url(n):
        count += 1
        start_iteration = datetime.now()
        write_csv(pic_links(get_html(i)))
        end_iteration = datetime.now()
        diff = end_iteration - start_iteration
        print ('{} For page {}/{}'.format(diff, count, n))
    total = datetime.now()
    print('Total time: {}'.format(total-start))

if __name__ == '__main__':
    main()
