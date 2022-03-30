
import json
import re
import requests


'''
基金代码、名称、简拼进行基金搜索
'''
# search = '诺安成长混合'
# url = 'http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchAPI.ashx?m=1&key=' + search  #
#
# result = requests.post(url)  # 发送请求
# print('##############查询结果##############')
# print(result.text)  # 返回数据
'''

通过基金编码获取估值
'''
amount=[41079,35980,2707,14024,35073,3282,3930,1085,4799,2294,5645,1985,3102]
code_list=['320007','400015','002984','011103','003096','001938','005827','110022','161122','168203','005693','008618','005224']
jz_list=[]
for n in range(len(code_list)):
    url = 'http://fundgz.1234567.com.cn/js/%s.js' % code_list[n]
    result = requests.get(url)  # 发送请求
    #print(result.text)
    data = json.loads(re.match(".*?({.*}).*", result.text, re.S).group(1))
    # print('##############基金详情##############')
    income_value = amount[n]*float(data['gszzl'])/100
    print('基金名称：%s' % data['name'], '估算增量：%s%%' % data['gszzl'], '基金收入：%s' % income_value)
    # print(float(data['gszzl'])/100)
    # print('{:.2%}'.format(float(data['gszzl'])/100))
    jz_list.append((float(data['gszzl'])/100))


income=int(sum(map(lambda x,y:x*y,amount,jz_list)))
print("今天估值收益：",income)
print("爬取时间： %s" % data['gztime'])
