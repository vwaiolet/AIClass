import csv

pofol = open('C:/Users/user/Desktop/깃 과제/23y3m15d/csv/portfolio.csv')
rpofol = csv.reader(pofol)
next(rpofol)

pre_stock = []
pre_total = 0
for line in rpofol:
    pre_stock.append(line)
    
#print(pre_stock)

for i in range(len(pre_stock)):
    for j in range(1, 2):
        pre_total += (float(pre_stock[i][j]) * float(pre_stock[i][j+1]))

print('기존 total price : ', pre_total)

update = open('C:/Users/user/Desktop/깃 과제/23y3m15d/csv/prices.csv')
rupdate = csv.reader(update)

upd_price = []
had_stock = ['AA', 'IBM', 'CAT', 'MSFT', 'GE']
upd_stock = []
upd_total = 0
#for line in rupdate:
#    upd_stock.append(line)

#print(upd_stock)

for price in rupdate:
    upd_stock.append(price)

print(upd_stock)