import lxml.etree as ET


tree = ET.fromstring('''<div>
... <div>
...     <p>
...     <span class="abc">Monitor</span> <b>$300</b>
...     </p>
...     <a href="/add">Add to cart</a>
... </div>
... <div>
...     <p>
...     <span class="abc">Keyboard</span> $20
...     </p>
...     <a href="/add">Add to cart</a>
... </div>
... </div>''')
print tree.xpath('//div[a[contains(., "Add to cart")]]/p//text()')
# ['\n    ', 'Monitor', ' ', '$300', '\n    ', '\n    ', 'Keyboard', ' $20 \n    ']
# res = _
# [txt for txt in (txt.strip() for txt in res) if txt]
# ['Monitor', '$300', 'Keyboard', '$20']