prices = [7,6,4,3,1]
output = 0
result = []
for i in range (len(prices)):
    j = i + 1
    while j < (len(prices)):
        if prices[i] - prices[j] <= 0:
            result.append(abs(prices[i] - prices[j]))
        else:
            result.append(0)
            #print("Buy on day", i, "and sell on day", j, "and profit", abs(prices[i] - prices[j]), )
            #print("Buy on day",prices[i], "and sell on day" ,prices[j],"and profit",abs(prices[i-j]),)
        j += 1
print(max(result))