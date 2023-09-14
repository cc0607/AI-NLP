# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ChinaPipeline:
    def process_item(self, item, spider):
        return item


class DeleteNullTitlePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem('found null title %s', item)


class DuplicatesTitlePipeline(object):
    def __init__(self):
        self.article = set()

    def process_item(self, item, spider):
        title = item['title']
        if title in self.article:
            raise DropItem('duplicates title found %s', item)
        self.article.add(title)
        return (item)
