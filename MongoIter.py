# -*- coding:utf-8 -*-
"""
解决MongoDB大数据集遍历时会出现的
"""

def mongo_iter(col, limit):
    while True:
        if cursor_id != None:
            cursor = col.find({'_id': {'$gt': cursor_id}}).limit(limit)
        else:
            cursor = col.find().limit(limit)

        if cursor.count() == 0:
            break

        for item in cursor:
            yield item

        cursor_id = item.get('_id')

