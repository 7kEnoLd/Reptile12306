#对数据进行解码
#引用re模块 -- 正则表达式
import re
def decrypt(string):
    #指定匹配规则
    reg = re.compile('.*?\|预订\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*')
    '''
        正则匹配
        [0]:匹配所有数据
    '''
    result = re.findall(reg,string)[0]
    #返回匹配结果
    return result