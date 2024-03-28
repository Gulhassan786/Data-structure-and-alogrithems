
def finalPrices(prices):
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j]<= prices[i]:
                    prices[i] -= prices[j]
                    break
  
        return prices

finalPrices([8,7,4,2,8,1,7,7,10,1])