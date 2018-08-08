# encoding:utf-8
from bs4 import BeautifulSoup

def parse_html(html):
    print(html)
    soup = BeautifulSoup(html)
    movie_list_soup =  soup.find('ol',attrs={'class':'grid_view'})
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div',attrs={'class':'hd'})
        movie_name = detail.find('span',attrs={'class':'title'}).getText()
        print(movie_name)