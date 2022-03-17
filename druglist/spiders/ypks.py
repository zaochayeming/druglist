import scrapy
import re
# from druglist.items import DruglistItem
from scrapy import Item, Field
from scrapy.loader import ItemLoader


class YpksSpider(scrapy.Spider):
    name = 'ypks'
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
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def detail_parse(self, response):
        item = Item()
        item_l = ItemLoader(item=item)
        print(response.url)
        drug_instructions = response.xpath('//ul[@class="drug-explain"]/li')
        for i in drug_instructions:
            if len(i.xpath('./p[contains(text(), "【药品名称】")]')) > 0:
                name = i.xpath('./p[contains(text(), "【药品名称】")]/following-sibling::p[position()>0]')
                # print(name)
                # print(name.re("汉语拼音：(.*?)\n"))
                if len(name.re("通用名称：(.*?)\n")) > 0:
                    common_name = name.re("通用名称：(.*?)\n")[0].strip()
                    # medicine_item['common_name'] = common_name
                    item.fields['通用名称'] = Field()
                    item_l.add_value('通用名称', common_name)
                    # print('通用名称：', common_name)

                    # 药品类型
                    medicine_tag = response.xpath('//div[@class="drug-name-type-add"]/i/text()').extract()  # 药品类型
                    medicine_tag = '，'.join(medicine_tag)
                    # medicine_item['medicine_tag'] = medicine_tag
                    item.fields['药品类型'] = Field()
                    item_l.add_value('药品类型', medicine_tag)
                    # print('药品类型', medicine_tag)

                if len(name.re("商品名称：(.*?)<")) > 0:
                    trade_name = name.re("商品名称：(.*?)<")[0].replace('<br>', '').strip()
                    # medicine_item['trade_name'] = trade_name
                    item.fields['商品名称'] = Field()
                    item_l.add_value('商品名称', trade_name)
                    # print('商品名称：', trade_name)
                if len(name.re("英文名称：(.*?)<")) > 0:
                    english_name = name.re("英文名称：(.*?)<")[0].replace('<br>', '').strip()
                    # medicine_item['english_name'] = english_name
                    item.fields['英文名称'] = Field()
                    item_l.add_value('英文名称', english_name)
                    # print('英文名称：', english_name)
                if len(name.re("汉语拼音：(.*)<")) > 0:
                    chinese_name = name.re("汉语拼音：(.*)<")[0].strip()
                    # medicine_item['chinese_name'] = chinese_name
                    item.fields['汉语拼音'] = Field()
                    item_l.add_value('汉语拼音', chinese_name)
                    # print('汉语拼音：', chinese_name)
            if len(i.xpath('./p[contains(text(), "【成份】")]')) > 0:
                # component = i.xpath('./p[contains(text(), "【成份】")]/following-sibling::p[1').re("\r\n(.*?)\r\n")[0].strip()
                component = i.xpath('./p[contains(text(), "【成份】")]/following-sibling::p[position()>0]/text()').extract()
                component = ''.join(component).strip()
                # medicine_item['component'] = unescape(re.sub('<[^>]*>', '', component))
                component = re.sub('<[^<]+?>', '', component)
                # medicine_item['component'] = component
                item.fields['成份'] = Field()
                item_l.add_value('成份', component)
                # print('成份:', component)
            if len(i.xpath('./p[contains(text(), "【性状】")]')) > 0:
                character = i.xpath('./p[contains(text(), "【性状】")]/following-sibling::p[position()>0]/text()').extract()
                character = ''.join(character).strip()
                # medicine_item['character'] = character
                item.fields['性状'] = Field()
                item_l.add_value('性状', character)
                # print('性状:', character)
            if len(i.xpath('./p[contains(text(), "【适应症】")]')) > 0:
                indication = i.xpath('./p[contains(text(), "【适应症】")]/following-sibling::p[position()>0]/text()').extract()
                indication = ''.join(indication).strip()
                indication = re.sub('<[^<]+?>', '', indication)
                # medicine_item['indication'] = indication
                item.fields['适应症'] = Field()
                item_l.add_value('适应症', indication)
                # print('适应症:', indication)
            if len(i.xpath('./p[contains(text(), "【功能主治】")]')) > 0:
                functions = i.xpath('./p[contains(text(), "【功能主治】")]/following-sibling::p[position()>0]/text()').extract()
                functions = ''.join(functions).strip()
                # medicine_item['functions'] = functions
                item.fields['功能主治'] = Field()
                item_l.add_value('功能主治', functions)
                # print('功能主治:', functions)
            if len(i.xpath('./p[contains(text(), "【用法用量】")]')) > 0:
                dosage = i.xpath('./p[contains(text(), "【用法用量】")]/following-sibling::p[position()>0]/text()').extract()
                dosage = ''.join(dosage).strip()
                dosage = re.sub('<[^<]+?>', '', dosage)
                # medicine_item['dosage'] = dosage
                item.fields['用法用量'] = Field()
                item_l.add_value('用法用量', dosage)
                # print('用法用量:', dosage)
            if len(i.xpath('./p[contains(text(), "【不良反应】")]')) > 0:
                adverse_reaction = i.xpath('./p[contains(text(), "【不良反应】")]/following-sibling::p[position()>0]/text()').extract()
                adverse_reaction = ''.join(adverse_reaction).strip()
                # medicine_item['adverse_reaction'] = adverse_reaction
                item.fields['不良反应'] = Field()
                item_l.add_value('不良反应', adverse_reaction)
                # print('不良反应:', adverse_reaction)
            if len(i.xpath('./p[contains(text(), "【禁忌】")]')) > 0:
                taboo = i.xpath('./p[contains(text(), "【禁忌】")]/following-sibling::p[position()>0]/text()').extract()
                taboo = ''.join(taboo).strip()
                # medicine_item['taboo'] = taboo
                item.fields['禁忌'] = Field()
                item_l.add_value('禁忌', taboo)
                # print('禁忌:', taboo)
            if len(i.xpath('./p[contains(text(), "【注意事项】")]')) > 0:
                attention = i.xpath('./p[contains(text(), "【注意事项】")]/following-sibling::p[position()>0]/text()').extract()
                attention = ''.join(attention).strip()
                # medicine_item['attention'] = attention
                item.fields['注意事项'] = Field()
                item_l.add_value('注意事项', attention)
                # print('注意事项:', attention)
            if len(i.xpath('./p[contains(text(), "【药物相互作用】")]')) > 0:
                drug_interaction = i.xpath('./p[contains(text(), "【药物相互作用】")]/following-sibling::p[position()>0]/text()').extract()
                drug_interaction = ''.join(drug_interaction).strip()
                # medicine_item['drug_interaction'] = drug_interaction
                item.fields['药物相互作用'] = Field()
                item_l.add_value('药物相互作用', drug_interaction)
                # print('药物相互作用:', drug_interaction)
            if len(i.xpath('./p[contains(text(), "【贮藏】")]')) > 0:
                storage = i.xpath('./p[contains(text(), "【贮藏】")]/following-sibling::p[position()>0]/text()').extract()
                storage = ''.join(storage).strip()
                # medicine_item['storage'] = storage
                item.fields['贮藏'] = Field()
                item_l.add_value('贮藏', storage)
                # print('贮藏:', storage)
            if len(i.xpath('./p[contains(text(), "【规格】")]')) > 0:
                specifications = i.xpath('./p[contains(text(), "【规格】")]/following-sibling::p[position()>0]/text()').extract()
                specifications = ''.join(specifications).strip()
                # medicine_item['specifications'] = specifications
                item.fields['规格'] = Field()
                item_l.add_value('规格', specifications)
                # print('规格:', specifications)
            if len(i.xpath('./p[contains(text(), "【包装规格】")]')) > 0:
                package = i.xpath('./p[contains(text(), "【包装规格】")]/following-sibling::p[position()>0]/text()').extract()
                package = ''.join(package).strip()
                # medicine_item['package'] = package
                item.fields['包装规格'] = Field()
                item_l.add_value('包装规格', package)
                # print('包装规格:', package)
            if len(i.xpath('./p[contains(text(), "【有效期】")]')) > 0:
                time = i.xpath('./p[contains(text(), "【有效期】")]/following-sibling::p[position()>0]/text()').extract()
                time = ''.join(time).strip()
                # medicine_item['time'] = time
                item.fields['有效期'] = Field()
                item_l.add_value('有效期', time)
                # print('有效期:', time)
            if len(i.xpath('./p[contains(text(), "【批准文号】")]')) > 0:
                approval_number = i.xpath('./p[contains(text(), "【批准文号】")]/following-sibling::p[position()>0]/text()').extract()
                approval_number = ''.join(approval_number).strip()
                # medicine_item['approval_number'] = approval_number
                item.fields['批准文号'] = Field()
                item_l.add_value('批准文号', approval_number)
                # print('批准文号:', approval_number)
            if len(i.xpath('./p[contains(text(), "【说明书修订日期】")]')) > 0:
                revision_date = i.xpath('./p[contains(text(), "【说明书修订日期】")]/following-sibling::p[position()>0]/text()').extract()
                revision_date = ''.join(revision_date).strip()
                # medicine_item['revision_date'] = revision_date
                item.fields['说明书修订日期'] = Field()
                item_l.add_value('说明书修订日期', revision_date)
                # print('说明书修订日期:', revision_date)
            if len(i.xpath('./p[contains(text(), "【特殊人群用药】")]')) > 0:
                tem = i.xpath('./p[contains(text(), "【特殊人群用药】")]/following-sibling::p[position()>0]').extract()
                special = ''
                for x in tem:
                    x = re.sub('<[^>]*>', '', x).strip().replace(' ', '').split('\r\n')
                    for j in x:
                        if j != '':
                            special += j + '\n'

                    # x = [i for i in x if i != '']
                    # x = re.sub('<[^>]*>', '', x).strip().replace(' ', '').replace('\r\n', '')
                    # print(x)
                # medicine_item['special'] = special[0:-1].replace(' ', '')
                item.fields['特殊人群用药'] = Field()
                item_l.add_value('特殊人群用药', special[0:-1].replace(' ', ''))
                # print('特殊人群用药:', special)
            if len(i.xpath('./p[contains(text(), "【药理作用】")]')) > 0:
                action = i.xpath('./p[contains(text(), "【药理作用】")]/following-sibling::p[position()>0]/text()').extract()
                action = ''.join(action).strip()
                # medicine_item['action'] = action
                item.fields['药理作用'] = Field()
                item_l.add_value('药理作用', action)
                # print('药理作用:', action)
            if len(i.xpath('./p[contains(text(), "【生产企业】")]')) > 0:
                manufacturing = i.xpath('./p[contains(text(), "【生产企业】")]/following-sibling::p[1]')
                # print(manufacturing)
                # print(len(manufacturing.re("企业简称：(.*?)\n")))
                if len(manufacturing.re("企业名称：(.*?)\n")) > 0:
                    enterprise_name = manufacturing.re("企业名称：(.*?)\n")[0]
                    # medicine_item['enterprise_name'] = enterprise_name
                    item.fields['企业名称'] = Field()
                    item_l.add_value('企业名称', enterprise_name)
                    # print('企业名称：', enterprise_name)
            if len(i.re("企业简称：(.*?)\n")) > 0:
                enterprise_abbreviation = i.re("企业简称：(.*?)</p>")[0].strip()
                # medicine_item['enterprise_abbreviation'] = enterprise_abbreviation
                item.fields['企业简称'] = Field()
                item_l.add_value('企业简称', enterprise_abbreviation)
                # print('企业简称：', enterprise_abbreviation)
        # print('2')
        # return medicine_item
        return item_l.load_item()
        # pass
