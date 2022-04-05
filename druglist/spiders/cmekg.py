import scrapy
import json
import os
import pandas as pd
from scrapy import Item, Field
from scrapy.loader import ItemLoader


class HospitalSpider(scrapy.Spider):
    name = 'cmekg'
    allowed_domains = ['cmekg.pcl.ac.cn']
    current_path = os.path.dirname(__file__)
    data_name = pd.read_json(current_path + '/data/treatment.json')
    urls = []
    for i in data_name['name']:
        url = 'https://zstp.pcl.ac.cn:8002/get_tree_map?name=' + i
        urls.append(url)
    start_urls = urls

    def parse(self, response):
        item = Item()
        item_l = ItemLoader(item=item)

        resp = json.loads(response.text)
        name = resp['data']['name']
        item.fields['名称'] = Field()
        item_l.add_value('名称', name)

        for i in resp['data']['children']:
            key = i['name']
            value = []
            for i in i['children']:
                value.append(i['name'])
            value = '，'.join(value)

            item.fields[key] = Field()
            item_l.add_value(key, value)

        print(item_l.load_item())
        return item_l.load_item()
