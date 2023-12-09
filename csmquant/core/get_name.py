import pandas as pd
from .format_symbol import after_l_format_symbol
from .get_web_json_data import get_web_content


def get_history_name(symbol):
    """
    # 获取股票历史名称
    :param symbol:
    :return:
    """

    f_symbol = after_l_format_symbol(symbol)
    url = f'https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPT_IPO_ABSTOCK&columns=SECURITY_CODE,CHANGE_DATE,CHANGE_AFTER_FN,CHANGE_AFTER_AB,TRADE_MARKET_TYPE,RANK,SECUCODE&quoteColumns=&filter=(SECUCODE=%22{f_symbol}%22)&pageNumber=1&pageSize=100&sortTypes=1&sortColumns=CHANGE_DATE&source=QuoteWeb&client=WEB'

    content = get_web_content(url=url)['result']['data']
    df = pd.DataFrame(content)
    df.rename(columns={'CHANGE_DATE': 'timestamp', 'CHANGE_AFTER_FN': 'name'}, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df[['timestamp', 'name']]

    return df


if __name__ == '__main__':
    df = get_history_name('000002')
    print(df)