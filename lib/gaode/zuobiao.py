import requests
from lib.request.headers import *
from lib.spider.base_spider import *


def get_zuobiao(x):
    headers = create_headers()
    BaseSpider.random_delay()
    # url = "https://restapi.amap.com/v3/geocode/geo"
    url = "https://restapi.amap.com/v3/place/text"
    data = {
        'keywords': x,
        'city': '420100',
        'key': '8325164e247e15eea68b59e89200988b'
    }
    response = requests.get(url, timeout=10, headers=headers, params=data)
    try:
        pois_0 = response.json()['pois'][0]
    except Exception as e:
        pois_0 = {
            'name': '0',
            'type': '0',
            'adname': '0',
            'location': '0',
        }

    pois_name = pois_0['name']
    type = pois_0['type']
    adname = pois_0['adname']
    location = '"{0}"'.format(pois_0['location'])
    # location = response.json()['geocodes'][0]
    # district = location['district']
    # if type(district) == list:
    #     district = '未知区'
    # zuobiao = '"{0}"'.format(location['location'])
    return (pois_name, type, adname, location)


if __name__ == '__main__':
    test = get_zuobiao('盘龙古肆·巢立方')
    print(test)
    # print((test[0]))
    # print((test[1]))
