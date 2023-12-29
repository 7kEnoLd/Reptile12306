# 以用request模块
import requests
# 引用json模块
import json
# 取得编码模块
from urllib.parse import urlencode

'''
    @headers:request请求的请求头
    请求信息：
    F12，启动开发者模式，在参数里就可以找到请求头信息
    疑问：有方法自动读取headers里的参数吗
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 '
                  'Safari/537.36 Edg/121.0.0.0',
    'Cookie': '_uab_collina=170382163387775172115723; JSESSIONID=C082D1145114145CC6F1E8DB6F06173D; '
              'BIGipServerpassport=887619850.50215.0000; guidesStatus=off; highContrastMode=defaltMode; '
              'cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=1742274826.50210.0000; '
              '_jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; '
              '_jc_save_toDate=2023-12-29; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5317%u4EAC%2CBJP; '
              '_jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2024-01-02; _jc_save_fromDate=2024-01-04'
}

'''
    @data_dict:key_value:
    经过多次的请求测试，发现get参数改变的都是出发地，到达地，出发时间
    所以确定字典有三个键值对
    即：fromwhere,towhere,startime
'''


def get_tickets(fromwhere, towhere, startime):
    # 数据字典
    data = {
        'leftTicketDTO.train_date': startime,
        'leftTicketDTO.from_station': fromwhere,
        'leftTicketDTO.to_station': towhere,
        'purpose_codes': 'ADULT',
    }
    # 构造请求链接：地址 + 参数 （startime,fromwhere,wowhere）
    request_url = 'https://kyfw.12306.cn/otn/leftTicket/query?' + urlencode(data)
    # 利用json.loads()将其他(这里是文本类型)类型的数据转化成Python类型（这里是转成字典）
    response = json.loads(requests.get(request_url, headers=headers).text)
    # 构造结果字典
    result = response['data']['result']
    # 创建新的字典，并且遍历字典，除去列车停运数据
    new_list = []
    for item in result:
        if not '列车停运' in item:
            new_list.append(item)
        else:
            pass
    # @return:dict{}
    return new_list
