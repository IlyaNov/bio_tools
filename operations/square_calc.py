import math 

def __calc(mkm_per_d,d_amount):
    '''return square in m^2'''
    d_mkm = mkm_per_d * d_amount
    d_mkm /= 1e6
    return d_mkm ** 2 * math.pi

def calculation(experiments,mkm_per_d):
    for exp in experiments:
        experiments[exp]['square'] = __calc(mkm_per_d,experiments[exp]['dim'])
