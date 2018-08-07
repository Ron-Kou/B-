# encoding:utf-8
from lxml import etree
import re
import requests
import os
import datetime
from XmlParser import parse


def save_xml(xml_path, av,up_name):
    xml = requests.get(xml_path)
    xml_string = xml.content.decode('utf-8')

    file = open(os.getcwd() + '/resources/danmu/'+up_name+'-danmu-' + av + '.xml', 'w')
    try:
        file.write(xml_string)
    finally:
        file.close()
    return 1

def get_danmu(av,up_name):
    # av = "28351489"
    url = "http://www.bilibili.com/video/av" + av
    page = requests.get(url)
    # print(page.headers)
    match = re.search(r'cid=(\d+)', page.text)
    if match:
        cid = match.group(1)
    else:
        return 0
    xml_path = "http://comment.bilibili.tv/{0}.xml".format(cid)

    return save_xml(xml_path, av,up_name)


def get_avs(name):
    av_list = open(os.getcwd() + '/resources/ups/' + name + '/list.txt', 'r')
    set = []
    try:
        list = av_list.read()
        set = list.replace("\n","").split(',')
    finally:
        av_list.close()
    return set


# 暂时没有实现
def save_list_keyword(up_name):
    url = 'http://search.bilibili.com/all?keyword='+up_name
    space_id = ''

    # 待开发
    # page = requests.get(url)
    # print(page.text)
    # # space.bilibili.com/17409016?from=search&seid=5317788543038004355"
    # match = re.search(r'space.bilibili.com//(\d+)\?from=search', page.text)
    # if match:
    #     space_id = match.group(1)
    #     print("yes,space id is "+space_id)
    # else:
    #     print("sorry")
    #     return 0

    space_id = '17409016'
    page_count = 1
    space_url = 'http://space.bilibili.com/'+space_id+'/#/video?tid=0&page=1&keyword=&order=pubdate'
    page = requests.get(space_url)
    print(page.text)
    # match = re.search(r'space.bilibili.com//(\d+)\?from=search', page.text)






if __name__ == '__main__':
    # 根据up名称得到视频id列表
    # up_name = '爱做饭的芋头SAMA' # 芋头大人
    # save_list_keyword(up_name)

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    print(nowTime)


    # step1: save danmu to local
    up_name = 'yutou'
    set = get_avs(up_name)
    bad = []
    for item in set:
        if get_danmu(item,up_name) == 0:
            bad.append(item)
    print ('video ids not saved successfully:')
    print (bad)

    # parse danmu containing '素材'
    xml_path = 'resources/danmu/'
    for item in set:
        xml_name = up_name+ '-danmu-'+item+'.xml'
        parse(xml_path,xml_name,item)


