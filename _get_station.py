# 引用request模块 -- 网络请求模块
import requests
# 引用re模块 -- 正则表达式
import re
# 引用easyGui模块，制作弹窗
import easygui as ea


# Function() -- 获取12306站点信息


def get_station():
    """
        @url：12306站点信息存储文件地址（即网络服务器文件目录）
        :return: station
    """
    # 车站信息的js文件，去12306的http的query找
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9295'
    # 爬取数据，并以txt问本形式返回
    response = requests.get(url).text
    # 用正则表达式匹配出name和referred（站点列表和简称列表）

    name = re.findall(r'.*?\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|', response)
    referred = re.findall(r'.*?\|.*?\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|', response)
    # 用zip打包信息，将信息打包成由元组构成的列表，在转成字典存储到本地文件里
    '''
    @zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    '''
    station = dict(zip(name, referred))
    '''
    1.以二进制形式打开新的文件，本地有文件就打开，没有就创建一个新的
    2.向文件写入获取内容
    3.关闭文件流
    '''

    file = open('D:\\Project\\PyCharm\\Reptile12306\\station.txt', 'w', encoding='utf-8')
    file.write(str(station))
    file.close()

    # 弹窗提示：站点信息爬取完成，并且已经存储在本地
    ea.msgbox(msg='----------------12306站点信息已经爬取完成----------------\n\n'
                  '-----------------稍后可查看关键词、词云图----------------\n\n', title='运行提示！',
              ok_button='查看关键字检索')
    # @return:
    return station
