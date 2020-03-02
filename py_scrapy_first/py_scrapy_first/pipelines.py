# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class PyScrapyFirstPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="py_scrapy_first_pc_dangdang")
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            sql="insert into books(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            #print(sql)
            conn.query(sql)
            conn.commit()
        conn.close()
        return item
