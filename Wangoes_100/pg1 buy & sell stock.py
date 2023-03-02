prices = [7,1,5,3,6,4]
maxProfit = 0
minPurchase = prices[0]
for i in range(1, len(prices)):
    sell_profit=prices[i]-minPurchase
    if sell_profit> maxProfit:
        maxProfit=sell_profit
    if prices[i]<minPurchase:
        minPurchase=prices[i]

print(maxProfit)