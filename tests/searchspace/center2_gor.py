import numpy as np


def get_values(ini, end):
    return [ini + (end-ini)*el for el in [0.00, 0.25, 0.50, 0.75, 1.00]]


ini = 300
end = 3700
hold = [get_values(ini, end)]

n_levels = 5

for i in range(n_levels):
    print('Level {}'.format(i))
    lst = hold; print(lst)
    hold = []
    for _ini, _, middle, _, _end in lst:
        hold.append(get_values(_ini, middle))
        hold.append(get_values(middle, _end))



#print('Node 1')
#print('{}'.format(300+(3700-300)*0.00))
#print('{}'.format(300+(3700-300)*0.25))
#print('{}'.format(300+(3700-300)*0.50))
#print('{}'.format(300+(3700-300)*0.75))
#print('{}'.format(300+(3700-300)*1.00))
#
#print('Node 11')
#print('{}'.format(300+(2000-300)*0.00))
#print('{}'.format(300+(2000-300)*0.25))
#print('{}'.format(300+(2000-300)*0.50))
#print('{}'.format(300+(2000-300)*0.75))
#print('{}'.format(300+(2000-300)*1.00))
#
#print('Node 12')
#print('{}'.format(2000+(3700-2000)*0.00))
#print('{}'.format(2000+(3700-2000)*0.25))
#print('{}'.format(2000+(3700-2000)*0.50))
#print('{}'.format(2000+(3700-2000)*0.75))
#print('{}'.format(2000+(3700-2000)*1.00))

#print('Node 111')
##print('{}'.format(300+(2000-300)*0.00))
#print('{}'.format(300+(2000-300)*0.25))
##print('{}'.format(300+(2000-300)*0.50))
#print('{}'.format(300+(2000-300)*0.75))
##print('{}'.format(300+(2000-300)*1.00))
#
#print('Node 121')
##print('{}'.format(2000+(3700-2000)*0.00))
#print('{}'.format(2000+(3700-2000)*0.25))
##print('{}'.format(2000+(3700-2000)*0.50))
#print('{}'.format(2000+(3700-2000)*0.75))
##print('{}'.format(2000+(3700-2000)*1.00))
