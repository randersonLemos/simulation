import copy
import os
if os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in os.sys.path: os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from simulation.misc.simtime import Simtime

def five_points(lst):
    length = len(lst)
    den = 4
    return [lst[int((length-1)*num/den)] for num in range(den+1)]

st = Simtime((2022, 4, 30), (2046, 9, 30), 2038)
lst = []
for el in st.simtime().split('\n'):
    if '*WSRF' in el:
        pass
    else:
        lst.append(el)


#holder = []
#holder.append(st.simtime().split('\n'))
#curr = holder

#count = 4
#while count:
#    tmp = []
#    for lst in curr:
#        tmp.append(lst[:int(len(lst)*1/2)])
#        tmp.append(lst[int(len(lst)*1/2):])
#    curr = tmp
#    for lst in tmp:
#        holder.append(lst)
#    count -= 1
#
#
#llst = []
#for lst in holder:
#    llst.append('{} --> {} {}'.format(lst[int(len(lst)*1/2)].split('**')[0], lst[int(len(lst)*1/4)].split('**')[0], lst[int(len(lst)*3/4)].split('**')[0]))
#
#llst = sorted(llst)
#for el in llst:
#    print(el, file=open('out.txt', 'a'))
