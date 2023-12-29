from _get_station import get_station
from _get_tickets import get_tickets
from GUI import get_list_from_gui
from decrypt import decrypt
from texttable import Texttable
import easygui as g
import sys
import datetime


# 获取信息函数
def get_message():
    _inputInfo = get_list_from_gui()

    fw = _inputInfo[0]
    tw = _inputInfo[1]
    st = _inputInfo[2]

    if st == '':
        # 如果没有输入时间，则当前日期为默认时间
        st = datetime.date.today()
        # 锁定参数
        return fw, tw, st
    else:
        today = datetime.date.today()
        date = str(today).split('-')
        list = st.split('-')
        # 未来多少天的逻辑我没管了，按着预售期来就完事
        if int(list[0]) < int(date[0]):
            exit("输入的年份不在我的查询范围之内")
        else:
            if int(list[0]) == int(date[0]) and int(list[1]) < int(date[1]):
                exit("你输入的月份不在我的查询范围之内")
            else:
                if int(list[0]) == int(date[0]) and int(list[1]) == int(date[1]) and int(list[2]) < int(date[2]):
                    exit("你输入的日期不在我的查询范围之内")
                else:
                    if int(list[1]) < 10 and int(list[1][0]) != 0:
                        list[1] = '0' + list[1]
                    if int(list[2]) < 10 and int(list[2][0]) != 0:
                        list[2] = '0' + list[2]
                    return fw, tw, list[0] + '-' + list[1] + '-' + list[2]


message = get_message()


def run():
    # 获取站点信息
    station_name = get_station()
    g.msgbox(msg='request Static : request success.\n\n'
                 '数据表生成成功', title='运行提示', ok_button='打印数据表')
    try:
        # result_list = []
        fromwhere = station_name[message[0]]
        towhere = station_name[message[1]]
        startime = message[2]
        # get_tickets()获得车票信息列表
        tickets = get_tickets(fromwhere, towhere, startime)
        print('===============================================================================')
        print('carNum'.center(8, '-'), end='')
        print('{0:{1}^9}'.format('始发站', chr(12288)), end='')
        print('{0:{1}^9}'.format('目的地', chr(12288)), end='')
        print('{0:{1}^9}'.format('sTime', chr(12288)), end='')
        print('{0:{1}^9}'.format('aTime', chr(12288)), end='')
        print('{0:{1}^9}'.format('bTime', chr(12288)))
        print('===============================================================================')

        for item in tickets:
            # 利用decrypt()函数解码result（网络请求里的result），解码后生成列表，存储到result中
            result = list(decrypt(item))
            # 遍历站点信息字典，存储到new_dict新字典里
            new_dict = {v: k for k, v in station_name.items()}
            # ----------result_test-----------#
            # 结果：
            # list列表：
            # ['G102', 'AOH', 'VNP', '06:26', '12:29', '06:03',  '有', '有', '13']
            # print(result)
            # -----------new_dict_test----------#
            # 结果：
            # dict字典：
            # {'VAP': '北京北', 'BOP': '北京东'...}
            # print(new_dict)
            '''
                将出发地、到达地的简称转换成中文

            '''
            # result列表准备就绪：
            result[1] = new_dict[result[1]]
            result[2] = new_dict[result[2]]

            rightWidth = 8
            print(result[0].center(rightWidth, '-'), end='')
            print('{0:{1}^9}'.format(result[1], chr(12288)), end='')
            print('{0:{1}^9}'.format(result[2], chr(12288)), end='')
            print('{0:{1}^9}'.format(result[3], chr(12288)), end='')
            print('{0:{1}^9}'.format(result[4], chr(12288)), end='')
            print('{0:{1}^9}'.format(result[5], chr(12288)))
            print('-------------------------------------------------------------------------------')
    except KeyError as k:
        print("I can't find the city %s" % k)


if __name__ == '__main__':
    run()
