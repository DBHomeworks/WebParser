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


    doc.write('task1.xml', xml_declaration=True, encoding='utf-16')

def task2():
    tree = etree.parse('task1.xml')

    url_list = []
    image_count_list = []

    for item in tree.xpath('//page'):
        subfields = item.getchildren()
        count = len([subfield.attrib["type"] for subfield in subfields if subfield.attrib["type"] == "image"])

        print item.attrib["url"]
        print count

        url_list.append([item.attrib["url"]])
        image_count_list.append(count)

    # print url_list
    # print image_count_list

    index = image_count_list.index(min(image_count_list))

    print "Minimum count of image has the following url: ", url_list[index], " : ", image_count_list[index]

def webshop_parser():
    page = requests.get('http://wallet.ua/c/f-briefcases_for_men/')
    tree = html.fromstring(page.content)
    products = tree.xpath('//div[@id="catalog"]/div[@class="catalog-section"]//table[@class="item_info"]')
    return [{
                "image": get_image(product),
                "name": get_product_name(product),
                "price": get_product_price(product)
            } for product in products]

def get_image(product):
        image = product.xpath('.//a[@class="multy-img"]/img[@class="second-picture"]')[0]

        return {"src": "http://wallet.ua" + image.xpath('.//@src')[0],
                                "description": image.xpath('.//@alt')[0]}

def get_product_name(product):
    return product.xpath('.//tr/td[@align="left"]/a/text()')[0].strip()

def get_product_price(product):
    return product.xpath('.//span[@class="catalog-price crate"]/text()')[0].strip()

def write_to_file():
    root = etree.Element('data')
    doc = etree.ElementTree(root)

    bag_number = 1

    for item in webshop_parser():
        bag = etree.SubElement(root, 'bag')
        name = etree.SubElement(bag, 'name', value=item['name'])
        price = etree.SubElement(bag, 'price', value=item['price'])
        name = etree.SubElement(bag, 'image', value=item['image']['src'])
        description = etree.SubElement(bag, 'description', value=item['image']['description'])

    doc.write('task4.xml', xml_declaration=True, encoding='utf-16')


# parse_page()

# task2()

write_to_file()
