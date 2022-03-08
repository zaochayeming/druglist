# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DruglistPipeline:
    def process_item(self, item, spider):
        for key, values in item.items():
            values = values[0]
            # print(values)
        # print('2')
        return item
