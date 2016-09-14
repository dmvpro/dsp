import math
import thinkstats2
import first


def EffectSizeWeight(live, firsts, others):
    # calculate mean weight for live births, first births & other births
    mean1 = live.totalwgt_lb.mean()
    mean2 = firsts.totalwgt_lb.mean()
    mean3 = others.totalwgt_lb.mean()

    # calculate difference between firsts and others 
    diff = mean2 - mean3

    # calculate variance of firsts & others
    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    # assign n_ as len(var_)
    n1, n2 = len(var1), len(var2)

    # calculate Cohen Effect Size by Weight
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d_wgt = diff / math.sqrt(pooled_var)
    return d_wgt

# compare d_wgt to d value from prglnth (d_prg?)
