#Bond Pricer

import numpy as np

"""
lastcoupon = np.datetime64('2017-02-10')
nextcoupon = np.datetime64('2017-08-10')
settledate = np.datetime64('2017-02-24')

def pv(payment, ytm, frequency, fracAct, periods):
    pv = [] 
    for i in range(periods):
        pvCoupons = payment / ( 1 + ytm/frequency)**(fracAct+i)
        pv.append(pvCoupon)
    pvCoupon = sum(pv)
    pvFace = face / (1+ytm/frequency) ** (fracAct + i)
    pv = pvCoupons + pvFace
    return pv



"""

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
