# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: len chen
# CreateDate: 2021/10/14 4:01 下午
# Description:
import json
import requests


class Prometheus:
    # 测试，暂时先写在这
    address = "10.0.2.113:19011"

    def query(self, expr):
        url = 'http://' + self.address + '/api/v1/query?query=' + expr
        try:
            rsp = json.loads(requests.get(url=url, timeout=0.5).content.decode('utf8', 'ignore'))
            if rsp.get('status') == 'success':
                return rsp.get('data')
            else:
                return {}
        except Exception as e:
            print(e)
            return {}
