# encoding:utf-8
import xml.etree.ElementTree as ET

keyword = '素材'


def parse(xml_path,xml_name,item):
    source = xml_path + xml_name
    tree = ET.parse(source)
    bili_url = 'https://www.bilibili.com/video/av{0}'.format(item)
    # tree = ET.parse('resources/danmu/yutou-danmu-7639037.xml')
    root = tree.getroot()

    # 遍历xml文档的第二层
    for child in root:
        # 第二层节点的标签名称和属性
        if child.tag == 'd':
            seconds = child.attrib['p'].split(',')[0]
            minutes = 0
            time_string = ''
            seconds = float(seconds)
            if seconds > 60:
                minutes = int(seconds / 60)
                time_string = '{0}分{1}秒'.format(minutes,round(seconds - minutes*60,3))
            else:
                time_string = '{0}秒'.format(seconds)
            # print(time_string, ":", child.text)
            if keyword in child.text:
                print(bili_url+','+time_string, ":", child.text)


