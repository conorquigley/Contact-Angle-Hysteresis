#!/bin/bash

decomposePar > log.decomposePar 2>&1
mpirun -np 14 interKistlerFoam -parallel > log.interKistlerFoam & # Ensure the number of cores here, 14 as written here, is the same as the decomposePar script.
reconstructPar > log.reconstructPar 2>&1
