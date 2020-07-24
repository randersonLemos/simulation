import numpy

def intervals_limit(ini, end, n_int):
    q = numpy.power(end/ini, 1/n_int)
    return [int(ini*q**power) for power in range(n_int+1)]

def intervals_center(lst):
    lstt = []
    for a,b in zip(lst[:-1], lst[1:]):
        lstt.append(a)
        lstt.append(int((a+b)/2))
    lstt.append(b)
    return lstt

ini = 300
end = 3700
n_int = 2

n_levels = 2

for i in range(n_levels):


lst = intervals_limit(ini, end, n_int)
print(lst)
print(intervals_center(lst))
