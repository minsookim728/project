class True_range():
    """
    Class constructor contains three variables. 
    stock_high and stock_low are the high and the low price of the day of the stock.
    stock_close is the close price of the stock from the previous day.
    execution function returns the true range of the price by subtracting the highest price and the lowest price of the day.
    if the closing price is greater than stock_high or less than stock_low, use this instead of that.
    """
    def __init__(self, stock_dict: dict, date_list: list):
        self.stock = stock_dict
        self.date = date_list


    def execution(self) -> dict:
        for i in range(1, len(self.date)):
            if self.stock[self.date[i]]['high'] >= self.stock[self.date[i-1]]['close'] and self.stock[self.date[i]]['low'] <= self.stock[self.date[i-1]]['close']:
                self.stock[self.date[i]]['indicator'] = self.stock[self.date[i]]['high'] - self.stock[self.date[i]]['low']
            elif self.stock[self.date[i]]['high'] < self.stock[self.date[i-1]]['close']:
                self.stock[self.date[i]]['indicator'] = self.stock[self.date[i-1]]['close'] - self.stock[self.date[i]]['low']
            elif self.stock[self.date[i]]['low'] > self.stock[self.date[i-1]]['close']:
                self.stock[self.date[i]]['indicator'] = self.stock[self.date[i]]['high'] - self.stock[self.date[i-1]]['close']
        return self.stock


class Simple_moving_average():
    """
    """
    def __init__(self, stock_dict: dict, date_list: list, analysis_size: int):
        self.stock = stock_dict
        self.date = date_list
        self.size = analysis_size
        
    def execution(self):
        pass
        


class Directional_indicator():
    """
    """
    def __init__(self, ):
        pass