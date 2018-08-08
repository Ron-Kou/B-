# encoding:utf-8
import requests
import os
from HtmlParser import parse_html
import shutil
import configparser


URL = 'http://api.bilibili.com/x/web-interface/search/type'
# URL = 'http://movie.douban.com/top250/'

# https: // www.bilibili.com / video / av28351489

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }


def human_request():
    # https: // www.bilibili.com / video / av28351489
    respone = requests.get(URL,headers=HEADERS,params={'jsonp': 'jsonp',
                                                       'search_type': 'video',
                                                       'highlight': 1,
                                                       'keyword': '爱做饭的芋头SAMA',
                                                       'page': 4,
                                                       'callback': '__jp2'})
    # print(respone.content.decode('utf-8'))
    return respone

def foo():
    print("a")


if __name__ == '__main__':

    #
    #
    # open(os.getcwd() + '/resources/config/config.properties','w').write('[position]\n'+'\n'.join(config.options('position')))
    # print(str(config.items()))

    dir = os.getcwd() + '/resources/danmu/all/'
    for file in os.listdir(dir):
        print(str(file) + " deleted")
        if file.split('.')[1] == 'xml':
            print(True)
        else:
            print(False)






