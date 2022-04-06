from scrapy import cmdline

# 运行爬虫
# cmdline.execute(['scrapy', 'crawl', 'ypk'])
# cmdline.execute(['scrapy', 'crawl', 'ypks'])
# cmdline.execute(['scrapy', 'crawl', 'ahospital'])
# cmdline.execute(['scrapy', 'crawl', 'cmekg'])

# 导出成csv文件
# cmdline.execute(['scrapy', 'crawl', 'ypk', '-o', 'result.csv'])
# cmdline.execute(['scrapy', 'crawl', 'ypks', '-o', '../result.csv'])
# cmdline.execute(['scrapy', 'crawl', 'cmekg', '-o', 'result.csv'])
cmdline.execute(['scrapy', 'crawl', 'ahospital', '-o', 'ahospital.csv'])
# cmdline.execute(["scrapy crawl ypk -o result.csv -t csv".split()])

# 导出json文件
# cmdline.execute(['scrapy', 'crawl', 'ypks', '-o', 'result.json'])
# cmdline.execute(['scrapy', 'crawl', 'cmekg', '-o', 'result.json'])

