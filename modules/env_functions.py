__author__ = 'mslabicki'

import math

def returnDistanceFromSNR(expectedSignalLoss):
    lambda_val = 0.142758313333
    a = 4.0
    b = 0.0065
    c = 17.1
    d = 10.8
    s = 15.8

    ht = 40
    hr = 1.5
    f = 2.1
    gamma = a - b*ht + c/ht
    Xf = 6 * math.log10( f/2 )
    Xh = -d * math.log10( hr/2 )

    R0 = 100.0
    R0p = R0 * pow(10.0,-( (Xf+Xh) / (10*gamma) ))

    bandwidth=20
    k = 1.3806488 * math.pow(10, -23)
    T = 293.0
    BW = bandwidth * 1000 * 1000
    N = 10*math.log10(k*T) + 10*math.log10(BW)

    alpha = 20 * math.log10( (4*math.pi*R0p) / lambda_val )
    R = R0 * math.pow(10, (expectedSignalLoss - alpha-Xf-Xh-s - N)/(10*gamma))

    return R