#Considering we'll calculate annual earnings a few times, we here
#define a function that will do it so we can reuse it later easily
def ann_earnings(capital, rate):
    annual_earnings = round(capital * (rate/100), 3)
    return(annual_earnings)

initial_investment = float(input("Initial investment: "))
return_rate = float(input("Return rate in %: "))

print("Annual earnings: " + str(ann_earnings(initial_investment, return_rate)))

initial_investment += 5000
return_rate += 2

print("New annual earnings: " + str(ann_earnings(initial_investment, return_rate)))

#We here update the capital with this year's earnings
initial_investment = initial_investment + ann_earnings(initial_investment, return_rate)
print("New total capital: " + str(initial_investment))

#Here, we take 10% of the total capital
initial_investment = initial_investment*0.9
#We decrease the rate by 1%
return_rate -= 1
print("New total capital: " + str(initial_investment))
print("New annual earnings: " + str(ann_earnings(initial_investment, return_rate)))