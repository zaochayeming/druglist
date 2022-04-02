import scrapy


class HospitalSpider(scrapy.Spider):
    name = 'disease'
    allowed_domains = ['www.a-hospital.com']
    start_urls = ['http://www.a-hospital.com/']

    def parse(self, response):
        print(response.status)
        pass
