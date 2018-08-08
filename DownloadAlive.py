# encoding:utf-8
from lxml import etree
import re
import requests
import os
import datetime
import ConfigUtil

position_file_path = os.getcwd() + '/resources/danmu/all'


def save_xml(path, av):
    xml = requests.get(path)
    try:
        xml_string = xml.content.decode('utf-8')
    except UnicodeDecodeError as e:
        raise e

    file = open(position_file_path + '/all-' + av + '.xml', 'w')
    try:
        file.write(xml_string)
        print(av + ' saved.')
    except (Exception, SystemExit) as e:
        raise e
    finally:
        file.close()
    return 1


# 命名规则，all-id.xml
def save_danmu(av):
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

    try:
        save_xml(xml_path, av)
    except UnicodeDecodeError as e:
        raise e


if __name__ == '__main__':
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    p = ConfigUtil.get_config('from')
    print('{0} from av id {1}'.format(nowTime, p))
    try:
        while p < 99999999:
            try:
                save_danmu(str(p))
            except UnicodeDecodeError as e:
                print('{0} not saved for decoding error {1}'.format(p, e))
            except Exception as e:
                print('{0} not saved for unknown error {1}'.format(p, e))
            finally:
                p = p + 1
    except SystemExit as ex:
        print('-----------------------exit raised-----------------------')
        print('code ' + ex.code)
        print(str(ex))
    except Exception as e:
        print('-----------------------Exception-----------------------')
        print(str(e))
    finally:
        print('--------------------------finally conrrent p={0}-----------------------'.format(p - 1))
        ConfigUtil.set_config('max', p)
        ConfigUtil.set_config('from', p)

