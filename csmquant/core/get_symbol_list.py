import math
import pandas as pd

from csmquant.core.get_web_json_data import get_web_content


def get_symbol_list_from_eastmoney():
    # 定义一个空列表存储股票代码
    symbol_list = []
    # url
    base_url = 'http://push2.eastmoney.com/api/qt/clist/get?pn={}&pz=20&po=1&np=1&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152'
    page1_url = base_url.format(1)

    # 获取第一页的数据
    content1 = get_web_content(url=page1_url)

    df1 = pd.DataFrame(data=content1['data']['diff'])
    symbol_list.extend(df1['f12'].to_list())

    # 获取股票数量
    symbol_num = content1['data']['total']
    print(f"总共{symbol_num}只股票")
    # 计算股票代码的页数
    page_num = math.ceil(symbol_num / 20)

    # 循环计算剩下的页
    for i in range(2, page_num+1):
        print(f'第{i}页股票代码获取中，总共{page_num}页')
        url = base_url.format(i)
        content = get_web_content(url=url)
        df = pd.DataFrame(data=content['data']['diff'])
        symbol_list.extend(df['f12'].to_list())

    return symbol_list


if __name__ == '__main__':
    symbol_list = get_symbol_list_from_eastmoney()
    print(symbol_list)
    print(len(symbol_list))

    # 验证是否有重复数据
    new_list = list(set(symbol_list))
    print(len(new_list))
