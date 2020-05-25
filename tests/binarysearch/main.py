import copy
import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.misc.simtime import Simtime


st = Simtime((2022, 4, 30), (2046, 9, 30), 2038)

holder = []
holder.append(st.simtime().split('\n'))
curr = holder

count = 3
while count:
    tmp = []
    for lst in curr:
        tmp.append(lst[:int(len(lst)*1/2)])
        tmp.append(lst[int(len(lst)*1/2):])
    curr = tmp
    for lst in tmp:
        holder.append(lst)
    count -= 1

for lst in holder:
    stg = '{} {}'.format(lst[int(len(lst)*1/4)], lst[int(len(lst)*3/4)])
    print(stg)
