# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
from xml.sax.saxutils import unescape
from scrapy.exporters import JsonItemExporter


# useful for handling different item types with a single interface


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
                # 替换转义字符和html标签内容
                # content = html_parser.unescape(re.sub('<[^>]*>', '', values[0]))
                content = unescape(re.sub('<[^>]*>', '', values[0])).replace('', '') \
                    .replace('&nbsp;', ' ') \
                    .replace('&;;', '～') \
                    .replace('&ldquo;', '“') \
                    .replace('&nbs', ' ') \
                    .replace('&nb', ' ') \
                    .replace('&n', ' ') \
                    .replace('&middot', '·') \
                    .replace('&rsquo', '"') \
                    .replace('&amp', '&') \
                    .replace('&ndash', ';') \
                    .replace('&times', '×') \
                    .replace('&ge;', '⊂') \
                    .replace('&ge', '⊂') \
                    .replace('&alpha', 'α') \
                    .replace('&;alpha;', 'α') \
                    .replace('&beta', 'β') \
                    .replace('&;beta;', 'β') \
                    .replace('&Beta', 'β') \
                    .replace('&gamma;', 'γ') \
                    .replace('&gamma', 'γ') \
                    .replace('&Delta;', 'Δ') \
                    .replace('&prime;', '′') \
                    .replace('&gt;', '>') \
                    .replace('&deg;', '°') \
                    .replace('&deg', '°') \
                    .replace('&plusmn', '±') \
                    .replace('&hellip;', '…') \
                    .replace('&larr;', '←') \
                    .replace('&acute;', '´') \
                    .replace('&micro;', 'µ') \
                    .replace('&bull;;', '•') \
                    .replace('&;bull;', '•') \
                    .replace('&bull;', '•') \
                    .replace('&Ograve;', 'Ò') \
                    .replace('&rdquo;', '”') \
                    .replace('&mu', 'μ') \
                    .replace('&le', '≤') \
                    .replace('rsquo', '"') \
                    .replace('&mu', 'Ν') \
                    .replace('amp', '&') \
                    .replace('&mdash;', '—') \
                    .replace('mdash', '—') \
                    .replace('&rarr;', '→') \
                    .replace('&gt;;', '>') \
                    .replace('&ordm;', 'º') \
                    .replace('&infin;', '∞') \
                    .replace('&lt;', '<') \
                    .replace('&lt;', '<') \
                    .replace('&#;', '、') \
                    .replace('Hydroxyc&tothecinfor', 'Hydroxycamptothecinfor ') \
                    .replace('&#8226;', '·')
                item[key] = content
            # values = values[0]
            # print(values)
        print(item)
        return item


class DruglistPipelines:
    def __init__(self):
        # 爬虫开始生成json文件
        self.file = open("result.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        # 导出json文件结束
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        # 过滤通用名称并导出json文件
        tem = item['通用名称'][0]
        data = dict({'通用名称': tem})
        print(data)
        self.exporter.export_item(data)

        for key, values in item.items():
            # print(key, values)
            values = values[0].replace(',', '，').replace('', '') \
                .replace('&nbsp;', ' ') \
                .replace('&;;', '～') \
                .replace('&ldquo;', '“') \
                .replace('&nbs', ' ') \
                .replace('&nb', ' ') \
                .replace('&n', ' ') \
                .replace('&middot', '·') \
                .replace('&rsquo', '"') \
                .replace('&amp', '&') \
                .replace('&ndash', ';') \
                .replace('&times', '×') \
                .replace('&ge;', '⊂') \
                .replace('&ge', '⊂') \
                .replace('&alpha', 'α') \
                .replace('&;alpha;', 'α') \
                .replace('&beta', 'β') \
                .replace('&;beta;', 'β') \
                .replace('&Beta', 'β') \
                .replace('&gamma;', 'γ') \
                .replace('&gamma', 'γ') \
                .replace('&Delta;', 'Δ') \
                .replace('&prime;', '′') \
                .replace('&gt;', '>') \
                .replace('&deg;', '°') \
                .replace('&deg', '°') \
                .replace('&plusmn', '±') \
                .replace('&hellip;', '…') \
                .replace('&larr;', '←') \
                .replace('&acute;', '´') \
                .replace('&micro;', 'µ') \
                .replace('&bull;;', '•') \
                .replace('&;bull;', '•') \
                .replace('&bull;', '•') \
                .replace('&Ograve;', 'Ò') \
                .replace('&rdquo;', '”') \
                .replace('&mu', 'μ') \
                .replace('&le', '≤') \
                .replace('rsquo', '"') \
                .replace('&mu', 'Ν') \
                .replace('amp', '&') \
                .replace('&mdash;', '—') \
                .replace('mdash', '—') \
                .replace('&rarr;', '→') \
                .replace('&gt;;', '>') \
                .replace('&ordm;', 'º') \
                .replace('&infin;', '∞') \
                .replace('&lt;', '<') \
                .replace('&lt;', '<') \
                .replace('&#;', '、') \
                .replace('&#8226;', '·')
            # print(key, ':', values)
            # print(key, values)
            # print(values)
        return item

class DiseaseListPipelines:
    def process_item(self, item, spider):
        # print('1')
        for key, values in item.items():
            values = values[0].replace(',', '，')
            # print(values)
            print(key, values)
        return item


class DataProcess:
    def m_name(self):
        pattern = re.compile('(.*)[(]')
        result = pattern.search(self)
        return result
