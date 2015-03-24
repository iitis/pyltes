__author__ = 'mslabicki'

import math

def returnDistanceFromSNR(SINR, Ptx):
    lambda_val = 0.143
    s = 15.8
    a = 4.0
    b = 0.0065
    c = 17.1
    d = 10.8
    ht = 40
    hr = 1.5
    f = 2.1
    gamma = a - b*ht + c/ht
    Xf = 6 * math.log10( f/2 )
    Xh = -d * math.log10( hr/2 )

    R0 = 100.0
    R0p = R0 * pow(10.0,-( (Xf+Xh) / (10*gamma) ))

    N = -104.5
    alpha = 20 * math.log10( (4*math.pi*R0p) / lambda_val )
    R = R0 * math.pow(10, (Ptx-alpha-Xf-Xh-s-SINR - N)/(10*gamma))

    return R