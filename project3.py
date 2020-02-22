from datetime import datetime, date, timedelta
import json
import api
import indicators
import signal_strategies


def execution():
    path_apikey = 'D:\\project_3\\project_3_mine\\apikey.txt'
    url_AV_api = 'https://www.alphavantage.co'
    symbol_stock = 'AAPL'
    date_start = '2020-02-15'
    date_end = '2020-02-19'
    command = 'TR <1.5 >0.5'.split()
    #Hello 

    api_key = get_apikey(path_apikey)
    #Concatenate the variables to create a full valid url
    full_url = url_AV_api + '/query?function=TIME_SERIES_DAILY&symbol=' + symbol_stock + '&outputsize=full&apikey=' + api_key
    #Get dictionary-type object
    stock_dict = api.get_result(full_url)
    #Get all days from the start date to the end date
    date_range = get_date_range(date_start, date_end)
    #Store info of selected stock into new dictionary.
    selected_dict = get_dict_in_range(date_range, stock_dict)
    #Extract days in the dict for ease usage
    stock_date_list = list(selected_dict.keys())
    selected_dict = analysis(command, selected_dict, stock_date_list)
    report(symbol_stock, selected_dict, stock_date_list)


def get_apikey(path_key: str) -> str:
    """Store the API Key from the txt file into a variable"""
    f = open(path_key, 'r')
    api_key = f.readline()
    f.close()
    return api_key


def analysis(command: list, stock_dict: dict, stock_date_list: list):
    if command[0] == 'TR':
        stock_dict = convert(stock_dict, stock_date_list)
        TR = indicators.True_range(stock_dict, stock_date_list)
        SignalObj = signal_strategies.True_range(TR.execution(), stock_date_list, command[1], command[2])
        signal_dict = SignalObj.execution()
        return signal_dict
    elif command[0] == 'MP':
        pass
    elif command[0] == 'MV':
        pass
    elif command[0] == 'DP':
        pass
    elif command[0] == 'DV':
        pass


def report(symbol: str, stock_dict: dict, date_list: list):
    print(symbol)
    print(len(date_list))
    print()
    header = 'Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell?'
    convert(stock_dict, date_list)
    print(header)
    for i in date_list:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(i, stock_dict[i]['open'], stock_dict[i]['high'], stock_dict[i]['low'], stock_dict[i]['close'], stock_dict[i]['volume'], stock_dict[i]['indicator'], stock_dict[i]['buy'], stock_dict[i]['sell']))


def get_date_range(start: str, end: str) -> list:
    date_list = []
    dt_start = datetime.strptime(start, '%Y-%m-%d')
    dt_start = dt_start.date()
    dt_end = datetime.strptime(end, '%Y-%m-%d')
    dt_end = dt_end.date()
    while dt_start != dt_end:
        date_list.append(str(dt_start))
        dt_start = dt_start + timedelta(days=1)
        if dt_start == dt_end:
            date_list.append(str(dt_end))
    return date_list


def get_dict_in_range(date_list: list, stock_dict: dict) -> dict:
    new_dict = {}
    for i in date_list:
        if i in stock_dict["Time Series (Daily)"]:
            new_dict[i] = {'open': stock_dict["Time Series (Daily)"][i]['1. open'], 'high': stock_dict["Time Series (Daily)"][i]['2. high'], 'low': stock_dict["Time Series (Daily)"][i]['3. low'], 'close': stock_dict["Time Series (Daily)"][i]['4. close'], 'volume': stock_dict["Time Series (Daily)"][i]['5. volume'], 'indicator': '', 'buy': '', 'sell': ''}
    return new_dict


def convert(stock_dict: dict, date_list: list):
    for i in date_list:
        if type(stock_dict[i]['open']) == str: 
            stock_dict[i]['open'] = float(stock_dict[i]['open'])
            stock_dict[i]['high'] = float(stock_dict[i]['high'])
            stock_dict[i]['low'] = float(stock_dict[i]['low'])
            stock_dict[i]['close'] = float(stock_dict[i]['close'])
            stock_dict[i]['volume'] = float(stock_dict[i]['volume'])
        else:
            stock_dict[i]['open'] = '{:.4f}'.format(stock_dict[i]['open'])
            stock_dict[i]['high'] = '{:.4f}'.format(stock_dict[i]['high'])
            stock_dict[i]['low'] = '{:.4f}'.format(stock_dict[i]['low'])
            stock_dict[i]['close'] = '{:.4f}'.format(stock_dict[i]['close'])
            stock_dict[i]['volume'] = '{:.4f}'.format(stock_dict[i]['volume'])
    return stock_dict


if __name__ == "__main__":
    execution()