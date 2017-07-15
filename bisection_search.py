monthly_interest_rate = annualInterestRate/12
lower=balance/12
upper=(balance*(1+annualInterestRate/12)**12)/12
while True:
    newbalance=balance   
    x=(lower+upper)/2
    for i in [i+1 for i in range(12)]:
       newbalance-=x
       newbalance*=(1+annualInterestRate/12)
    if newbalance<=0:
        if abs(newbalance)<=0.001:
            print ('Lowest Payment: ' + str(round(x,2)))
            break
        else:
            upper=x
    else:
        lower=x