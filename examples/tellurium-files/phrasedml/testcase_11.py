"""
RepeatedTask of repeatedTask
This is mainly used in multidimensional parameter scans.
The number of simulations can get very large very fast.
"""
from __future__ import print_function
import tellurium as te

antimonyStr = '''
model testcase_11()
  J0: S1 -> S2; k1*S1-k2*S2
  S1 = 10.0; S2 = 0.0;
  k1 = 0.5; k2=0.4
end
'''
phrasedmlStr = '''
  mod1 = model "testcase_11"
  sim1 = simulate uniform(0, 10, 100)
  task1 = run sim1 on mod1
  rtask1 = repeat task1 for k1 in uniform(0, 1, 2)
  rtask2 = repeat rtask1 for k2 in uniform(0, 1, 3)
  rtask3 = repeat rtask2 for S1 in [5, 10], reset=true
  plot "RepeatedTask of RepeatedTask" rtask3.time vs rtask3.S1, rtask3.S2
'''

# phrasedml experiment
exp = te.experiment(antimonyStr, phrasedmlStr)

# python code
import os
with open(os.path.realpath(__file__) + 'code.py', 'w') as f:
    f.write(exp._toPython(phrasedmlStr))

# execute python
import os
exp.execute(phrasedmlStr, workingDir=os.getcwd())
