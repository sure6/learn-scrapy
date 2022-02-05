#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: leesure
@file: run.py
@datetime: 2022/01/21 17:23 星期五
@description: 
"""
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl huya -o huya.csv'.split())
