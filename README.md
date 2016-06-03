# LASER-driftcards
Python toolbox to process and analyze data from driftcards deployed during LASER P3. The library containts scripts that allows to work on bamboo plates _identification_, _rectification_ given INS data and _dispersion statistics analysis_.

The toolbox is organized in two main modules: __XY__ and __INS__

## XY
Includes all the subroutines to work on aerostat pictures, convert these into x,y paper plates positions, and perform georectification of the positions.

## INS
Includes all the subroutines required to deal with the INS (Internal Navigation System) data. These includes subroutines that allow to extract pitch, roll, heading, altitude and position (lat, lon) of the aerostat for any given picture.

Subroutines to compute Lagrangian statistics are stored into `stats.py` and include to read/write IO a subroutine to compute _cloud dispersion_.

## Example
A typical workflow would be something like the following.

### Driftcards identification
First operation would be to indentify the drifcards from the original images. A script to do this would look like this,

```python
import numpy as np
import scipy.io
import glob
from driftcardslib.XY import color_processing
from driftcardslib.XY import image_processing
from driftcardslib.XY import IO

import matplotlib.pyplot as plt

exp = 'F8'

files = np.sort(glob.glob('/home/jmensa/LASER/data/P3/img/'+exp+'/LASER_'+exp+'_*.jpg'))

a_t = []
b_t = []
t_t = []

for filename in files[:]:
 print filename
 frame = plt.imread(filename)

# remove M8
 frame = frame[1000:,:,:] # 1000 for most exp, 500 for F4

 mask, delta_s = color_processing.glare(frame,99.98) #99.99 for F4, 99.98 for F8, 99.999 for F10
 X,Y = image_processing.masking(mask,delta_s)

 path = 'csv/XY/LASER_'+exp+'_'+filename[-8:-4]+'_XY.csv'
 print path
 IO.writeXY(path,(X,Y))
```
