# report.py

import fileparse
from stock import Stock

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name', 'shares', 'price'],
                                        types=[str, int, float])

    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for i in portfolio:
        current_price = prices[i.name]
        change = current_price - i.price
        summary = (i.name, i.shares, current_price, change)
        report.append(summary)

    return report

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    print('%10s' % 'Name', '%10s' % 'Shares', '%10s' % 'Price', '%10s' % 'Change')
    print('---------- ' * 4)
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolio, prices)

    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys

    main(sys.argv)
