# LASER-driftcards
Python toolbox to process and analyze data from driftcards deployed during LASER P3. The library containts scripts that allows to work on bamboo plates _identification_, _rectification_ given INS data and _dispersion statistics analysis_.

The toolbox is organized in two main modules: __XY__ and __INS__

## XY
Includes all the subroutines to work on aerostat pictures, convert these into x,y paper plates positions, and perform georectification of the positions.

## INS
Includes all the subroutines required to deal with the INS (Internal Navigation System) data. These includes subroutines that allow to extract pitch, roll, heading, altitude and position (lat, lon) of the aerostat for any given picture.

Subroutines to compute Lagrangian statistics are stored into `stats.py` and include to read/write IO a subroutine to compute _cloud dispersion_.
