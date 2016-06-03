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
import glob
from driftcardslib.XY import color_processing
from driftcardslib.XY import image_processing
from driftcardslib.XY import IO

exp = 'F8'

files = np.sort(glob.glob('./img/'+exp+'/LASER_'+exp+'_*.jpg'))

a_t = []
b_t = []
t_t = []

for filename in files[:]:
 print filename
 frame = plt.imread(filename)

 # dirty and cheap way to remove Masco 8 from the frame. It tends to be always on top of the frame.
 frame = frame[1000:,:,:] # 1000 for most experiments, 500 for F4.


 # the thresholding value for glare is sensitive
 mask, delta_s = color_processing.glare(frame,99.98) #99.99 for F4, 99.98 for F8, 99.999 for F10
 X,Y = image_processing.masking(mask,delta_s)

 path = './csv/XY/LASER_'+exp+'_'+filename[-8:-4]+'_XY.csv'
 print path
 IO.writeXY(path,(X,Y))
```

### Compute INS data for each frame
INS data comes in high frequency data which needs to synchronized to the timestamp of the images. This is quite triky as different experiments were performed with different configurations. Here is an example of how to do it.

```python
import numpy as np
import glob
import driftcardslib.INS.IO as INSIO
import driftcardslib.INS.time as INStime
import datetime

exps = ['F8','F10']

for exp in exps:

 # INS and timestamp are not aligned. Each experiment has a different timeGap.

 Sunday,shift = INStime.timeGap(exp)

 file_INS = '/home/jmensa/LASER/scripts_LASER/P3/INS/'+exp+'_INS_NMEA_LOG.txt'

 INS_all = INSIO.read_INS_all(file_INS)

 files = np.sort(glob.glob('/home/jmensa/LASER/data/P3/img/'+exp+'/LASER_'+exp+'_*.jpg'))

 for filename in files[:]:
  fileout = './csv/INS/LASER_'+exp+'_'+filename[-8:-4]+'_INS.csv'
  print fileout

  time_frame = INStime.timeframe(filename)
  time_INS = INStime.SOW2UTC(INS_all[:,6],Sunday,shift)

  INSIO.write_INS_frame(INS_all,time_INS,time_frame,fileout)

```

### Georectify driftcard positions
Given INS data, we now want to project the XY positions of the driftcards to a UTM grid. A script to do that would look like the following,

```python
import numpy as np
import driftcardslib.XY.rectify as rectify
import driftcardslib.XY.IO as XYIO
import driftcardslib.INS.IO as INSIO
import glob

exps = ['F8','F10']

f_lens = 17 #mm

for exp in exps:

 files = np.sort(glob.glob('./csv/XY/LASER_'+exp+'*_XY.csv'))
 files_INS = np.sort(glob.glob('./csv/INS/LASER_'+exp+'*_INS.csv'))

 ny = 5792
 nx = 8688

 for n in range(len(files)):
  filename = files[n]
  print filename

  X,Y = XYIO.readXY(files[n])

  INS = XYIO.readXY_INS(files_INS[n])
  
  # comp_ang_XY generates a map of the azimuthal angles between lens and driftcard given a lens focal lenght
  [angx,angy] = rectify.comp_ang_XY(f_lens,[nx,ny],X,Y)

  # dan_map_image takes angx, angy, roll, pitch, heading, elevation. Heading was bad during F8 and F10.
  [Xr,Yr] = rectify.dan_map_image(angx,angy,float(INS[3]),float(INS[4]),0,float(INS[2])) 

  fileout = './csv/XY/LASER_'+exp+'_'+files[n][-11:-7]+'_XYr.csv'
  print fileout

  XYIO.writeXY(fileout,(Xr,Yr))

```

### Compute dispersion
Once we have the georectified positions we can compute cloud dispersion.

```python
import numpy as np
import glob
import driftcardslib.XY.IO as IO
import driftcardslib.stats as stats

exps = ['F8','F10']

for exp in exps:

 files = np.sort(glob.glob('./csv/XY/LASER_'+exp+'_*XYr.csv'))

 a_t = []
 b_t = []
 t_t = []

 for filename in files[:]:
  print filename

  X,Y = IO.readXY(filename)
  
  # cloud dispersion is computed with the method of the principal axes
  theta,a,b = stats.princax(X,Y) # angle, a, b

  a_t.append(a)
  b_t.append(b)
  t_t.append(float(filename[-12:-8])*15)

 fileout = './csv/cloud_dispersion_'+exp+'_XY.csv'
 stats.writeDisp(fileout,t_t,a_t,b_t)
```
