# Lab 3 

# Part 1 Classifying speeds
num = []
danger = []
warning = []
safe = []

safeLimit = int(input("Enter safe limit: "))
warningLimit = int(input("Enter warning limit: "))

while num != -1:
    num = float(input("Enter number "))
    if num >= 0 and num <= safeLimit:
        safe.append(num)
    elif num > safeLimit and num <= warningLimit:
        warning.append(num)
    elif num > warningLimit:
        danger.append(num)

print(safe)
print("there are",len(safe)," safe sensor readings")

print(warning)
print("there are",len(warning)," warning sensor readings")

print(danger)
print("there are",len(danger)," danger sensor readings")



# Part 2 Pick a stock a write it's new stock price
stocks = ['IBM', 'AAPL', 'GOOG', 'FB', 'SMSN', 'INTC', 'MCD', 'TWTR']
stockPrices = [23.4, 24.5, 25.3, 56.7, 89.4, 45.3, 43.6, 67.4]

name = (input("Enter the stock name: "))
newPrice = 0
pIncrease = int(input("Enter the percentage increase: "))

i=0 
found = False
while i < len(stocks) and found == False:
      if stocks[i] == name:
          newPrice = stockPrices[i]+((pIncrease/100) * stockPrices[i])
          stockPrices[i] = round(newPrice)
          found = True
      else:
          i = i + 1

if not found:
    print("stock not found")
else:
    print(stocks)
    print(stockPrices)


    
# Part 3 Combine two lists, then sort them

list1 = [1, 4, 6, 7, 9, 11, 15]
list2 = [2, 3, 4, 5, 10, 11, 12]

list3 = list1 + list2
list3.sort()

print(list3)

