import scrapy


class YpkSpider(scrapy.Spider):
    name = 'ypk'
    allowed_domains = ['ypk.39.net']
    start_urls = [
                  # 'http://ypk.39.net/jiating/',
                  # 'http://ypk.39.net/ganmao/',
                  # 'http://ypk.39.net/weichang/',
                  # 'http://ypk.39.net/pifu/',
                  # 'http://ypk.39.net/wuguan/',
                  # 'http://ypk.39.net/nanke/',
                  # 'http://ypk.39.net/fuke/',
                  # 'http://ypk.39.net/erke/',
                  # 'http://ypk.39.net/xinnaoxueguan/',
                  'http://ypk.39.net/zhongliu/'
                  ]

    def parse(self, response):
        # print(response.url)
        drug_url = response.xpath('//ul[@class="drugs-ul"]/li/a/@href').extract()
        # for i in drug_url:
        #     yield scrapy.Request{
        #         i,
        #     }
        print(drug_url)
        pass

    # def detail_parse(self, response):
