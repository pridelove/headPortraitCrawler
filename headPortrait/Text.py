# import requests
# # from lxml import etree
# # wb_data = requests.get('https://m.woyaogexing.com/touxiang/katong/index_2.html').content
# # html = etree.HTML(wb_data)
# # #res = html.xpath('//div/ul[@class="g-piclist-container"]//li//a//img/@data-src')
# # res = html.xpath('//div//ul[@class="g-piclist-container"]//li//img//@data-src')
# # print(res)
from lxml import etree
import re

str ='https://m.woyaogexing.com/touxiang/nv/2020/969070.html'
print(re.findall(r'/touxiang/[a-z]{0,7}/',str))