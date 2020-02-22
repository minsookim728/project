class True_range():
    def __init__(self, stock_dict: dict, date_list: list,buy_threshold: str, sell_threshold: str):
        self.stock = stock_dict
        self.date = date_list
        self.buy = buy_threshold
        self.sell = sell_threshold


    def execution(self) -> dict:
        buy_ineq = ''
        sell_ineq = ''
        buy_thresh = ''
        sell_thresh = ''
        for i in self.buy:
            if i == '>' or i == '<':
                buy_ineq += i
            else:
                buy_thresh += i
        for j in self.sell:
            if j == '>' or j == '<':
                sell_ineq += j
            else:
                sell_thresh += j        
        buy_thresh = float(buy_thresh)
        sell_thresh = float(sell_thresh)
        for day in range(len(self.date)):
            if self.stock[self.date[day]]['indicator'] != '':
                if buy_ineq == '>':
                    if self.stock[self.date[day]]['indicator'] / self.stock[self.date[day-1]]['close'] > buy_thresh:
                        self.stock[self.date[day]]['buy'] == 'BUY'
                elif buy_ineq == '<':
                    if self.stock[self.date[day]]['indicator'] / self.stock[self.date[day-1]]['close'] < buy_thresh:
                        self.stock[self.date[day]]['buy'] == 'BUY'
                if sell_ineq == '>':
                    if self.stock[self.date[day]]['indicator'] / self.stock[self.date[day-1]]['close'] > sell_thresh:
                        self.stock[self.date[day]]['sell'] == 'SELL'
                elif sell_ineq == '<':
                    if self.stock[self.date[day]]['indicator'] / self.stock[self.date[day-1]]['close'] < sell_thresh:
                        self.stock[self.date[day]]['sell'] == 'SELL'
        return self.stock