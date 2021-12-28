import numpy as np
from numpy import linalg as la

def comparison_series():
    series = []
    for k in range(50):
        series.append(1)
        i = 1
        while i <= 10:
            series[k] += (-1)**i*(k + 1)**i
            i += 1
    return series

def lin_solve(f,k):
    series_col = np.zeros(shape = (k,1))
    for i in range(k):
        series_col[i] = int(f[i])
    lin_eqs = np.zeros(shape = (k, k))
    for x in range(k + 1):
        y = 0
        while y < k:
            lin_eqs[x-1,y] = x**y
            y += 1
    best_fit = np.transpose(la.solve(lin_eqs,series_col))
    best_fit = best_fit[0]
    return best_fit

def main(degrees):
    f = comparison_series()
    sum = 0
    k = 1
    while k < degrees + 2:
        poly_coeffs = lin_solve(f,k)
        n_deg_sol = []
        for k in range(degrees + 2):
            d = 0
            n_deg_sol.append(0)
            for c in poly_coeffs:
                n_deg_sol[k] += c*(k + 1)**d
                d += 1
            if round(n_deg_sol[k]) != f[k]:
                sum += round(n_deg_sol[k])
                break
        k += 1
    return sum

print(main(10))