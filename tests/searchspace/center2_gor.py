import os
import copy
import numpy as np

if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.misc.simtime import Simtime

#print('Node 1')
#print('{}'.format(300+(3700-300)*0.00))
#print('{}'.format(300+(3700-300)*0.25))
#print('{}'.format(300+(3700-300)*0.50))
#print('{}'.format(300+(3700-300)*0.75))
#print('{}'.format(300+(3700-300)*1.00))

print('Node 11')
#print('{}'.format(300+(2000-300)*0.00))
print('{}'.format(300+(2000-300)*0.25))
#print('{}'.format(300+(2000-300)*0.50))
print('{}'.format(300+(2000-300)*0.75))
#print('{}'.format(300+(2000-300)*1.00))

print('Node 12')
#print('{}'.format(2000+(3700-2000)*0.00))
print('{}'.format(2000+(3700-2000)*0.25))
#print('{}'.format(2000+(3700-2000)*0.50))
print('{}'.format(2000+(3700-2000)*0.75))
#print('{}'.format(2000+(3700-2000)*1.00))
