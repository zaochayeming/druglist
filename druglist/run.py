from scrapy import cmdline

# 运行爬虫
# cmdline.execute(['scrapy', 'crawl', 'ypk'])
# 导出成csv文件
cmdline.execute(['scrapy', 'crawl', 'ypk', '-o', 'result.csv'])
# cmdline.execute(["scrapy crawl ypk -o result.csv -t csv".split()])
