#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 新房楼盘的数据结构


class LouPan(object):
    def __init__(self, xiaoqu, price, total, pois_name, type, adname, location):
        # self.district = district
        # self.area = area
        self.xiaoqu = xiaoqu
        # self.address = address
        # self.size = size
        self.price = price
        self.total = total
        self.pois_name = pois_name
        self.type = type
        self.adname = adname
        self.location = location

    def text(self):
        return self.xiaoqu + "," + \
                self.price + "," + \
                self.total + "," + \
                self.pois_name + "," + \
                self.type + "," + \
                self.adname + "," + \
                self.location