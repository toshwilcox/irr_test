import numpy as np
from datetime import date
import statistics

#define the data set
cash_flow = [-1000, 350, 400, 500]
dates = [date(2019, 1, 1), date(2019, 3, 20), date(2019, 5, 25), date(2019, 7, 2)]



def newton(f, df, x0, tol, maxiter):
    for i in range(maxiter):
        x1 = x0 - f(x0) / df(x0)
        print(x1)
        if (x1 - x0) < .001:
            return x1
        x0 = x1
    return x1

def range_finder(f):
    tens = np.linspace(0,100,11)
    tens_upper = [i for i in tens if f(i) > 0]
    tens_lower = [i for i in tens if f(i) < 0]
    range = [tens_upper[np.argmin([f(j) for j in tens_upper])], tens_lower[np.argmax([f(j) for j in tens_lower])] ]


    ones = np.linspace(min(range), max(range), 11)
    ones_upper = [i for i in ones if f(i) > 0]
    ones_lower = [i for i in ones if f(i) < 0]
    range = [ones_upper[np.argmin([f(j) for j in ones_upper])], ones_lower[np.argmax([f(j) for j in ones_lower])] ]

    dec = np.linspace(min(range), max(range), 101)
    dec_upper = [i for i in dec if f(i) > 0]
    dec_lower = [i for i in dec if f(i) < 0]
    range = [dec_upper[np.argmin([f(j) for j in dec_upper])], dec_lower[np.argmax([f(j) for j in dec_lower])] ]

    dec1 = np.linspace(min(range), max(range), 101)
    dec1_upper = [i for i in dec1 if f(i) > 0]
    dec1_lower = [i for i in dec1 if f(i) < 0]
    range = [dec1_upper[np.argmin([f(j) for j in dec1_upper])], dec1_lower[np.argmax([f(j) for j in dec1_lower])] ]

    return statistics.mean(range)


if __name__ == '__main__':
    nv = lambda rate: cash_flow[0] + (cash_flow[1] / (1+rate)**((dates[1]-dates[0]).days/365)) + (cash_flow[2] / (1+rate)**((dates[2]-dates[0]).days/365)) + (cash_flow[3] / (1+rate)**((dates[3]-dates[0]).days/365))
    derr_nv = lambda rate: (cash_flow[1] * -(((dates[1]-dates[0]).days/365))) * (1+rate)**((-(dates[1]-dates[0]).days/365) - 1 ) + (cash_flow[2] * -(((dates[2]-dates[0]).days/365))) * (1+rate)**((-(dates[2]-dates[0]).days/365) - 1) + (cash_flow[3] * -(((dates[3]-dates[0]).days/365))) * (1+rate)**((-(dates[3]-dates[0]).days/365) - 1)
    print("TEST NEWTON'S METHOD")
    newton_soln = newton(nv, derr_nv, .1, .001, 100)
    print("THIS IS THE XIRR ", newton_soln)
    print("THE NV FUNCTION EVALUATED AT ", newton_soln, " IS ", nv(newton_soln), "\n\n")

    print("TEST THE RANGE FINDER METHOD")
    range_finder_soln = range_finder(nv)
    print("THIS IS THE XIRR ", range_finder_soln)
    print("THE NV FUNCTION EVALUATED AT ", range_finder_soln, " IS ", nv(range_finder_soln))
