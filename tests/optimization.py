import random
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from simulation.manager.template_manager import TemplateManager

MARKS = []
MARKS.append('#PRK014_Z1_GOR#')
MARKS.append('#PRK014_Z2_GOR#')
MARKS.append('#PRK014_Z3_GOR#')
MARKS.append('#PRK028_Z1_GOR#')
MARKS.append('#PRK028_Z2_GOR#')
MARKS.append('#PRK028_Z3_GOR#')
MARKS.append('#PRK045_Z1_GOR#')
MARKS.append('#PRK045_Z2_GOR#')
MARKS.append('#PRK045_Z3_GOR#')
MARKS.append('#PRK052_Z1_GOR#')
MARKS.append('#PRK052_Z2_GOR#')
MARKS.append('#PRK052_Z3_GOR#')
MARKS.append('#PRK060_Z1_GOR#')
MARKS.append('#PRK060_Z2_GOR#')
MARKS.append('#PRK060_Z3_GOR#')
MARKS.append('#PRK061_Z1_GOR#')
MARKS.append('#PRK061_Z2_GOR#')
MARKS.append('#PRK061_Z3_GOR#')
MARKS.append('#PRK083_Z1_GOR#')
MARKS.append('#PRK083_Z2_GOR#')
MARKS.append('#PRK083_Z3_GOR#')
MARKS.append('#PRK084_Z1_GOR#')
MARKS.append('#PRK084_Z2_GOR#')
MARKS.append('#PRK084_Z3_GOR#')
MARKS.append('#PRK085_Z1_GOR#')
MARKS.append('#PRK085_Z2_GOR#')
MARKS.append('#PRK085_Z3_GOR#')

CHOICES = list(map(str,[300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2400, 2700, 2900, 3100, 3300]))

N_ITERATION = 1
N_SAMPLE = 5

for i in range(N_ITERATION):    
    for j in range(N_SAMPLE):
        tm = TemplateManager(template_file_path='H:/DEV_AREA/templates/U2DBO_IM80_E0_WAG_IW.dat.tlp')
        tm.replace_mark(MARKS, random.choices(CHOICES, k=len(MARKS)))
        tm.write(file_path='H:/DEV_AREA/iteration{:04d}/run{:04d}.dat'.format(i+1,i+j+1))