import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.misc.simtime import Simtime


st = Simtime((2022, 4, 30), (2046, 9, 30), 2038)

lst = st.simtime().split('\n')

print(lst[int(len(lst)*1/4)]); print(lst[int(len(lst)*3/4)])

lst1, lst2 = lst[:int(len(lst)*1/2)], lst[int(len(lst)*1/2):]

print(lst1[int(len(lst1)*1/4)]); print(lst1[int(len(lst1)*3/4)])
print(lst2[int(len(lst2)*1/4)]); print(lst2[int(len(lst2)*3/4)])
