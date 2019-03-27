# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import datetime
import csv

class WeibohotspiderPipeline(object):

    timeStr = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    csvFilePath = os.getcwd() + "/data"
    csvFileName = timeStr + ".csv"
    def open_spider(self, spider):

        print("开始爬虫")

        if not os.path.exists(self.csvFilePath):
            os.mkdir(self.csvFilePath)

        os.chdir(self.csvFilePath)
        with open(self.csvFileName, "w") as f:
            csv_write = csv.writer(f)
            csv_row = ["NO", "keyword", "state", "hot", "href"]
            csv_write.writerow(csv_row)

    def process_item(self, item, spider):

        # print(item)
        os.chdir(self.csvFilePath)
        with open(self.csvFileName, "a+") as f:
            csv_write = csv.writer(f)
            data_row = [item["NO"], item["keyword"], item["state"], item["hot"], item["href"]]
            csv_write.writerow(data_row)

        return item

    def close_spider(self, spider):

        print("结束爬虫")