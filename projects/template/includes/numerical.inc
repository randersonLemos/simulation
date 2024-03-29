NUMERICAL

*DTMAX       30.
*DTMIN    0.001

*WATER_FIX 4

*NORM *SATUR 0.12
*NORM *PRESS 40
*MAXCHANGE *SATUR 0.24
*MAXCHANGE *PRESS 80
*AIM *THRESH 0.1 0.1
*NORM *PBUB  40
*NORM *PDW   101
*NORTH       200
*ITERMAX     200
*NEWTONCYC   15

SOLVER PARASOL
PDEGAA 1
JACPAR ON
DPLANES 4
NCUTS 10
INAC-WELL-SO ON


