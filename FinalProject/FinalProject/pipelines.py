# Created by: Maria Masood
# Date: 04/07/2021
# Description: After an item has been scraped by a spider, it is sent to pipeline.py to process several components that
#are executed sequentially


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FinalprojectPipeline:
    def process_item(self, item, spider):
        return item
