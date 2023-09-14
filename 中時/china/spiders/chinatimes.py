import scrapy
import bs4
from scrapy_selenium import SeleniumRequest
from datetime import datetime
import re
from ..items import ChinaItem


class ChinatimesSpider(scrapy.Spider):
    name = "chinatimes"
    allowed_domains = ["chinatimes.com"]
    page_temp_url = "https://www.chinatimes.com/search/台灣選舉?page=%d&chdtv"
    cur_page = 3
    max_page = 5

    start_urls = (page_temp_url % cur_page)

    def start_requests(self):
        for page in range(6, 8):
            # print('----------------page{i}-----------------')
            yield SeleniumRequest(url=f'https://www.chinatimes.com/search/台灣選舉?page={page}&chdtv', callback=self.parse)

    def parse(self, response):

        titles = response.xpath(
            "//div[@class='articlebox-compact']//h3//a/text()").get()
        urls = response.xpath(
            "//div[@class='articlebox-compact']//h3//a/@href").getall()

        # 有文章才要繼續

        for i in range(len(urls)):
            yield response.follow(urls[i], callback=self.parse_article)

    def parse_article(self, response):

        # 標題
        title = response.xpath('//h1/text()').get()

        catagory = response.xpath("//div[@class='source']/text()").get()

        # 發文時間
        published_time = response.xpath("//span[@class='date']/text()").get()
        # published_time = datetime.strptime(
        #   published_time_str, '%Y-%m-%d')

        # 內文
        content = ' '.join(response.xpath(
            "//div[@class='article-body']//p").getall())

        items = ChinaItem()
        items['url'] = response.url
        items['title'] = title
        items['catagory'] = catagory
        items['publish_time'] = published_time
        items['content'] = content

        yield items
