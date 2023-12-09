def l_format_symbol(symbol):
    """
    格式化股票代码
    SH600519
    SZ000002
    BJ831278
    """
    if symbol.startswith('6'):
        symbol = 'SH' + symbol
    elif symbol.startswith('3') or symbol.startswith('0'):
        symbol = 'SZ' + symbol
    elif symbol.startswith('4') or symbol.startswith('8'):
        symbol = 'BJ' + symbol

    return symbol


def n_format_symbol(symbol):
    """
    格式化股票代码
    0.831278
    1.605178
    0.002699
    """
    if symbol.startswith('6'):
        symbol = '1.' + symbol
    elif symbol.startswith('3') or symbol.startswith('0'):
        symbol = '0.' + symbol
    elif symbol.startswith('4') or symbol.startswith('8'):
        symbol = '0.' + symbol

    return symbol


def after_l_format_symbol(symbol):
    """
    格式化股票代码
    SH600519
    SZ000002
    BJ831278
    """
    if symbol.startswith('6'):
        symbol = symbol + '.SH'
    elif symbol.startswith('3') or symbol.startswith('0'):
        symbol = symbol + '.SZ'
    elif symbol.startswith('4') or symbol.startswith('8'):
        symbol = symbol + '.BJ'

    return symbol