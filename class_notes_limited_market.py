####################################################################################
#Limited Market Game
# W. Neal - January 9, 2019
# Adapted from a spreadsheed-based game
# Companies compete for market share and profit by setting their prices strategically
######################################################################################





#Set the default values of the variables
teamNames = ["STEMBustion","Smarttrash", "Cherry Pi", "STEM Cells", "Bio Group", "Bananaoonana","SSE        "]
teamNames = ["SER","SIR","Integers"]  #The team names list is a list of strings
numTeams = len(teamNames)
population = 1000000
difficulty = 1
prices = [0]*numTeams
numRounds = 5



print("Welcome to the 'Limited Market Game!'  Teams need to decide on a price for their 'products' at the beginning of each round.  There are 1000000 customers who will choose to purchase products based on price - the lower the price, the more customers will choose a given product.  Can your company turn a profit after five rounds?")
totalProfit = [0]*numTeams
for r in range(0,numRounds):
    for i in range(0,numTeams):
        done = 0
        while done == 0:
            try:
                print("Please enter the price for ",teamNames[i])
                price = input()
                price = float(price)
                if price >0 and price<=100:
                    done = 1
            except: 
                print("Please enter a number between 1 and 100")
        prices[i] = price       
    priceAverage = sum(prices)/len(prices)
    print("The average price is: ", priceAverage)
    adjustment1 = []
    adjustment2 = []
    customers = []
    revenue = []
    expenses = []
    profit = []
    for i in range(len(prices)):
        adjustment1.append(priceAverage-prices[i])
        a1min = min(adjustment1)
    for i in range(len(prices)):
        adjustment2.append(adjustment1[i]-a1min+0.2*priceAverage)
    a2Sum = sum(adjustment2)
    for i in range(len(prices)):
        customers.append(int(adjustment2[i]*population/a2Sum))
    for i in range(len(prices)):
         revenue.append(prices[i]*customers[i])
    for i in range(len(prices)):
         expenses.append(5*population+customers[i]*difficulty)
    for i in range(len(prices)):
         profit.append(revenue[i]-expenses[i])
    for i in range(len(prices)):
         totalProfit[i]+=profit[i]
    print("Limited Market Game - Round ", r+1, " out of ",numRounds) 
    print("Team","\t","Price","\t", "Revenue","\t", "Expenses","\t","Profit","\t", 
"Total Profit")
    for i in range(len(prices)):
         print(teamNames[i],"\t",prices[i],"\t",revenue[i],"\t",expenses[i],"\t",profit[i],"\t",totalProfit[i])
    print("")
print("")
print("Limited Market Game - Final Results") 
print("Team","\t","Price","\t", "Revenue","\t", "Expenses","\t","Profit","\t", 
"Total Profit")
for i in range(len(prices)):
     print(teamNames[i],"\t",prices[i],"\t",revenue[i],"\t",expenses[i],"\t",profit[i],"\t",totalProfit[i])


     
