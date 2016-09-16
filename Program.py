from lxml import html
import requests
from lxml import etree

def empty_string(str):
    for symbol in str:
        if symbol is not " ":
            continue
        else:
            return 1
    return 0

def parse_page():
    root = etree.Element('data')
    doc = etree.ElementTree(root)

    page = requests.get('http://tsn.ua')
    tree = html.fromstring(page.content)
    link = tree.xpath('//a[not(@class)]/@href')

    print link

    page_number = 0
    i = 0

    while page_number != 20:
        if 'javascript' in link[i]:
            i += 1
            continue

        if link[i].find('http', 0) == -1:
            link[i] = 'http://tsn.ua' + link[i]

        page = requests.get(link[i])
        tree = html.fromstring(page.content)
        text = tree.xpath('//*[text()]')
        images = tree.xpath('//img/@src')


        if text and images:
            page_element = etree.SubElement(root, 'page', url=link[i])

            for t in text:
                if t.tag != "head" and t.tag != "script" and t.text is not None and "\n" not in t.text and t is not None and "\n" not in t and t.tag != "script" and t.text and not empty_string(t.text):
                    # print t.text
                    text_fragment = etree.SubElement(page_element, 'fragment', type='text')
                    text_fragment.text = t.text


            for image in images:
                # print image
                image_fragment = etree.SubElement(page_element, 'fragment', type='image')
                image_fragment.text = image

            page_number += 1
        i += 1


    doc.write('data.xml', xml_declaration=True, encoding='utf-16')


parse_page()