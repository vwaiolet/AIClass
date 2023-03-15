import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(stock)
            
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

portfolio = read_portfolio('C:/Users/user/Desktop/깃 과제/23y3m15d/csv/portfolio.csv')
prices = read_prices('C:/Users/user/Desktop/깃 과제/23y3m15d/csv/prices.csv')

total_cost = 0.0
for i in portfolio:
    total_cost += (i['shares'] * i['price'])
#print(total_cost)

#print(prices)
total_value = 0.0
# portfolio의 share * prices의 가격
for i in portfolio:
    if i['name'] in prices:
        total_value += (i['shares'] * prices[i['name']])
        #print(i['shares'], prices[i['name']])

print('Current value', total_value)

print('Gain', total_value - total_cost)