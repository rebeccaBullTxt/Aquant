import os
import requests
import json

import pandas as pd

from csmquant.core.get_symbol_list import get_symbol_list_from_eastmoney
from csmquant.core.get_web_json_data import get_web_content
from settings import DATA_DIR, EASTMONEY_BONUS_COLUMNS

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.expand_frame_repr', False)


def get_bonus(symbol):
    base_url = "https://datacenter-web.eastmoney.com/api/data/v1/get?sortColumns=REPORT_DATE&sortTypes=-1&pageSize=100&pageNumber=1&reportName=RPT_SHAREBONUS_DET&columns=ALL&quoteColumns=&js=%7B%22data%22%3A(x)%2C%22pages%22%3A(tp)%7D&source=WEB&client=WEB&filter=(SECURITY_CODE%3D%22{}%22)"
    # 获取网络数据
    data = get_web_content(url=base_url.format(symbol))["result"]["data"]
    df = pd.DataFrame(data=data)

    # 列名重命名
    columns_list = list(EASTMONEY_BONUS_COLUMNS.keys())
    df = df[columns_list]
    df = df.copy()  # 我在抽取了原来DataFrame数据的几列后，对抽取后的数据进行赋值操作时弹出这个警告。这个是深浅拷贝的警告,我对其进行一次深拷贝即可解决，这种方式可能会失效。
    df.rename(columns=EASTMONEY_BONUS_COLUMNS, inplace=True)

    # 日期数据处理
    df['预案公告日'] = pd.to_datetime(df['预案公告日']).dt.date
    df['股权登记日'] = pd.to_datetime(df['股权登记日']).dt.date
    df['除权除息日'] = pd.to_datetime(df['除权除息日']).dt.date
    df['报告期'] = pd.to_datetime(df['报告期']).dt.date

    return df


if __name__ == '__main__':
    # 数据文件存储路径
    file_dir = os.path.join(DATA_DIR, '历年分红数据')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # 股票列表
    symbol_list = get_symbol_list_from_eastmoney()
    # symbol_list = ['000002']

    # 没有分红数据的文件存到这个文件里面
    not_bonus = os.path.join(file_dir, '没有分红数据的股票.txt')
    if os.path.exists(not_bonus):  # 如果第一次运行，有未分红的股票记录，删除他
        os.remove(not_bonus)

    # 循环下载分红数据
    for symbol in symbol_list:
        try:
            file_path = os.path.join(file_dir, symbol + '.csv')
            print(f"正在下载{symbol}历年分红数据")
            # 下载保存数据
            df = get_bonus(symbol)
            df.to_csv(path_or_buf=file_path, index=False, encoding='utf_8_sig')
        except TypeError:
            with open(not_bonus, mode='a') as f:
                f.write(symbol + '\n')

