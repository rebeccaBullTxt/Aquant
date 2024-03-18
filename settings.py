# 数据存储文件夹，需要自己修改
DATA_DIR = '/home/dell/Documents/data_csv'

# 东方财富分红数据列名
EASTMONEY_BONUS_COLUMNS = {
    "SECURITY_NAME_ABBR": "名称",
    "SECURITY_CODE": "股票代码",
    "BONUS_IT_RATIO": "送转总比例",
    "BONUS_RATIO": "送股比例",
    "IT_RATIO": "转股比例",
    "PRETAX_BONUS_RMB": "现金分红比例(10股)",
    "PLAN_NOTICE_DATE": "预案公告日",
    "EQUITY_RECORD_DATE": "股权登记日",
    "EX_DIVIDEND_DATE": "除权除息日",
    "REPORT_DATE": "报告期",
    "ASSIGN_PROGRESS": "方案进度",
    "IMPL_PLAN_PROFILE": "分配方案预案",
    "NOTICE_DATE": "最新公告日期",
    "EX_DIVIDEND_DAYS": "除权除息的天数",
    "BASIC_EPS": "每股收益(元)",
    "BVPS": "每股净资产(元)",
    "PER_CAPITAL_RESERVE": "每股公积金(元)",
    "PER_UNASSIGN_PROFIT": "每股未分配利润(元)",
    "PNP_YOY_RATIO": "净利润同比增长(%)",
    "TOTAL_SHARES": "总股本",
    "PUBLISH_DATE": "业绩披露日期",
    "DIVIDENT_RATIO": "股息率（%）",
    "D10_CLOSE_ADJCHRATE": "预案公告日后10日涨幅%",
    "BD10_CLOSE_ADJCHRATE": "股权登记日前10日涨幅%",
    "D30_CLOSE_ADJCHRATE": "除权除息日后30日涨幅%",
}

EASTMONEY_INDEX_SYMBOL = {
    "上证指数": "1.000001",
    "深成指数": "0.399001",
    "创业板指": "0.399006",
    "沪深300": "1.000300",
    "上证50": "1.000300",
    "科创50": "1.000688",
    "北证50": "0.899050",
}

"""
指数的额数据都是一样，不分复权不复权，默认选前复权1
"""
EASTMONEY_FUQUAN_TYPE = {
    "不复权": "0",
    "前复权": "1",
    "后复权": "2",
}

EASTMONEY_KLINES_TYPE = {
    "5分钟": "5",
    "15分钟": "15",
    "30分钟": "30",
    "60分钟": "60",
    "日K": "101",
    "周K": "102",
    "月K": "103",
}


