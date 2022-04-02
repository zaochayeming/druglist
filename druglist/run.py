from scrapy import cmdline

# 运行爬虫
# cmdline.execute(['scrapy', 'crawl', 'ypk'])
# cmdline.execute(['scrapy', 'crawl', 'ypks'])
cmdline.execute(['scrapy', 'crawl', 'symptom'])

# 导出成csv文件
# cmdline.execute(['scrapy', 'crawl', 'ypk', '-o', 'result.csv'])
# cmdline.execute(['scrapy', 'crawl', 'ypks', '-o', '../result.csv'])
# cmdline.execute(["scrapy crawl ypk -o result.csv -t csv".split()])

# 导出json文件
# cmdline.execute(['scrapy', 'crawl', 'ypks', '-o', 'result.json'])

