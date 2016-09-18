```python
import thinkstats2
import nsfg
import math

df = nsfg.ReadFemPreg()
df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0 #calculate totalwgt from lb + (oz/16)

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]  #isolate live births
firsts = live[live.birthord == 1] #isolate first births
others = live[live.birthord != 1] #isolate multiple births

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
n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)

# calculate Cohen Effect Size by Weight
pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
d_wgt = diff / math.sqrt(pooled_var)
print d_wgt

# compare d_wgt to d value from prglnth (d_prg?)

diff2 = firsts.prglngth.mean() - others.prglngth.mean()
var3 = firsts.prglngth.var()
var4 = firsts.prglngth.var()
n3, n4 = len(firsts.prglngth), len(others.prglngth)
pooled_var2 = (n3 * var3 + n4 * var4) / (n3 + n4)
d_prg = diff2 / math.sqrt(pooled_var2)
print d_prg

# d_wgt = -0.08867  vs. d_prg = 0.02795
```
