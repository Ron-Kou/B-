# encoding:utf-8
from lxml import etree

def get_xml(xml):
    xml = bytes(bytearray(xml, encoding='utf-8'))
    etree.XML(xml)