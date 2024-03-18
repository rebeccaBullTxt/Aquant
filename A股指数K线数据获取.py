from settings import EASTMONEY_INDEX_SYMBOL, EASTMONEY_FUQUAN_TYPE, EASTMONEY_KLINES_TYPE


# 构建URL
def func(eastmoney_symbol, fuquan_type, klines_type, klines_num=50000):
    """
    5分钟以上K线数据接口
    """
    klines_url = (f"https://push2his.eastmoney.com/api/qt/stock/kline/"
                  f"get?secid={eastmoney_symbol}"
                  f"&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61"
                  f"&klt={klines_type}&fqt={fuquan_type}&end=20500101&lmt={klines_num}")
    return klines_url


def func2(eastmoney_symbol, ndays=5):
    """
    1分钟K线数据接口
    """
    klines_url = f"https://push2his.eastmoney.com/api/qt/stock/trends2/get?fields1=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13&fields2=f51,f52,f53,f54,f55,f56,f57,f58&ndays={ndays}&secid={eastmoney_symbol}"
    return klines_url


if __name__ == '__main__':
    klines_type = EASTMONEY_KLINES_TYPE.get('日K')  # k线类型，101是日k线数据
    fuquan_type = EASTMONEY_FUQUAN_TYPE.get('前复权')  # 复权类型
    sh_symbol = EASTMONEY_INDEX_SYMBOL.get('上证指数')
    sz_symbol = EASTMONEY_INDEX_SYMBOL.get('深成指数')
    print(func(eastmoney_symbol=sh_symbol,fuquan_type=fuquan_type, klines_type=klines_type))
    print(func(eastmoney_symbol=sz_symbol,fuquan_type=fuquan_type, klines_type=klines_type))
