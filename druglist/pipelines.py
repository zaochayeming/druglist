# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DruglistPipeline:
    def process_item(self, item, spider):
        for key, values in item.items():
            if key == '药品':
                if DataProcess.m_name(values[0]) is None:
                    item[key] = values[0]
                else:
                    item[key] = DataProcess.m_name(values[0]).group()[0:-1]
            elif key == '药品类型':
                item[key] = '，'.join(values)
            else:
                item[key] = values[0]
            # values = values[0]
            # print(values)
        print(item)
        return item


class DataProcess:
    def m_name(self):
        pattern = re.compile('(.*)[(]')
        result = pattern.search(self)
        return result
