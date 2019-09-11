# MAE345-Student
Source code assignments for MAE345.

This repository contains Jupyter notebook assignments for Princeton's MAE345 class. It is organized in the following manner:

- All Jupyter notebooks are placed in the top level directory so they have access to all other Python modules and paths referenced in them are consistent.
- All data provided / collected for use in assignments resides in `quad_data`.
- The directory `scripts` contains all scripts for running the labs using the Crazyflie.
- The script `install_dependencies.sh` will install the necessary dependencies for running the software for the class on a fresh Ubuntu 18.04 installation. It will also build the firmware for the Bitcraze Crazyflie 2.1 we have modified for the class that is available from [this repository](https://github.com/irom-lab/crazyflie-firmware).

For those not familiar with Linux / Ubuntu, a VirtualBox image will be provided that is already configured for the class.
