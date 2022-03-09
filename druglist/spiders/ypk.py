import scrapy
import re
# from druglist.items import DruglistItem

from scrapy import Item, Field
from scrapy.loader import ItemLoader


class YpkSpider(scrapy.Spider):
    name = 'ypk'
    allowed_domains = ['ypk.39.net']
    start_urls = [
        'http://ypk.39.net/jiating/',
        'http://ypk.39.net/ganmao/',
        'http://ypk.39.net/weichang/',
        'http://ypk.39.net/pifu/',
        'http://ypk.39.net/wuguan/',
        'http://ypk.39.net/nanke/',
        'http://ypk.39.net/fuke/',
        'http://ypk.39.net/erke/',
        'http://ypk.39.net/xinnaoxueguan/',
        'http://ypk.39.net/zhongliu/'
    ]

    def parse(self, response, **kwargs):
        # print(response.url)
        drug_url = response.xpath('//ul[@class="drugs-ul"]/li/a/@href').extract()  # 获取当前页面药品详情页面url
        # print(drug_url)
        # 访问药品详情页面
        for i in drug_url:
            i = i + 'manual/'
            yield scrapy.Request(
                i,
                callback=self.detail_parse
            )

        next_url = response.xpath('//p[@class="page-number"]/a[contains(text(), "下页")]/@href').extract_first()   # 获取下一页的url
        print(next_url)
        # 访问下一页药品数据
        yield scrapy.Request(
            next_url,
            callback=self.parse
        )
        # pass

    # 获取药品说明书内容
    def detail_parse(self, response):
        item = Item()
        item_l = ItemLoader(item=item)

        m_name = response.xpath('//h1[@class="drug-layout-r-stor"]/text()').extract_first()  # 药品名称
        # print(m_name)
        item.fields['药品'] = Field()
        item_l.add_value('药品', m_name)

        m_tag = response.xpath('//div[@class="drug-name-type-add"]/i/text()').extract()  # 药品类型标签
        item.fields['药品类型'] = Field()
        item_l.add_value('药品类型', m_tag)

        drug_instructions = response.xpath('//ul[@class="drug-explain"]/li')
        for i in drug_instructions:
            # 获取说明书的标题信息
            key = i.xpath('./p[1]/text()').re(r'[【](.*?)[】]')[0]

            # 获取标题的内容信息
            tem = i.xpath('./p[position()>1]//text()').extract()
            tem = ''.join(tem)
            tem = re.split(r'\s+', tem)
            value = ''.join(tem).replace(',', '，').replace('<p>', '').replace('</p>', '')
            item.fields[key] = Field()
            item_l.add_value(key, value)

        return item_l.load_item()
