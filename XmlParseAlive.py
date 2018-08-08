# encoding = utf-8
from XmlParser import parse
import os
import datetime
import ConfigUtil


def clean(start,end):
    dir = os.getcwd() + '/resources/danmu/all/'
    for file in os.listdir(dir):
        # 避免非xml文件的干扰
        if file.split('.')[1] == 'xml':
            name_id = int(file.split('-')[1].split('.')[0])
            if start <= name_id <= end:
                os.remove(dir + file)
                print(file + " deleted")
    print('cleaned xml finished.')


if __name__ == '__main__':
    xml_path = os.getcwd() + '/resources/danmu/all/'
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    p = ConfigUtil.get_config('start')
    max_p = ConfigUtil.get_config('max')
    ConfigUtil.set_config('from', max_p + 1)

    print('{0} av id {1}-{2}'.format(nowTime, p, max_p))
    # 追加
    out_file = open(os.getcwd() + '/resources/config/out.txt', 'a')
    try:
        while p < max_p:
            try:
                out = parse(xml_path, 'all-{0}.xml'.format(p), p)
                if out is not None:
                    out_file.write(out + '\n')
            except Exception as e:
                print('{0} not parsed error {1}'.format(p, e))
            p = p + 1
    except (Exception, SystemExit) as e:
        print(e)
        ConfigUtil.set_config('from', p)

    finally:
        start = ConfigUtil.get_config('start')
        ConfigUtil.set_config('start', p)
        out_file.close()
        clean(start,p)
