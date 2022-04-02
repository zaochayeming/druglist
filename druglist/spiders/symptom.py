import scrapy


class HospitalSpider(scrapy.Spider):
    name = 'symptom'
    allowed_domains = ['www.a-hospital.com']
    start_urls = [
        'http://www.a-hospital.com/w/症状条目索引-A'
        # 'http://www.a-hospital.com/w/症状条目索引-B',
        # 'http://www.a-hospital.com/w/症状条目索引-C',
        # 'http://www.a-hospital.com/w/症状条目索引-D',
        # 'http://www.a-hospital.com/w/症状条目索引-E',
        # 'http://www.a-hospital.com/w/症状条目索引-F',
        # 'http://www.a-hospital.com/w/症状条目索引-G',
        # 'http://www.a-hospital.com/w/症状条目索引-H',
        # 'http://www.a-hospital.com/w/症状条目索引-J',
        # 'http://www.a-hospital.com/w/症状条目索引-K',
        # 'http://www.a-hospital.com/w/症状条目索引-L',
        # 'http://www.a-hospital.com/w/症状条目索引-M',
        # 'http://www.a-hospital.com/w/症状条目索引-N',
        # 'http://www.a-hospital.com/w/症状条目索引-P',
        # 'http://www.a-hospital.com/w/症状条目索引-Q',
        # 'http://www.a-hospital.com/w/症状条目索引-R',
        # 'http://www.a-hospital.com/w/症状条目索引-S',
        # 'http://www.a-hospital.com/w/症状条目索引-T',
        # 'http://www.a-hospital.com/w/症状条目索引-W',
        # 'http://www.a-hospital.com/w/症状条目索引-X',
        # 'http://www.a-hospital.com/w/症状条目索引-Y',
        # 'http://www.a-hospital.com/w/症状条目索引-Z'
    ]

    def parse(self, response):
        resps = response.xpath('//div[@id="bodyContent"]/ul/li/a/@href').extract()
        for i in resps:
            detail_url = 'http://www.a-hospital.com' + i
            yield scrapy.Request(
                detail_url,
                callback=self.detail_parse
            )
            # print(url)
        pass

    def detail_parse(self, response):
        print(response.status)
        name = response.xpath('//h1/text()').extract_first()
        list = response.xpath('//div[@id="toctitle"]')
        print(name)
        print(list)
        pass
