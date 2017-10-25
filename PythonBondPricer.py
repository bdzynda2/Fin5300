#Bond Pricer

import numpy as np 

def pv(payment, ytm, frequency, fracAct, periods):
    pv = [] 
    payment = payment / freq
    for i in range(periods):
        pvCoupon = payment / ( 1 + ytm/frequency)**(fracAct+i)
        pv.append(pvCoupon)
    pvCoupon = sum(pv)
    pvFace = 100 / (1+ytm/frequency) ** (fracAct + i)
    pv = pvCoupon + pvFace
    return pv


lastCouponInput = input("\nEnter the Last Coupon (YYYY-MM-DD): ")

lastCoupon = np.datetime64(lastCouponInput)

nextCouponInput = input("\nEnter the Next Coupon Date (YYYY-MM-DD): ")

nextCoupon = np.datetime64(nextCouponInput)

settleDateInput = input("\nEnter the Settlement Date: (YYYY-MM-DD): ")

settleDate = np.datetime64(settleDateInput)

remainingDays = nextCoupon-settleDate
totalDays = nextCoupon - lastCoupon
fractionalPeriod = remainingDays/totalDays

print("\nRemaining Days: ", remainingDays)

print("\nTotal Days: ", totalDays)

print("\nThe fractional period is ", fractionalPeriod)

print("\nAssume $100.00 FV\n")

CouponPayment = float(input("\nEnter the Coupon Payment in Dollars: $ "))
YTM = float(input("\nEnter the YTM as a decimal: ")) 
freq = int(input("\nEnter the coupon frequency periods per year: "))
n = int(input("\nEnter the total periods: "))


presentValue = pv(CouponPayment, YTM, freq, fractionalPeriod, n)

print("\nThe Present Value of the Bond is $", presentValue)
