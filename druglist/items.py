# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DruglistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通用名称 = scrapy.Field()    # 通用名称
    # 商品名称 = scrapy.Field()    # 商品名称
    # 英文名称 = scrapy.Field()    # 英文名称
    # 汉语拼音 = scrapy.Field()    # 汉语拼音
    # 药品分类 = scrapy.Field()    # 药品分类
    # 成分 = scrapy.Field()    # 成分
    # 性状 = scrapy.Field()    # 性状
    # 适应症 = scrapy.Field()    # 适应症
    # 功能主治 = scrapy.Field()    # 功能主治
    # 用法用量 = scrapy.Field()    # 用法用量
    # 不良反应 = scrapy.Field()    # 不良反应
    # 禁忌 = scrapy.Field()    # 禁忌
    # 注意事项 = scrapy.Field()    # 注意事项
    # 药物相互作用 = scrapy.Field()    # 药物相互作用
    # 贮藏 = scrapy.Field()    # 贮藏
    # 规格 = scrapy.Field()    # 规格
    # 包装规格 = scrapy.Field()    # 包装规格
    # 有效期 = scrapy.Field()    # 有效期
    # 批准文号 = scrapy.Field()    # 批准文号
    # 说明书修订日期 = scrapy.Field()    # 说明书修订日期
    # 特殊人群用药 = scrapy.Field()    # 特殊人群用药
    # 药理作用 = scrapy.Field()    # 药理作用
    # 企业名称 = scrapy.Field()    # 企业名称
    # 企业简称 = scrapy.Field()    # 企业简称


    common_name = scrapy.Field()    # 通用名称
    trade_name = scrapy.Field()    # 商品名称
    english_name = scrapy.Field()    # 英文名称
    chinese_name = scrapy.Field()    # 汉语拼音
    medicine_tag = scrapy.Field()    # 药品分类
    component = scrapy.Field()    # 成分
    character = scrapy.Field()    # 性状
    indication = scrapy.Field()    # 适应症
    functions = scrapy.Field()    # 功能主治
    dosage = scrapy.Field()    # 用法用量
    adverse_reaction = scrapy.Field()    # 不良反应
    taboo = scrapy.Field()    # 禁忌
    attention = scrapy.Field()    # 注意事项
    drug_interaction = scrapy.Field()    # 药物相互作用
    storage = scrapy.Field()    # 贮藏
    specifications = scrapy.Field()    # 规格
    package = scrapy.Field()    # 包装规格
    time = scrapy.Field()    # 有效期
    approval_number = scrapy.Field()    # 批准文号
    revision_date = scrapy.Field()    # 说明书修订日期
    special = scrapy.Field()    # 特殊人群用药
    action = scrapy.Field()    # 药理作用
    enterprise_name = scrapy.Field()    # 企业名称
    enterprise_abbreviation = scrapy.Field()    # 企业简称